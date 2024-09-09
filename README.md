# Proyecto Titanic API

## Descripción

En esta clase vas a convertir un modelo predictivo en un API REST. Puedes usar cualquier modelo que hayas desarrollado en alguna otra materia. El desempeño del modelo no es criterio de evaluación de este proyecto. En este caso se selecciona el proyecto Titanic.

## Estructura del Proyecto

```
proyecto_titanic/
│
├── data/
│   ├── raw/
│   │   └── titanic.csv
│   └── processed/
│       └── titanic_processed.csv
│
├── src/
│   ├── __init__.py
│   ├── prepare_data.py
│   ├── train_model.py
│   └── predict.py
│
├── models/
│   └── model.pkl
│
├── main.py
├── requirements.txt
└── README.md
```

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/proyecto-titanic-api.git
   ```

2. Navega al directorio del proyecto:
   ```
   cd proyecto-titanic-api
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Asegúrate de que el archivo `titanic.csv` esté en la carpeta `data/raw/`.

2. Ejecuta el script principal:
   ```
   python main.py
   ```

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
