import pandas as pd
import csv
from pathlib import Path


def limpiar_deportistas(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )

    # Evita errores de asignacion por dtype al reparar filas mal parseadas.
    df = df.astype("object")

    # --------------------------
    # Normalizar texto y preparar valores nulos
    # --------------------------
    
    for col in df.select_dtypes(include='object').columns:
       
        df[col] = df[col].astype(str).str.strip().replace('nan', pd.NA)
        
        if col != 'nombre':
            df[col] = df[col].str.replace(',', '.', regex=False)

    # --------------------------
    # Reparar filas mal parseadas
    # --------------------------
  
    malformed = df['deporte'].isna() & df['nombre'].astype(str).str.count(',').ge(8)
    if malformed.any():
      
        for idx in df[malformed].index:
            nombre_sucio = df.at[idx, 'nombre']  
            if pd.isna(nombre_sucio):
                continue  
            try:
               
                parsed_row = next(csv.reader([nombre_sucio], quotechar='"', skipinitialspace=True))
            except Exception:
              
                parsed_row = str(nombre_sucio).rsplit(',', 8)
            
            if len(parsed_row) == len(df.columns):
                df.loc[idx, df.columns] = parsed_row
           
    # --------------------------
    # Reaplicar comas decimales a columnas numéricas tras reparación
    # --------------------------
    for col in ['edad', 'peso_kg', 'altura_cm', 'frecuencia_cardiaca_bpm', 'horas_entrenamiento_semana', 'rendimiento_score']:
        if col in df.columns:
         
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False)

    # --------------------------
    # Convertir a numérico
    # --------------------------
    for col in ['edad', 'peso_kg', 'altura_cm', 'frecuencia_cardiaca_bpm', 'horas_entrenamiento', 'horas_entrenamiento_semana', 'rendimiento_score']:
        if col in df.columns:
          
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # --------------------------
    # Detectar y eliminar outliers con IQR
    # --------------------------
    # 6. Eliminar outliers en peso_kg y horas_entrenamiento_semana usando IQR
    for col in ['peso_kg', 'horas_entrenamiento_semana']:
        if col in df.columns:
            # Calcular Q1, Q3 e IQR
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
        
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

    # --------------------------
    # Imputar nulos numéricos con la media de la columna
    # --------------------------
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # --------------------------
    # Normalizar texto de categorías
    # --------------------------
    if 'deporte' in df.columns:
        df['deporte'] = df['deporte'].str.upper().str.strip().replace({
            'NATACIÓN': 'NATACION',
            'NATACIÓ': 'NATACION',
            'NATACIO': 'NATACION',
            'FÚTBOL': 'FUTBOL',
            'VOLLEYBALL': 'VOLEIBOL',
            'TENNIS': 'TENIS',
            'BASKETBALL': 'BALONCESTO'
        })
    if 'posicion' in df.columns:
        df['posicion'] = df['posicion'].str.upper().str.strip()  

    df = df.drop_duplicates()

    output_path = Path(__file__).resolve().parent.parent / 'deportistas_limpios.csv'
    df.to_csv(output_path, index=False)

    return df
