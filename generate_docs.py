import csv
import os

def generate_docs():
    csv_path = os.path.join(os.path.dirname(__file__), "eclipse_ux_issues.csv")
    details_path = os.path.join(os.path.dirname(__file__), "issue_details.md")
    links_path = os.path.join(os.path.dirname(__file__), "issue_links.md")
    
    issues = []
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                issues.append(row)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_path}")
        return
            
    # Generate issue_details.md
    with open(details_path, "w", encoding="utf-8") as f:
        f.write("# Detalles de Issues UX en Eclipse\n\n")
        for issue in issues:
            f.write(f"## Issue #{issue['ID']} - {issue['State'].capitalize()}\n")
            f.write(f"**Título:** {issue['Title']}\n\n")
            f.write(f"**Etiquetas:** {issue['Labels'] if issue['Labels'] else 'Ninguna'}\n\n")
            f.write(f"**Creado:** {issue['Created At'][:10]}\n\n")
            f.write(f"**Enlace:** [{issue['URL']}]({issue['URL']})\n\n")
            f.write("---\n\n")
            
    # Generate issue_links.md
    with open(links_path, "w", encoding="utf-8") as f:
        f.write("# Enlaces Directos a los Issues de UX\n\n")
        f.write("Haz clic en los enlaces a continuación para abrir los problemas directamente en tu navegador. Están listados con su título para fácil identificación:\n\n")
        for issue in issues:
            f.write(f"- [Issue #{issue['ID']}: {issue['Title']}]({issue['URL']})\n")
            
    print("Documentos generados exitosamente.")

if __name__ == "__main__":
    generate_docs()
