<h1>🏠 HousingPricePredictor-Asturias</h1>

<h2>📝 Descripción del Proyecto</h2>
<p>Este proyecto utiliza Machine Learning para predecir los precios de viviendas en Asturias. El modelo se entrena con datos scrapeados de Idealista, que incluyen características como tipo de inmueble, ubicación, metros cuadrados, número de habitaciones y precio. El objetivo es proporcionar una herramienta que ayude a compradores a tomar decisiones informadas sobre viviendas.</p>

<h2>🎯 Objetivos</h2>
<ul>
    <li>Predecir el precio de viviendas en función de sus características.</li>
    <li>Identificar las variables más influyentes en el precio (metros cuadrados, ubicación, etc.).</li>
    <li>Comparar diferentes modelos de Machine Learning para seleccionar el más adecuado.</li>
    <li>Proporcionar una solución práctica para el análisis del mercado inmobiliario en Asturias.</li>
</ul>

<h2>📑 Estructura del Proyecto</h2>
<pre>
📂 HousingPricePredictor-Asturias/
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

<h2>🛠️ Tecnologías</h2>
<ul>
    <li>Python</li>
    <li>Pandas</li>
    <li>Numpy</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
    <li>Scikit-learn</li>
    <li>XGBoost</li>
    <li>LightGBM</li>
</ul>

<h2>🚀 Cómo Ejecutar el Proyecto</h2>
<ol>
    <li>Clona el repositorio:</li>
    <pre>git clone https://github.com/apvwbm/HousingPricePredictor-Asturias.git</pre>
    <li>Instala las dependencias necesarias:</li>
    <pre>pip install -r requirements.txt</pre>
    <li>Explora los notebooks en la carpeta <code>src/notebooks/</code>:</li>
    <pre>jupyter notebook src/notebooks/01_eda.ipynb</pre>
    <li>Consulta los resultados finales en <code>src/results_notebook/final_results.ipynb</code>.</li>
</ol>

<h2>📊 Resultados</h2>
<p>El modelo seleccionado logró un RMSE de X y un R² de Y en el conjunto de prueba. Los detalles completos están disponibles en el notebook final.</p>

<h2>👤 Autor</h2>
<p>Aitor Pérez</p>
<p><a href="https://www.linkedin.com/in/aitor-perez/" target="_blank">LinkedIN</a> | <a href="https://github.com/apvwbm" target="_blank">Github</a></p>