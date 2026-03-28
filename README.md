# ProjectoDeportes
Proyecto Deportes - Análisis de Datos Deportivos
📋 Descripción del Proyecto
Este proyecto es la resolución de la Guía 3 de la asignatura Programación para Ciencia de Datos. Consiste en el análisis completo de un dataset de deportistas, aplicando técnicas de limpieza, transformación y análisis de datos utilizando Python y pandas.

El dataset original contiene 2280 registros con múltiples problemas típicos del mundo real: valores nulos, datos mal parseados, formatos inconsistentes, outliers y registros duplicados.

🎯 Objetivos
Realizar una exploración inicial del dataset para identificar problemas de calidad de datos.

Implementar funciones de limpieza para normalizar y corregir los datos.

Ejecutar un análisis básico para extraer métricas relevantes sobre el rendimiento deportivo.

Exportar los resultados limpios y los análisis generados.

📁 Estructura del Proyecto
text
ProjectoDeportes/
│
├── data/
│   └── deportistas.csv               # Dataset original
│
├── outputs/
│   ├── deportistas_limpios.csv       # Dataset después de limpieza
│   └── analisis_por_deporte.csv      # Promedio de rendimiento por deporte
│
├── src/
│   ├── limpieza.py                   # Función de limpieza de datos
│   └── analisis.py                   # Funciones de análisis estadístico
│
├── analisis.ipynb                    # Notebook con el proceso completo
│
└── README.md                         # Este archivo
🔧 Funciones Implementadas
1. Limpieza de Datos (src/limpieza.py)
La función limpiar_deportistas(df) realiza las siguientes transformaciones:

Normalización de nombres de columnas: convierte a minúsculas, reemplaza espacios por guiones bajos.

Reparación de filas mal parseadas: corrige registros donde los datos están concatenados en la columna nombre.

Conversión de tipos numéricos: transforma columnas como edad, peso_kg, altura_cm, etc., a formato numérico, manejando comas decimales.

Normalización de categorías: unifica nombres de deportes (ej. NATACIÓN → NATACION, FÚTBOL → FUTBOL).

Eliminación de duplicados: remueve filas completamente duplicadas.

Detección y eliminación de outliers: utiliza el método IQR (Rango Intercuartílico) para las columnas peso_kg y horas_entrenamiento_semana.

Imputación de valores nulos: completa los valores faltantes en columnas numéricas con la media de la columna.

2. Análisis de Datos (src/analisis.py)
Resumen_datos(df): retorna un resumen con:

Total de deportistas

Promedio de rendimiento

Edad promedio

Promedio_por_deporte(df): calcula el promedio de rendimiento_score agrupado por deporte.

Deportistas_destacados(df, umbral): filtra los deportistas con rendimiento superior al umbral (por defecto 7.0).

📊 Resultados Obtenidos
Estadísticas después de la limpieza
Métrica	Valor
Registros iniciales	2280
Registros después de limpieza	2135
Deportes únicos	12
Promedio de rendimiento	5.57
Edad promedio	31.08 años
Top 5 Deportes por Rendimiento Promedio
Deporte	Rendimiento Promedio
ATLETISMO	5.96
BOXEO	5.86
TENIS	5.83
RUGBY	5.71
VOLEIBOL	5.64
Deportistas Destacados (rendimiento > 7.0)
Se identificaron 707 deportistas con rendimiento superior a 7.0. Los mejores 5 son:

Nombre	Deporte	Rendimiento
Catalina Mora	VOLEIBOL	9.76
Tomás Gutiérrez	FUTBOL	8.06
Fernanda Jiménez	FUTBOL	8.22
Sebastián Rojas	NATACION	7.16
Paola Romero	ATLETISMO	7.75
