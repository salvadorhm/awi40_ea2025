# awi40_ea2025

## 1. Crear un Virtual Enviroment

Para crear un ambiente virtual y separar la librerias necesarias para un proyecto se utiliza el siguiente comando.

Nota: el ambiente virtual utilizará la versión de Python predeterminada.

```shell
python3 -m venv .venv
```

En caso de necesitar una versión distinta de python por alguna situación de compatibilidad de algunas librerías se especifíca desde la creación, tal como se muestra en los siguientes ejemplos.

```shell
python3.12 -m venv .venv
```

```shell
python3.11 -m venv .venv
```

## 2. Activar un virtual enviroment

Para activar un ambiente virtual de trabajo se activa utilizando el comando source.

```shell
source .venv/bin/activate
```

## 3. Desactivar un vitual enviroment

Para desactivar el ambiente de trabajo se utiliza el comando deactivate.

```shell
deactivate
```

## 4. Ejemplos

Este repositorio contiene una lista de ejemplos del uso del microframework [web.py](https://webpy.org)

|No.|Ejercicio|Descripción| Referencia |
| -- | -- | -- | -- |
|01|00_webapp|Hola mundo de web.py| [Referencia](https://webpy.org/index.es.html) |
|02|01_webapp|Ejemplo de 2 urls y su respectiva clase| [Referencia](https://webpy.org/index.es.html) |
|03|02_webapp|Renderizar un archivo HTML utilizando templetor| [Referencia](https://webpy.org/docs/0.3/templetor) |
|04|03_webapp|Enviar variables desde python al html| [Referencia](https://webpy.org/docs/0.3/templetor) |
|05|04_webapp|Hipervinculos entre dos páginas html| [Referencia](https://webpy.org/docs/0.3/templetor) |
|06|05_webapp|Manejo de formularios html| [Referencia](https://webpy.org/cookbook/input) |
|07|06_webapp|Código python dentro del html| [Referencia](https://webpy.org/docs/0.3/templetor) |
|08|07_webapp|Uso de plantilla base en html| [Referencia](https://webpy.org/docs/0.3/templetor) |
|09|08_webapp|Archivos estaticos| [Referencia](https://webpy.org/cookbook/staticfiles) |
|10|09_webapp|Paginas de error| [Referencia](https://webpy.org/cookbook/custom_notfound) |

