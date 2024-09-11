

from api import obtener_datos
from ui import obtener_entrada_usuario, mostrar_resultados

def main():
    departamento, municipio, cultivo, limit = obtener_entrada_usuario()
    datos = obtener_datos(departamento, municipio, cultivo, limit)
    mostrar_resultados(datos)

if __name__ == "__main__":
    main()