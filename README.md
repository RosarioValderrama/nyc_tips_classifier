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

---

## Tecnologías y Librerías

- Python 3.11
- pandas, numpy, matplotlib, scipy
- scikit-learn
- Jupyter Notebook

---

## Flujo de trabajo

1. **Carga y preprocesamiento:**  
   Lectura de datasets mensuales desde URLs en formato `.parquet`, limpieza de nulos y selección de columnas relevantes.

2. **Generación de features:**  
   Se aplicó ingeniería de características para construir variables predictoras a partir del viaje (`fare_amount`, `trip_distance`, `tip_amount`, etc.).

3. **Entrenamiento del modelo:**  
   Se entrenó un modelo de clasificación (Random Forest) para predecir la variable binaria `high_tip`.

4. **Evaluación mensual:**  
   Se probó el modelo en los meses desde febrero a agosto de 2020, evaluando su **F1-score** en cada caso.

5. **Visualización del rendimiento:**  
   Se generó un gráfico de líneas con la evolución mensual del F1-score, destacando patrones o anomalías.

6. **Análisis crítico:**  
   Se aplicó un test estadístico (Kolmogorov-Smirnov) para comparar la distribución de la variable `fare_amount` entre meses (febrero vs abril), evidenciando que los cambios en los datos afectan el rendimiento del modelo.

---

## Resultados

- El modelo obtuvo un F1-score de entre 0.61 y 0.73 a lo largo de los distintos meses.
- Se observó una caída significativa del rendimiento en abril, posiblemente debido a efectos externos como la pandemia o estacionalidad.
- El test KS entregó una **p-value < 0.05**, lo que indica una diferencia estadísticamente significativa en las distribuciones de `fare_amount` entre meses.

![Gráfico F1-score mensual](reports/figures/f1_mensual.png)

---

## Reproducir el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/usuario/nyc_tips_classifier.git
cd nyc_tips_classifier

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

