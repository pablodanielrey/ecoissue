Este proyecto usa poetry para su administración.
Por lo que cuando se instalan librerias en la documentación se ve:

```bash
pip install nombre-de-librería
```

pero nosotros usaremos 

```bash
poetry add nombre-de-librería.
```


ej:

para instalar la libreria requests vamos a usar:

```bash
poetry add requests
```


# Como ejecutar el programa

## Instalar el entorno para poder ejecutar el programa.
```bash
cd ecoissue
poetry shell
poetry install
```

## Ejecutar el archivo principal del proyecto.

```bash
python3 ecoissue/main.py
```