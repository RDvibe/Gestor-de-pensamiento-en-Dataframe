import pandas as pd
from datetime import datetime
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Nombre de las columnas en tu DataFrame
columnas = ['Fecha', 'Hora', 'Informacion']

# Intentamos cargar el DataFrame desde un archivo existente
try:
    df = pd.read_csv('tu_dataframe.csv')

# Si el archivo no existe, creamos un DataFrame nuevo
except FileNotFoundError:
    df = pd.DataFrame(columns=columnas)

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Insertar nueva información")
    print("2. Visualizar información existente")
    print("3. Borrar información por número")
    print("4. Salir")

    opcion = input("Selecciona una opción (1, 2, 3, 4): ")

    if opcion == '1':
        # Obtén la fecha y hora actuales
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        hora_actual = datetime.now().strftime("%H:%M:%S")

        # Solicita nueva información al usuario
        nueva_informacion = input("Ingresa nueva información rebelde: ")

        # Crea un nuevo registro con la fecha, hora y nueva información
        nuevo_registro = pd.DataFrame([[fecha_actual, hora_actual, nueva_informacion]], columns=columnas)

        # Agrega el nuevo registro al DataFrame existente
        df = pd.concat([df, nuevo_registro], ignore_index=True)

        # Guarda el DataFrame actualizado en un archivo CSV
        df.to_csv('tu_dataframe.csv', index=False)
        print("¡Información añadida y guardada exitosamente!")

    elif opcion == '2':
        # Verifica si hay información en el DataFrame
        if not df.empty:
            # Muestra el DataFrame actual con formato mejorado y color rojo
            print("\nInformación existente:")
            for idx, row in df.iterrows():
                fecha_hora = f"{row['Fecha']} {row['Hora']}" if not pd.isna(row['Hora']) else row['Fecha']
                informacion = f"{Fore.RED}{row['Informacion']}{Style.RESET_ALL}"
                print(f"{Fore.RED}{idx}{Style.RESET_ALL}. {fecha_hora}: {informacion}")
        else:
            print("No hay información en el DataFrame.")

    elif opcion == '3':
        # Pide al usuario el número de entrada que desea borrar
        try:
            numero_borrar = int(input("Ingresa el número de entrada que deseas borrar: "))
            # Verifica si el DataFrame no está vacío y el número de entrada es válido
            if not df.empty and 0 <= numero_borrar < len(df):
                # Borra la fila correspondiente
                df = df.drop(numero_borrar, axis=0).reset_index(drop=True)
                print(f"Entrada número {numero_borrar} borrada exitosamente.")
            else:
                print("Número de entrada no válido. Introduce un número dentro del rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    elif opcion == '4':
        # Guarda el DataFrame actualizado en un archivo CSV antes de salir
        df.to_csv('tu_dataframe.csv', index=False)
        print("¡Hasta luego, rebelde de los datos!")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

