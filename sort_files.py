import os
from collections import defaultdict

# Chemins de base
base_dir = os.path.abspath(os.path.dirname(__file__))
source_dir = os.path.join(base_dir, "Codeforces")
output_file = os.path.join(base_dir, "tags_table.md")

def extract_tags_and_todos(filepath):
    """
    Extrait les tags d'un fichier .py.

    Returns:
        - tags (set): Les catégories du fichier.
    """
    tags = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("# tags:"):
                # Récupère les tags après "# tags:"
                tags = set(map(str.strip, line[7:].split(",")))
                break
    return tags

def get_creation_time(filepath):
    """
    Récupère le temps de création d'un fichier.
    """
    return os.path.getctime(filepath)

# Organise les fichiers par tags
tags_dict = defaultdict(list)

# Parcourt les dossiers A-Z et les fichiers directement dans Codeforces
for root, dirs, files in os.walk(source_dir):
    # Filtrer les dossiers pour ne garder que ceux commençant par A-Z
    if root == source_dir:
        dirs[:] = [d for d in dirs if len(d) == 1 and d.isalpha() and d.isupper()]

    for filename in sorted(files):
        if filename.endswith(".py"):
            filepath = os.path.join(root, filename)

            # Récupère les tags
            tags = extract_tags_and_todos(filepath)

            # Associe chaque fichier à ses tags
            for tag in tags:
                relative_path = os.path.relpath(filepath, source_dir)
                tags_dict[tag].append((relative_path, get_creation_time(filepath)))

            # Classe les fichiers dans des dossiers A-Z
            first_letter = filename[0].upper()
            if not first_letter.isalpha():
                first_letter = "Misc"  # Dossier pour fichiers qui ne commencent pas par une lettre

            dest_dir = os.path.join(source_dir, first_letter)
            os.makedirs(dest_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas

            dest_path = os.path.join(dest_dir, filename)
            if filepath != dest_path:
                os.rename(filepath, dest_path)  # Déplace le fichier dans le bon dossier

# Génère le tableau Markdown
with open(output_file, "w", encoding="utf-8") as f:
    # En-tête du tableau
    f.write("| Tag              | Fichiers associés (triés par date) |\n")
    f.write("|------------------|-----------------------------------|\n")

    # Ajoute les fichiers par tag triés par date de création
    for tag, files in sorted(tags_dict.items()):
        # Trier les fichiers par date de création
        files_sorted = sorted(files, key=lambda x: x[1])
        file_list = ", ".join([file[0] for file in files_sorted])
        f.write(f"| {tag:<16} | {file_list} |\n")

print(f"Tableau des tags généré dans {output_file} !")
print("Fichiers triés par dossiers A-Z dans le répertoire Codeforces.")
