🏋️‍♂️ Proyecto Deportes
📊 Análisis de Datos Deportivos con Python
📋 Descripción

Este proyecto corresponde a la Guía 3 de la asignatura Programación para Ciencia de Datos.

Consiste en el análisis de un dataset de deportistas, aplicando procesos de:

🧹 Limpieza de datos
🔄 Transformación
📊 Análisis

El dataset original contiene 2280 registros con problemas reales como valores nulos, datos mal formateados, duplicados y outliers.

🎯 Objetivo
Explorar el dataset e identificar problemas de calidad
Limpiar y normalizar los datos
Analizar métricas relevantes del rendimiento deportivo
Generar datos confiables para análisis posterior
🛠️ Tecnologías Usadas
🐍 Python
🐼 pandas
📓 Jupyter Notebook
📁 Estructura del Proyecto
ProjectoDeportes/
│
├── data/
│   └── deportistas.csv
│
├── outputs/
│   ├── deportistas_limpios.csv
│   └── analisis_por_deporte.csv
│
├── src/
│   ├── limpieza.py
│   ├── analisis.py
│   └── __init__.py
│
├── analisis.ipynb
└── README.md
🧹 Limpieza de Datos

La función limpiar_deportistas(df) realiza:

Normalización de nombres de columnas
Corrección de datos mal parseados
Conversión a tipos numéricos
Normalización de categorías (deportes)
Eliminación de duplicados
Eliminación de outliers (método IQR)
Imputación de valores nulos con la media
📊 Análisis de Datos

Funciones implementadas:

Resumen_datos(df)
→ Total de deportistas, promedio de rendimiento y edad
Promedio_por_deporte(df)
→ Rendimiento promedio agrupado por deporte
Deportistas_destacados(df, umbral=7.0)
→ Filtra deportistas con alto rendimiento
📊 Resultados
📈 Estadísticas Generales
Métrica	Valor
Registros iniciales	2280
Registros limpios	2135
Deportes únicos	12
Rendimiento promedio	5.57
Edad promedio	31.08
🏆 Top 5 Deportes
Deporte	Rendimiento
ATLETISMO	5.96
BOXEO	5.86
TENIS	5.83
RUGBY	5.71
VOLEIBOL	5.64
⭐ Deportistas Destacados
Total: 707 deportistas con rendimiento > 7.0
Nombre	Deporte	Score
Catalina Mora	VOLEIBOL	9.76
Tomás Gutiérrez	FUTBOL	8.06
Fernanda Jiménez	FUTBOL	8.22
Sebastián Rojas	NATACION	7.16
Paola Romero	ATLETISMO	7.75
📌 Conclusiones
Se corrigieron múltiples problemas de calidad de datos
Se redujo el dataset de 2280 a 2135 registros
Se obtuvo un dataset limpio y confiable
Atletismo y Boxeo destacan en rendimiento
Un alto porcentaje de deportistas supera el umbral de rendimiento
👨‍💻 Autor

Bastián Villalobos
Ingeniería en Informática – DUOC UC
