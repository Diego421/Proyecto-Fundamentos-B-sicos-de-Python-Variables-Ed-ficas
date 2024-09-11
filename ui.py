# ui.py

def obtener_entrada_usuario():
    departamento = input("Ingrese el Departamento: ").strip().upper()
    municipio = input("Ingrese el Municipio: ").strip().upper()
    cultivo = input("Ingrese el Cultivo: ").strip().capitalize()
    
    while True:
        try:
            limit = int(input("Ingrese el número de registros a consultar: ").strip())
            if limit <= 0:
                raise ValueError("El número de registros debe ser positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")
    
    return departamento, municipio, cultivo, limit



def mostrar_resultados(datos):
    if datos.empty:
        print("No se encontraron resultados para los criterios ingresados.")
    else:
        # Filtrar y mostrar columnas deseadas si están presentes en el DataFrame
        columnas_deseadas = ['departamento', 'municipio', 'cultivo', 'topografia']
        columnas_existentes = [col for col in columnas_deseadas if col in datos.columns]
        
        if columnas_existentes:
            print("\nDatos Generales del Cultivo:")
            print(datos[columnas_existentes].to_string(index=False))
        else:
            print("No se encontraron las columnas esperadas en los datos.")
        
        print("\nMediana de las Variables Edáficas:")
        
        # Nombres exactos de las columnas en el DataFrame
        variables_edaficas = {
            'pH': 'ph_agua_suelo_2_5_1_0',
            'Fósforo': 'f_sforo_p_bray_ii_mg_kg',
            'Potasio': 'potasio_k_intercambiable_cmol_kg'
        }
        
        for var_name, col_name in variables_edaficas.items():
            if col_name in datos.columns:
                try:
                    mediana = datos[col_name].astype(float).median()
                    print(f"- {var_name}: {mediana:.2f}")
                except ValueError:
                    print(f"- {var_name}: No se pudo calcular (posibles valores no numéricos)")
            else:
                print(f"- {var_name}: Dato no disponible")




            