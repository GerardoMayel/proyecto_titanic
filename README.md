# Proyecto Titanic API

## Descripción

Este proyecto convierte un modelo predictivo del Titanic en una API REST utilizando Flask.

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
│   ├── prepare_data.py
│   ├── train_model.py
│   └── predict.py
│
├── models/
│   └── model.pkl
│
├── app.py
├── main.py
├── Dockerfile
├── requirements_analisis.txt
├── requirements_api.txt
└── README.md
```

## Instalación y Uso

### Entorno de Análisis

1. Crea y activa el entorno virtual:
   ```
   python3 -m venv env_analisis
   source env_analisis/bin/activate
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements_analisis.txt
   ```

3. Ejecuta el script principal para entrenar el modelo:
   ```
   python main.py
   ```

### API

1. Crea y activa el entorno virtual:
   ```
   python3 -m venv env_api
   source env_api/bin/activate
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements_api.txt
   ```

3. Ejecuta la API:
   ```
   python app.py
   ```

### Docker (opcional)

Para ejecutar la API en un contenedor Docker:

1. Construye la imagen:
   ```
   docker build -t titanic-api .
   ```

2. Ejecuta el contenedor:
   ```
   docker run -p 5000:5000 titanic-api
   ```

## Uso de la API

Envía una solicitud POST a `http://localhost:5000/predict` con los datos del pasajero en formato JSON. Por ejemplo:

```json
{
  "Pclass": 3,
  "Sex": 0,
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": 2
}
```

La API devolverá una predicción de supervivencia (0 o 1).

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)