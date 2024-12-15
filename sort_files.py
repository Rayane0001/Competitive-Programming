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

# Organise les fichiers par tags
tags_dict = defaultdict(list)

for filename in sorted(os.listdir(source_dir)):
    if filename.endswith(".py"):
        filepath = os.path.join(source_dir, filename)

        # Récupère les tags
        tags = extract_tags_and_todos(filepath)

        # Associe chaque fichier à ses tags
        for tag in tags:
            tags_dict[tag].append(filename)

        # Classe les fichiers dans des dossiers A-Z
        first_letter = filename[0].upper()
        if not first_letter.isalpha():
            first_letter = "Misc"  # Dossier pour fichiers qui ne commencent pas par une lettre

        dest_dir = os.path.join(source_dir, first_letter)
        os.makedirs(dest_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas

        dest_path = os.path.join(dest_dir, filename)
        os.rename(filepath, dest_path)  # Déplace le fichier dans le bon dossier

# Génère le tableau Markdown
with open(output_file, "w", encoding="utf-8") as f:
    # En-tête du tableau
    f.write("| Tag              | Fichiers associés           |\n")
    f.write("|------------------|-----------------------------|\n")

    # Ajoute les fichiers par tag
    for tag, files in sorted(tags_dict.items()):
        file_list = ", ".join(files)
        f.write(f"| {tag:<16} | {file_list} |\n")

print(f"Tableau des tags généré dans {output_file} !")
print("Fichiers triés par dossiers A-Z dans le répertoire Codeforces.")
