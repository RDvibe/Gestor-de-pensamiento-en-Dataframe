
# Gestor de Pensamientos en DataFrame

Este script de Python permite gestionar una colección de pensamientos almacenados en un DataFrame de `pandas`. Los pensamientos se guardan en un archivo CSV (`tu_dataframe.csv`) para su persistencia entre ejecuciones. Además, utiliza `colorama` para mejorar la visualización en la terminal.

## Características

- Insertar nuevos pensamientos con fecha y hora actuales.
- Visualizar todos los pensamientos existentes con índices.
- Borrar pensamientos específicos utilizando su número de índice.
- Salir y guardar automáticamente los cambios en el archivo CSV.

## Requisitos

Para ejecutar este script, necesitas tener Python instalado en tu sistema, así como las siguientes librerías:

- `pandas`: Para la manipulación y gestión del DataFrame.
- `colorama`: Para agregar color al texto en la terminal, mejorando la experiencia de usuario.

Puedes instalar estas dependencias con el siguiente comando:

```
pip install pandas colorama
```

## Uso

Para ejecutar el script, navega en la terminal hasta el directorio donde se encuentra el archivo `.py` y ejecuta:

```
python nombre_del_script.py
```

Sigue las instrucciones en pantalla para gestionar tus pensamientos. Elige entre insertar un nuevo pensamiento, visualizar los pensamientos existentes, borrar pensamientos o salir del script.
