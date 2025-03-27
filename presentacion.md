# 🏠 Predicción de Precios de Viviendas en Asturias — Proyecto de Machine Learning

## 🎯 Objetivo General

Desarrollar un modelo predictivo capaz de estimar el **precio de venta de una vivienda** en Asturias a partir de sus características principales, identificar las variables más influyentes en la determinación del precio y comparar distintos modelos de Machine Learning para ofrecer una solución práctica y aplicable al análisis del mercado inmobiliario.

---

## 🧭 Metodología

### 🧹 Preprocesado de Datos
- **Codificación**:
  - One-Hot Encoding para variables categóricas con pocas categorías.
  - Target Encoding para variables con alta cardinalidad (`barrio`, `municipio`, `distrito`).
- **Escalado de variables numéricas** con `StandardScaler`.
- **Limpieza y selección de variables** para evitar colinealidad y reducir ruido.

### 🤖 Modelado
Se entrenaron y compararon varios modelos de regresión:
- `LinearRegression`
- `RandomForestRegressor`
- `XGBoostRegressor`
- `CatBoostRegressor`

### 📏 Evaluación
- **Métricas utilizadas**:  
  - MAE (Mean Absolute Error)  
  - RMSE (Root Mean Squared Error)  
  - R² (Coeficiente de determinación)

- **Visualizaciones**:
  - Gráficos de predicción vs. precio real
  - Análisis de errores
  - Importancia de variables

---

## 📊 Resultados

| Modelo              | MAE (€)   | RMSE (€)   | R²     |
|---------------------|-----------|------------|--------|
| **XGBoost (top 7)** | **7.446** | **46.321** | **0.9175** |
|            XGBoost  | 7.549     | 46.855     | 0.9156 |
|      Random Forest  | 6.328     | 53.158     | 0.8913 |
|           CatBoost  | 5.839     | 55.382     | 0.8820 |
|  Linear Regression  | 24.688    | 59.016     | 0.8660 |  

> ✨ El modelo XGBoost con solo 7 variables alcanzó una precisión considerable con un R² de **0.9175** y un error medio de **7.446 €**.

---

## 🔍 Variables más influyentes

Según el análisis de **Permutation Importance**, las variables más determinantes para predecir el precio son:

1. `m2_construidos`
2. `precio_por_habitacion`
3. `euros_m2`
4. `precio_por_bano`
5. `barrio_encoded`
6. `habitaciones`
7. `banios`

> ✅ La superficie y la **ubicación a nivel de barrio** son los factores clave del precio.

---

## ✅ Conclusiones

- Se puede estimar el precio de un inmueble en Asturias con gran precisión utilizando solo unas pocas variables bien seleccionadas.
- El modelo **XGBoost** ha ofrecido la mejor combinación de rendimiento y capacidad interpretativa.
- El modelo reducido (7 variables) simplifica el proceso sin sacrificar precisión.
- La metodología es **escalable** y puede aplicarse a otras regiones con ajustes mínimos, haciendo falta únicamente cambiar los datos.
- Esta solución puede servir como base para **herramientas de valoración automática**, **análisis de mercado** o **soporte a la toma de decisiones inmobiliarias**.