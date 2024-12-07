import os
import subprocess
import argparse

def convert_md_to_json(directory_path):
    """
    Parcourt tous les fichiers Markdown d'un dossier et les convertit en JSON.

    :param directory_path: Chemin du dossier contenant les fichiers .md
    """
    # Vérifie si le dossier existe
    if not os.path.isdir(directory_path):
        print(f"Le dossier '{directory_path}' n'existe pas.")
        return

    # Parcourt tous les fichiers du dossier
    for filename in os.listdir(directory_path):
        if filename.endswith(".md"):  # Vérifie si le fichier est un fichier Markdown
            file_path = os.path.join(directory_path, filename)
            output_path = file_path.replace(".md", ".json")  # Génère le chemin du fichier de sortie

            print(f"Conversion de '{file_path}' en '{output_path}'...")
            try:
                # Exécute la commande md_to_json
                subprocess.run(["md_to_json", file_path, "-o", output_path], check=True)
                print(f"Fichier '{file_path}' converti avec succès.")
            except subprocess.CalledProcessError as e:
                print(f"Erreur lors de la conversion de '{file_path}': {e}")

if __name__ == "__main__":
    # Configure argparse pour accepter un argument pour le chemin du dossier
    parser = argparse.ArgumentParser(description="Convertir des fichiers Markdown en JSON.")
    parser.add_argument("directory", help="Chemin du dossier contenant les fichiers Markdown")
    
    # Parse les arguments
    args = parser.parse_args()

    # Appelle la fonction avec le chemin fourni
    convert_md_to_json(args.directory)
