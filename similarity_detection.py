import os
from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

# Initialisation de Flask
app = Flask(__name__)

# Initialisation du modèle CodeBERT
model_name = "microsoft/codebert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Chemins de base
base_dir = os.path.abspath(os.path.dirname(__file__))
training_dirs = ["Codeforces", "CSES", "Jean-Perrin"]
training_dirs = [os.path.join(base_dir, d) for d in training_dirs]

def read_file(filepath):
    """
    Lit le contenu d'un fichier.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def encode_code(content):
    """
    Encode le code source en un vecteur à l'aide de CodeBERT.
    """
    inputs = tokenizer(content, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def extract_tags(content):
    """
    Détecte des mots-clés simples pour générer des tags à partir du contenu du code.
    """
    tags = set()
    keywords = {
        "graph": ["bfs", "dfs", "dijkstra", "graph"],
        "string": ["substring", "prefix", "suffix", "string"],
        "dp": ["dp", "dynamic programming", "memoization"],
        "math": ["modulo", "gcd", "lcm", "prime", "factor"],
        "sorting": ["sort", "sorted", "quicksort", "mergesort"],
    }
    for tag, words in keywords.items():
        if any(word in content.lower() for word in words):
            tags.add(tag)
    return tags

# Analyse des fichiers
files = []
file_vectors = {}
file_tags = defaultdict(set)
for directory in training_dirs:
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(root, filename)
                files.append(filepath)
                content = read_file(filepath)
                file_vectors[filepath] = encode_code(content)
                file_tags[filepath].update(extract_tags(content))

# Calcul des similarités
similarities = defaultdict(list)
file_list = list(file_vectors.keys())
for i in range(len(file_list)):
    for j in range(i + 1, len(file_list)):
        file1, file2 = file_list[i], file_list[j]
        vec1, vec2 = file_vectors[file1], file_vectors[file2]
        score = cosine_similarity([vec1], [vec2])[0][0]
        if score > 0.7:  # Seuil pour afficher uniquement les résultats significatifs
            similarities[file1].append((file2, score))
            similarities[file2].append((file1, score))

# Routes Flask
@app.route("/")
def home():
    """
    Affiche la page d'accueil avec la liste des programmes et la barre de recherche.
    """
    return render_template("index.html", files=files, tags=dict(file_tags))


@app.route("/search", methods=["GET"])
def search():
    """
    Recherche les fichiers correspondant à un tag donné.
    """
    query = request.args.get("query", "").lower()

    if not query:
        return jsonify({"error": "No query provided"})

    results = {}

    # Recherche des fichiers qui correspondent à la requête
    for file, tags in file_tags.items():
        if any(query in tag.lower() for tag in tags):  # Recherche insensible à la casse
            results[file] = list(tags)

    return jsonify(results)

@app.route("/similar/<path:filepath>")
def similar(filepath):
    """
    Retourne les programmes similaires à un fichier donné.
    """
    filepath = os.path.join(base_dir, filepath)
    similar_files = similarities.get(filepath, [])
    return jsonify(similar_files)

# Lancement de l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
