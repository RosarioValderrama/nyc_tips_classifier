# NYC Tips Classifier 🚖

Este proyecto tiene como objetivo predecir la probabilidad de que un viaje en taxi en NYC (2020) reciba una propina, utilizando técnicas de Machine Learning. El código ha sido estructurado siguiendo buenas prácticas de ingeniería de software y ciencia de datos.

---

## Estructura del Proyecto

```text
├── data/
│   ├── raw/           <- Datos originales descargados
│   └── processed/     <- Datos transformados para modelado
├── models/            <- Modelos entrenados y serializados
├── notebooks/         <- Notebooks para exploración y validación
├── src/
│   ├── __init__.py
│   ├── config.py              <- Parámetros y rutas globales
│   ├── data/
│   │   └── dataset.py         <- Carga y limpieza básica de datos
│   ├── features/
│   │   └── build_features.py  <- Generación de variables predictoras
│   ├── modeling/
│   │   ├── train.py           <- Entrenamiento del modelo
│   │   └── predict.py         <- Predicción y evaluación
│   └── visualization/
│       └── plots.py           <- Visualización de resultados
├── requirements.txt     <- Lista de dependencias del proyecto
├── README.md            <- Este archivo

```

## Instalación

```shell
conda create --name cookiecutter-ids -c conda-forge python=3.11
conda activate cookiecutter-ids
pip install -r requirements.txt
```

## Referencia
Este proyecto utiliza la estructura basada en el template de [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science).

## Autora
Rosario Valderrama Labarca
Magíster en Data Science — Universidad del Desarrollo

