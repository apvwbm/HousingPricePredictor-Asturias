<h1>🏠 ML_AsturiasHousingPricePredictor</h1>

<p>
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--Learn-OK-orange" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/XGBoost-success-brightgreen" alt="XGBoost">
</p>

<hr>

<h2>📝 Descripción del Proyecto</h2>

<p>
  Este proyecto aplica técnicas de Machine Learning para <strong>predecir el precio de viviendas en Asturias</strong> a partir de datos reales obtenidos desde Idealista.
</p>
<p>
  Los datos incluyen información como:
</p>
<ul>
  <li>Tipo de inmueble</li>
  <li>Ubicación (barrio, municipio, distrito)</li>
  <li>Superficie construida</li>
  <li>Número de habitaciones y baños</li>
  <li>Precio de venta</li>
</ul>
<p>
  El objetivo es crear una herramienta que ayude a compradores, agentes o analistas a <strong>tomar decisiones informadas</strong> en el mercado inmobiliario.
</p>

<hr>

<h2>🎯 Objetivos</h2>
<ul>
  <li>🧠 Predecir el precio de viviendas en función de sus características.</li>
  <li>📊 Identificar las variables más influyentes en el precio (metros cuadrados, ubicación, etc.).</li>
  <li>⚖️ Comparar diferentes modelos de Machine Learning para seleccionar el más adecuado.</li>
  <li>🌍 Proporcionar una solución práctica para el análisis del mercado inmobiliario en Asturias.</li>
</ul>

<hr>

<h2>📑 Estructura del Proyecto</h2>
<pre>
📂 ML_AsturiasHousingPricePredictor/
├── 📂 src/
│   ├── 📂 data_sample/          # Datos de muestra en formato CSV.
│   │   └── idealista_data_asturias.csv
│   ├── 📂 img/                  # Imágenes y gráficos generados durante el EDA.
│   │   ├── price_distribution.png
│   │   ├── correlation_heatmap.png
│   │   └── ...
│   ├── 📂 notebooks/            # Notebooks de pruebas y exploración.
│   │   ├── 01_eda.ipynb
│   │   ├── 02_preprocessing.ipynb
│   │   └── 03_model_training.ipynb
│   ├── 📂 results_notebook/     # Notebook final con resultados consolidados.
│   │   └── final_results.ipynb
│   ├── 📂 models/               # Modelos entrenados guardados.
│   │   ├── random_forest_model.pkl
│   │   ├── xgboost_model.pkl
│   │   └── ...
│   └── 📂 utils/                # Funciones auxiliares y módulos personalizados.
│       ├── preprocessing.py
│       ├── evaluation.py
│       └── visualization.py
│
├── .gitignore                  # Archivos y carpetas a ignorar por Git.
├── README.md                   # Descripción breve del proyecto.
├── requirements.txt            # Archivo de requisitos del proyecto.
└── LICENSE                     # Licencia del proyecto.
</pre>

<hr>

<h2>🛠️ Tecnologías utilizadas</h2>
<ul>
  <li>Python</li>
  <li>Pandas, NumPy</li>
  <li>Matplotlib, Seaborn</li>
  <li>Scikit-learn</li>
  <li>XGBoost, CatBoost, LightGBM</li>
  <li>SHAP (interpretabilidad)</li>
  <li>Jupyter Notebook</li>
</ul>

<hr>

<h2>🚀 Cómo ejecutar el proyecto</h2>

<ol>
  <li><strong>Clona el repositorio:</strong>
    <pre><code>git clone https://github.com/apvwbm/ML_AsturiasHousingPricePredictor.git
cd ML_AsturiasHousingPricePredictor</code></pre>
  </li>

  <li><strong>(Opcional) Crea un entorno virtual:</strong>
    <pre><code>python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows</code></pre>
  </li>

  <li><strong>Instala las dependencias:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Explora los notebooks:</strong>
    <pre><code>jupyter notebook src/notebooks/01_eda.ipynb</code></pre>
  </li>

  <li><strong>Consulta los resultados finales:</strong>
    <pre><code>src/results_notebook/final_results.ipynb</code></pre>
  </li>
</ol>

<hr>

<h2>📊 Resultados</h2>

<p>El modelo seleccionado fue <strong>XGBoost</strong>, entrenado únicamente con las 7 variables más influyentes según <code>permutation_importance</code>. Obtuvo los siguientes resultados:</p>

<ul>
  <li><strong>MAE</strong>: 7.446 €</li>
  <li><strong>RMSE</strong>: 46.321 €</li>
  <li><strong>R²</strong>: 0.9175</li>
</ul>

<p><strong>📌 Esto demuestra que con un conjunto reducido de variables se puede lograr una predicción precisa y eficiente del precio de la vivienda.</strong></p>

<hr>

<h2>✅ Conclusiones</h2>

<ul>
  <li>El modelo puede estimar precios de viviendas en Asturias con una <strong>precisión del 91.7% (R²)</strong>.</li>
  <li>La <strong>superficie construida</strong> y la <strong>ubicación a nivel de barrio</strong> son los factores más determinantes.</li>
  <li>Se ha logrado reducir el número de variables sin perder precisión, mejorando la eficiencia.</li>
  <li>El enfoque es adaptable a otras regiones y puede servir como base para herramientas de valoración automática.</li>
</ul>

<hr>

<h2>👤 Autor</h2>

<p><strong>Aitor Pérez</strong></p>
<p>
  <a href="https://www.linkedin.com/in/aitor-perez/" target="_blank">LinkedIn</a> |
  <a href="https://github.com/apvwbm" target="_blank">GitHub</a>
</p>