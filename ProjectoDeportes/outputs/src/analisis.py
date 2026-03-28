import pandas as pd
from pathlib import Path


def Resumen_datos(df: pd.DataFrame) -> pd.Series:
	# Devuelve métricas generales del dataset de deportistas.
	return pd.Series(
		{
			"total_deportistas": df.shape[0],
			"promedio_rendimiento": df["rendimiento_score"].mean(),
			"edad_promedio": df["edad"].mean(),
		}
	)


def Promedio_por_deporte(df: pd.DataFrame) -> pd.DataFrame:
	# Calcula el promedio de rendimiento agrupado por deporte.
	resultado = (
		df.groupby("deporte")["rendimiento_score"]
		.mean()
		.reset_index(name="promedio_rendimiento")
	)

	output_path = Path(__file__).resolve().parent.parent / "analisis_por_deporte.csv"
	resultado.to_csv(output_path, index=False)

	return resultado


def Deportistas_destacados(df: pd.DataFrame, umbral: float = 7.0) -> pd.DataFrame:
	# # Filtra deportistas con rendimiento_score mayor al umbral.
	return df[df["rendimiento_score"] > umbral].copy()
