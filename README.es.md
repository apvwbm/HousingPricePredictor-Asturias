<h1>🏠 Predictor de Precios de Vivienda en Asturias</h1>
<p>
 <a href="https://github.com/apvwbm/ML_AsturiasHousingPricePredictor"><img src="https://img.shields.io/badge/EN-English-blue?style=for-the-badge" alt="English"></a>
</p>
<p> <img src="https://img.shields.io/badge/Python-3.12.8-blue?style=flat&logo=python&logoColor=ffdd54" alt="Python"> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" alt="Scikit-learn"> <img src="https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas" alt="Pandas"> <img src="https://img.shields.io/badge/XGBoost-success-brightgreen" alt="XGBoost"> </p>
<hr>
<h2>📝 Descripción del Proyecto</h2>
<p> Este proyecto aplica técnicas de Machine Learning para <strong>predecir precios de viviendas en Asturias, España</strong>, utilizando datos reales recopilados de Idealista. </p>
<p> El conjunto de datos incluye información como: </p>
<ul>
    <li>Tipo de propiedad</li>
    <li>Ubicación (barrio, municipio, distrito)</li>
    <li>Superficie construida (metros cuadrados)</li>
    <li>Número de habitaciones y baños</li>
    <li>Precio de venta</li>
</ul>
<p> El objetivo es desarrollar una herramienta que ayude a compradores, agentes inmobiliarios o analistas a <strong>tomar decisiones informadas</strong> en el mercado inmobiliario. </p>
<hr>
<h2>🎯 Objetivos</h2>
<ul>
    <li>🧠 Predecir los precios de la vivienda en función de sus características.</li>
    <li>📊 Identificar las variables más influyentes en el precio (metros cuadrados, ubicación, etc.).</li>
    <li>⚖️ Comparar distintos modelos de Machine Learning para elegir el más adecuado.</li>
    <li>🌍 Ofrecer una solución práctica para analizar el mercado inmobiliario asturiano.</li>
</ul>
<hr>
<h2>📑 Estructura del Proyecto</h2>
<pre>
📂 ML_AsturiasHousingPricePredictor/
├── 📂 src/
│   ├── 📂 data_sample/
│   │   ├── cleaned_dataset.csv
│   │   └── scrap_data_asturias.csv
│   ├── 📂 img/
│   │   ├── additional_features.png
│   │   ├── correlation_heatmap_extended.png
│   │   └── ...
│   ├── 📂 models/
│   │   ├── xgb_full_model.pkl
│   │   └── xgb_reduced_model.pkl
│   ├── 📂 notebooks/
│   │   ├── eda.ipynb
│   │   └── preprocessing.ipynb
│   ├── 📂 results_notebook/
│   │   └── final_results.ipynb
│   └── 📂 utils/
│       ├── bootcampviztools.py
│       └── toolbox_ML.py
│
├── .gitignore
├── README.md
└── requirements.txt
</pre>
<hr>
<h2>🛠️ Tecnologías Utilizadas</h2>
<ul>
    <li>Python</li>
    <li>Pandas, NumPy</li>
    <li>Matplotlib, Seaborn</li>
    <li>Scikit-learn</li>
    <li>XGBoost, CatBoost, LightGBM</li>
    <li>Jupyter Notebook</li>
</ul>
<hr>
<h2>🚀 Cómo Ejecutar el Proyecto</h2>
<ol>
    <li><strong>Clona el repositorio:</strong>
        <pre><code>git clone https://github.com/apvwbm/ML_AsturiasHousingPricePredictor.git 
        cd ML_AsturiasHousingPricePredictor</code></pre>
    </li>
    <li><strong>(Opcional) Crea un entorno virtual:</strong>
        <pre><code>python -m venv venv
        source venv/bin/activate # macOS/Linux 
        venv\Scripts\activate # Windows</code></pre>
    </li>
    <li><strong>Instala las dependencias:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Explora los notebooks:</strong>
        <pre><code>jupyter notebook src/notebooks/*.ipynb</code></pre>
    </li>
    <li><strong>Consulta los resultados finales:</strong>
        <pre><code>jupyter notebook src/results_notebook/final_results.ipynb</code></pre>
    </li>
</ol>
<hr>
<h2>📊 Resultados</h2>
<p>El modelo seleccionado fue <strong>XGBoost</strong>, entrenado utilizando solo las 7 variables más influyentes según <code>permutation_importance</code>. Se obtuvieron los siguientes resultados:</p>
<ul>
    <li><strong>MAE</strong>: 7.446 €</li>
    <li><strong>RMSE</strong>: 46.321 €</li>
    <li><strong>R²</strong>: 0,9175</li>
</ul>
<p><strong>📌 Esto demuestra que es posible realizar predicciones precisas y eficientes del precio de la vivienda incluso con un conjunto reducido de variables.</strong></p>
<hr>
<h2>✅ Conclusiones</h2>
<ul>
    <li>El modelo puede estimar los precios de la vivienda en Asturias con una <strong>precisión del 91,7% (R²)</strong>.</li>
    <li>La <strong>superficie construida</strong> y la <strong>ubicación del barrio</strong> son los factores más determinantes.</li>
    <li>Se logró reducir el número de variables sin perder precisión, mejorando así la eficiencia.</li>
    <li>Este enfoque es adaptable a otras regiones y sirve como base para herramientas automáticas de tasación.</li>
</ul>
<hr>
<h2>👤 Autor</h2>
<p><strong>Aitor Pérez</strong></p>
<p> <a href="https://www.linkedin.com/in/aitor-perez/" target="_blank">LinkedIn</a> | <a href="https://github.com/apvwbm" target="_blank">GitHub</a> </p>