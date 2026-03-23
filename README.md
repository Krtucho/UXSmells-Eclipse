# UXSmells-Eclipse

Este proyecto tiene como objetivo extraer, analizar y documentar problemas de Experiencia de Usuario (UX) e Interfaz de Usuario (UI) en el IDE de Eclipse, específicamente explorando el repositorio `eclipse-platform/eclipse.platform.ui`.

## Estructura del Proyecto

### Directorio `/scripts`
- `extract_issues.py`: Script en Python que se conecta a la API de GitHub para buscar issues que coincidan con palabras clave relacionadas a UX (como "UX", "UI", "usability", "smell", "layout"). Los descarga de forma paginada esquivando los límites estándar de la API y los exporta a CSV.
- `analyze_issues.py`: Script de análisis rápido que lee el archivo CSV y extrae estadísticas clave, contabilizando las etiquetas más usadas y la frecuencia de términos en los títulos (elimina palabras vacías).
- `generate_docs.py`: Script utilizado para convertir la tabla CSV generada en documentos Markdown de documentación.

### Directorio `/results`
- `eclipse_ux_issues.csv`: El conjunto de datos resultante con todos los issues extraídos.
- `issue_details.md`: Un documento autogenerado que detalla el título, estado, etiquetas y fecha de creación de cada issue individual, formando un catálogo fácil de investigar.
- `issue_links.md`: Una lista enfocada únicamente en proporcionar enlaces directos y clickeables a cada issue referenciado, ideal para abrir cada problema en el navegador de forma directa.

### Directorio `/docs`
- `task.md`: Archivo de seguimiento iterativo que se usó para planificar y registrar el progreso a nivel técnico durante la creación de los scripts y la extracción de datos.
- `analysis_results.md`: Documento preliminar que detalla los "UX smells" principales detectados, clasificándolos en categorías comunes basándose en el recuento automático.
- `all_repository_labels.md`: Listado exhaustivo de todas las 29 etiquetas extraídas directamente de la API de GitHub para el repositorio principal de interfaz de Eclipse.

## Cómo usar el proyecto

1. Si deseas extraer nuevos datos de GitHub, ejecuta:
   ```bash
   python3 scripts/extract_issues.py
   ```
2. Para procesar el nuevo CSV y obtener las estadísticas de las palabras clave de los UX Smells, ejecuta:
   ```bash
   python3 scripts/analyze_issues.py
   ```
3. Finalmente, para generar y actualizar los archivos de documentación Markdown basados en el CSV actual (`results/issue_details.md` y `results/issue_links.md`), ejecuta:
   ```bash
   python3 scripts/generate_docs.py
   ```
