<h1>🏠 Asturias Housing Price Predictor</h1>
<p>
 <a href="https://github.com/apvwbm/ML_AsturiasHousingPricePredictor/blob/main/README.es.md"><img src="https://img.shields.io/badge/ES-Espa%C3%B1ol-red?style=for-the-badge" alt="Español"></a>
</p>
<p>
 <img src="https://img.shields.io/badge/Python-3.12.8-blue?style=flat&logo=python&logoColor=ffdd54" alt="Python">
 <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
 <img src="https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas" alt="Pandas">
 <img src="https://img.shields.io/badge/XGBoost-success-brightgreen" alt="XGBoost">
</p>

<hr>

<h2>📝 Project Description</h2>
<p> This project applies Machine Learning techniques to <strong>predict housing prices in Asturias, Spain</strong>, using real-world data collected from Idealista. </p>
<p> The dataset includes information such as: </p>
<ul>
  <li>Property type</li>
  <li>Location (neighborhood, municipality, district)</li>
  <li>Built area (square meters)</li>
  <li>Number of bedrooms and bathrooms</li>
  <li>Selling price</li>
</ul>
<p> The goal is to develop a tool that helps buyers, real estate agents, or analysts to <strong>make informed decisions</strong> in the property market. </p>

<hr>

<h2>🎯 Objectives</h2>
<ul>
  <li>🧠 Predict housing prices based on property features.</li>
  <li>📊 Identify the most influential variables affecting price (square meters, location, etc.).</li>
  <li>⚖️ Compare different Machine Learning models to choose the most suitable one.</li>
  <li>🌍 Provide a practical solution for analyzing the real estate market in Asturias.</li>
</ul>

<hr>

<h2>📑 Project Structure</h2>
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

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>Python</li>
  <li>Pandas, NumPy</li>
  <li>Matplotlib, Seaborn</li>
  <li>Scikit-learn</li>
  <li>XGBoost, CatBoost, LightGBM</li>
  <li>Jupyter Notebook</li>
</ul>

<hr>

<h2>🚀 How to Run the Project</h2>
<ol>
  <li><strong>Clone the repository:</strong>
    <pre><code>git clone https://github.com/apvwbm/ML_AsturiasHousingPricePredictor.git
cd ML_AsturiasHousingPricePredictor</code></pre>
  </li>
  <li><strong>(Optional) Create a virtual environment:</strong>
    <pre><code>python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows</code></pre>
  </li>
  <li><strong>Install the dependencies:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><strong>Explore the notebooks:</strong>
    <pre><code>jupyter notebook src/notebooks/*.ipynb</code></pre>
  </li>
  <li><strong>Check the final results:</strong>
    <pre><code>jupyter notebook src/results_notebook/final_results.ipynb</code></pre>
  </li>
</ol>

<hr>

<h2>📊 Results</h2>
<p>The selected model was <strong>XGBoost</strong>, trained using only the 7 most influential features according to <code>permutation_importance</code>. It achieved the following results:</p>
<ul>
  <li><strong>MAE</strong>: €7,446</li>
  <li><strong>RMSE</strong>: €46,321</li>
  <li><strong>R²</strong>: 0.9175</li>
</ul>
<p><strong>📌 This demonstrates that precise and efficient housing price predictions are achievable even with a reduced set of variables.</strong></p>

<hr>

<h2>✅ Conclusions</h2>
<ul>
  <li>The model can estimate housing prices in Asturias with an <strong>accuracy of 91.7% (R²)</strong>.</li>
  <li><strong>Built area</strong> and <strong>neighborhood location</strong> are the most determining factors.</li>
  <li>The number of features was successfully reduced without sacrificing accuracy, enhancing efficiency.</li>
  <li>This approach is adaptable to other regions and serves as a basis for automated valuation tools.</li>
</ul>

<hr>

<h2>👤 Author</h2>
<p><strong>Aitor Pérez</strong></p>
<p>
 <a href="https://www.linkedin.com/in/aitor-perez/" target="_blank">LinkedIn</a> | <a href="https://github.com/apvwbm" target="_blank">GitHub</a>
</p>
