# api.py
import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, municipio, cultivo, limit=100):
    try:
        client = Socrata("www.datos.gov.co", None)
        
        # Usar el parámetro where para filtrar directamente en la API
        consulta = f"departamento='{departamento}' AND municipio='{municipio}' AND cultivo='{cultivo}'"
        resultados = client.get("ch4u-f3i5", where=consulta, limit=limit)
        
        if not resultados:
            raise ValueError("No se encontraron datos para los parámetros especificados.")
        
        # Convertir los resultados a un DataFrame de Pandas
        df = pd.DataFrame.from_records(resultados)
        
        # Renombrar columnas si es necesario
        if 'topografia' in df.columns:
            df.rename(columns={'topografia': 'topografia'}, inplace=True)
        
        return df
    
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error