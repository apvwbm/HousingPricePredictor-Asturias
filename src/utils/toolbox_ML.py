# toolbox_ML.py

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


def describe_df(df):
    """
    Función para describir un DataFrame de pandas proporcionando información sobre el tipo de datos,
    valores faltantes, valores únicos y cardinalidad.

    Params:
        df: DataFrame de pandas.

    Returns:
        DataFrame con la información recopilada sobre el DataFrame de entrada.
    """

    if not isinstance(df, pd.DataFrame):
        raise ValueError("El argumento 'df' debe ser un DataFrame de pandas válido.")

    # Creamons un diccionario para almacenar la información
    data = {
        'DATA_TYPE': df.dtypes,
        'MISSINGS(%)': df.isnull().mean() * 100,
        'UNIQUE_VALUES': df.nunique(),
        'CARDIN(%)': round(df.nunique() / len(df) * 100, 3)
    }

    # Creamos un nuevo DataFrame con la información recopilada, usamos 'transpose' para cambiar
    # las filas por columnas.
    estudiantes_df = pd.DataFrame(data).transpose()

    return estudiantes_df


def tipifica_variable(df, umbral_categoria=10, umbral_continua=30.0, motrar_card=False):
    """
    Función para tipificar variables como binaria, categórica, numérica continua y numérica discreta.
    
    Params:
        df (pd.DataFrame): DataFrame de pandas.
        umbral_categoria (int): Valor entero que define el umbral de la cardinalidad para variables categóricas.
        umbral_continua (float): Valor flotante que define el umbral de la cardinalidad para variables numéricas continuas.
        motrar_card (bool): Si es True, incluye la cardinalidad y el porcentaje de cardinalidad. False por defecto. 
    
    Returns:
        DataFrame con las columnas (variables), la tipificación sugerida de cada una.     
        y el tipo real detectado por pandas. Si `motrar_card` es True, también incluye las columnas 
        "CARD" (cardinalidad absoluta) y "%_CARD" (porcentaje de cardinalidad relativa).
    """
    
    # Validación del DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El argumento 'df' debe ser un DataFrame de pandas válido.")
    
    # Validación de los umbrales
    if not isinstance(umbral_categoria, int) or umbral_categoria <= 0:
        raise ValueError("El 'umbral_categoria' debe ser un número entero mayor que 0.")
    
    if not isinstance(umbral_continua, (float, int)) or umbral_continua <= 0:
        raise ValueError("El 'umbral_continua' debe ser un número float mayor que 0.")
    
    # DataFrame inicial con cardinalidad y tipificación sugerida
    df_card = pd.DataFrame({
        "CARD": df.nunique(),
        "%_CARD": round((df.nunique() / len(df) * 100),2),
        "tipo_sugerido": "",
        "tipo_real": df.dtypes.astype(str)
    })
    
    # Tipo Binaria
    df_card.loc[df_card["CARD"] == 2, "tipo_sugerido"] = "Binaria"
    
    # Tipo Categórica
    df_card.loc[(df_card["CARD"] < umbral_categoria) & (df_card["tipo_sugerido"] == ""), "tipo_sugerido"] = "Categórica"
    
    # Tipo Numérica Continua
    df_card.loc[(df_card["CARD"] >= umbral_categoria) & (df_card["%_CARD"] >= umbral_continua), "tipo_sugerido"] = "Numerica Continua"
    
    # Tipo Numérica Discreta
    df_card.loc[(df_card["CARD"] >= umbral_categoria) & (df_card["%_CARD"] < umbral_continua), "tipo_sugerido"] = "Numerica Discreta"

    # Selección y renombrado de columnas
    df_card = df_card.reset_index().rename(columns={"index": "nombre_variable"})
    
    if motrar_card == False:
        return df_card[["nombre_variable", "tipo_sugerido", "tipo_real"]]
    else:
        return df_card[["nombre_variable", "CARD", "%_CARD", "tipo_sugerido", "tipo_real"]]



def get_features_num_regression(df, target_col, umbral_corr, pvalue=None):
    """
    Función para seleccionar características basadas en la correlación con la variable objetivo.

    Params:
        df: DataFrame de pandas.
        target_col: Nombre de la columna objetivo en el DataFrame.
        umbral_corr: Valor flotante que define el umbral de la correlación para seleccionar características.
        pvalue: Valor flotante opcional que define el umbral de significancia para filtrar características basadas en el valor p.

    Returns:
        Lista de características que cumplen con los criterios de selección.
    """
    # Comprobaciones de los argumentos de entrada
    if not isinstance(df, pd.DataFrame):
        # comprueba que el primer argumento sea un DataFrame
        print("El primer argumento debe ser un DataFrame.")
        return None
    if target_col not in df.columns:
        # comprueba que la columna target exista en el DataFrame
        print(f"La columna '{target_col}' no existe en el DataFrame.")
        return None
    if not pd.api.types.is_numeric_dtype(df[target_col]):
        # comprueba que la columna target sea numérica
        print(f"La columna '{target_col}' no es numérica.")
        return None
    if not (0 <= umbral_corr <= 1):
        # comprueba que el umbral de correlación esté entre 0 y 1
        print("El umbral de correlación debe estar entre 0 y 1.")
        return None
    if pvalue is not None and not (0 <= pvalue <= 1):
        # comprueba que el valor de pvalue esté entre 0 y 1
        print("El valor de pvalue debe estar entre 0 y 1.")
        return None

        # Calcular la correlación
    # 'abs' calcula el valor absoluto de las correlaciones.
    corr = df.corr()[target_col].abs()
    features = corr[corr > umbral_corr].index.tolist()
    # Eliminar la variable target de la lista de features, porque su valor de correlación es 1.
    features.remove(target_col)

    # Filtrar por pvalue si es necesario
    if pvalue is not None:
        significant_features = []
        for feature in features:
            # colocamos el guión bajo '_,' para indicar que no nos interesa el primer valor
            _, p_val = stats.pearsonr(df[feature], df[target_col])
            if p_val < pvalue:
                significant_features.append(feature)
        features = significant_features

    return features


def plot_features_num_regression(df, target_col="", columns=[], umbral_corr=0, pvalue=None):
    """
    Función para analizar correlaciones numéricas y graficar pairplots.

    Params:
        df (pd.DataFrame): DataFrame de entrada.
        target_col (str): Columna objetivo para calcular correlaciones.
        columns (list[str]): Columnas a evaluar (si está vacío, selecciona numéricas). Por defecto [].
        umbral_corr (float): Umbral absoluto de correlación. Por defecto 0.
        pvalue (float): Nivel de significancia para el p-valor (opcional). Por defecto None.

    Returns:
        list[str]: Columnas seleccionadas que cumplen con los criterios.
    """

    # Validación del DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError(
            "El argumento 'df' debe ser un DataFrame de pandas válido.")

    # Validación de que 'target_col' sea obligatorio
    if not target_col:
        raise ValueError(
            "Debes proporcionar un 'target_col' válido para calcular correlaciones.")

    # Verificamos si 'target_col' es una columna válida en el dataframe
    if target_col and target_col not in df.columns:
        raise ValueError(f"La columna indicada como 'target_col': {target_col} no está en el DataFrame.")

    # Verificamos si la columna 'target_col' es numérica
    if target_col and not pd.api.types.is_numeric_dtype(df[target_col]):
        raise ValueError(f"La columna indicada como 'target_col': {target_col} no es numérica.")

    # Si 'columns' está vacío, usamos todas las columnas numéricas excepto 'target_col'
    if not columns:
        columns = df.select_dtypes(include=['number']).columns.tolist()
        if target_col in columns:
            columns.remove(target_col)

    # sino, es decir, si 'columns' no está vacío, validamos que las columnas existan y sean numéricas
    else:
        invalid_cols = [col for col in columns if col not in df.columns]
        if invalid_cols:
            raise ValueError(
                f"Las siguientes columnas no están en el DataFrame: {invalid_cols}")

        non_numeric_cols = [
            col for col in columns if not pd.api.types.is_numeric_dtype(df[col])]
        if non_numeric_cols:
            raise ValueError(f"Las siguientes columnas no son numéricas: {non_numeric_cols}")

    # Validación del umbral de correlacion 'umbral_corr'
    if not isinstance(umbral_corr, (int, float)) or not 0 <= umbral_corr <= 1:
        raise ValueError(
            "El argumento 'umbral_corr' debe ser un número entre 0 y 1.")

    # Validación del valor 'P-Value'
    if pvalue is not None:
        if not isinstance(pvalue, (int, float)) or not 0 <= pvalue <= 1:
            raise ValueError(
                "El argumento 'pvalue' debe ser un número entre 0 y 1, o 'None'.")

    # CORRELACION
    # Correlación absoluta de las columnas vs al target
    corr = np.abs(df.corr()[target_col]).sort_values(ascending=False)

    # Columnas que superan el umbral de correlacion, excluyendo a la columna 'target_col'
    selected_columns = corr[(corr > umbral_corr) & (
        corr.index != target_col)].index.tolist()

    # Si se proporciona un p-value, verificamos significancia estadística
    if pvalue is not None:
        significant_columns = []  # Lista para guardar las columnas significativas
        for col in selected_columns:
            corr, p_val = stats.pearsonr(df[col], df[target_col])
            if p_val <= pvalue:
                significant_columns.append(col)
        selected_columns = significant_columns  # Actualizamos con las significativas

    # Validación de los resultados de la correlación
    if not selected_columns:
        print("No se encontraron columnas que cumplan con los criterios de correlación y p-valor.")
        return None

    # PAIRPLOTS
    # Incluir siempre target_col en cada gráfico
    columns_to_plot = [target_col] + selected_columns

    # Dividir en grupos de máximo 5 columnas (incluyendo target_col)
    num_groups = (len(columns_to_plot) - 1) // 4 + \
        1  # Grupos de 4 columnas + target

    for i in range(num_groups):
        # Seleccionar un grupo de columnas
        subset = columns_to_plot[:1] + columns_to_plot[1 + i*4:1 + (i+1)*4]

        # Generar el pairplot
        sns.pairplot(df[subset], diag_kind="kde", corner=True)
        plt.show()

    return selected_columns


def check_normality(data):
    stat, p = stats.shapiro(data)
    return p > 0.01

def check_homoscedasticity(*groups):
    stat, p = stats.levene(*groups)
    return p > 0.01

def get_features_cat_regression(df, target_col, pvalue=0.05):
    """
    Función para obtener las características categóricas significativas en un modelo de regresión lineal.
    Params:
                df: dataframe de pandas
                target_col: columna objetivo del dataframe
                pvalue: p-valor para el test de significancia
    Returns:
                Lista con las características categóricas significativas
        """
    # Verificamos si el dataframe es válido
    if not isinstance(df, pd.DataFrame):
        print("El argumento 'df' no es un dataframe válido.")
        return None
    if not (0 <= pvalue <= 1):
        # comprueba que el valor de pvalue esté entre 0 y 1
        print("El valor de pvalue debe estar entre 0 y 1.")
        return None
    # Verificamos si 'target_col' es una columna válida en el dataframe
    if target_col not in df.columns:
        print(f"La columna '{target_col}' no está en el dataframe.")
        return None
    # Verificamos si la columna 'target_col' es numérica
    if not pd.api.types.is_numeric_dtype(df[target_col]):
        print(f"La columna '{target_col}' no es una columna numérica.")
        return None
    # Identificar las columnas categóricas del dataframe
    cat_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if not cat_columns:
        print("No se encontraron características categóricas en el dataframe.")
        return None
    # Lista para almacenar las columnas categóricas que superan el pvalor
    significant_cat_features = []
    for cat_col in cat_columns:
        # Si la columna categórica tiene más de un nivel (para que sea válida para el test)
        if df[cat_col].nunique() > 1:
            try:
                groups = [df[target_col][df[cat_col] == level].dropna() for level in df[cat_col].unique()]
                if all(len(g) >= 2 for g in groups):
                    # Comprobamos normalidad y homocedasticidad
                    all_data = np.concatenate(groups)
                    is_normal = check_normality(all_data)
                    is_homoscedastic = check_homoscedasticity(*groups)

                    if is_normal and is_homoscedastic:
                        print(f"La distribución de {target_col} es normal y homocedástica.")
                        if len(groups) == 2:
                            t_stat, p_val = stats.ttest_ind(groups[0], groups[1])
                            print(f"Student t (p_value): {p_val}")
                        else:
                            f_val, p_val = stats.f_oneway(*groups)
                            print(f"Oneway ANOVA (p_value): {p_val}")
                    else:
                        print(f"La distribución de {target_col} NO es normal o homocedástica.")
                        if len(groups) == 2:
                            u_stat, p_val = stats.mannwhitneyu(groups[0], groups[1])
                            print(f"MannWhitney U (p_value): {p_val}")
                        else:
                            h_stat, p_val = stats.kruskal(*groups)
                            print(f"Kruskal (p_value): {p_val}")

                    # Comprobamos si el p-valor es menor que el p-valor especificado
                    if p_val < pvalue:
                        significant_cat_features.append(cat_col)
            except Exception as e:
                print(f"Error al procesar la columna {cat_col}: {str(e)}")
                continue
    # Si encontramos columnas significativas, las devolvemos
    if significant_cat_features:
        return significant_cat_features
    else:
        print("\nNo se encontraron características categóricas significativas.")
        return None

def plot_features_cat_regression(df, target_col="", columns=[], pvalue=0.05, with_individual_plot=False):
    """
    Función para graficar histogramas agrupados de variables categóricas significativas.
    Params:
        df: dataframe de pandas
        target_col: columna objetivo del dataframe (variable numérica)
        columns: lista de columnas categóricas a evaluar (si está vacía, se usan todas las columnas categóricas)
        pvalue: p-valor para el test de significancia
        with_individual_plot: si es True, genera un gráfico individual por cada categoría
    Returns:
        Lista de columnas que cumplen con los criterios de significancia
    """
    # Verificamos si el dataframe es válido
    if not isinstance(df, pd.DataFrame):
        print("El argumento 'df' no es un dataframe válido.")
        return None
    if target_col and target_col not in df.columns:
        print(f"La columna '{target_col}' no está en el dataframe.")
        return None
    if not (0 <= pvalue <= 1):
        # comprueba que el valor de pvalue esté entre 0 y 1
        print("El valor de pvalue debe estar entre 0 y 1.")
        return None
    if target_col and not pd.api.types.is_numeric_dtype(df[target_col]):
        print(f"La columna '{target_col}' no es una columna numérica.")
        return None
    # Identificar las columnas categóricas del dataframe
    cat_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if not cat_columns:
        print("No se encontraron características categóricas en el dataframe.")
        return None
    # Si 'columns' está vacío, usamos todas las columnas categóricas
    if not columns:
        columns = cat_columns
    # Lista para almacenar las columnas significativas
    significant_cat_features = []
    # Verificamos la significancia de las columnas categóricas con respecto al 'target_col'
    for cat_col in columns:
        if cat_col not in cat_columns:
            print(f"La columna '{cat_col}' no es categórica o no existe en el dataframe.")
            continue
        if df[cat_col].nunique() > 1:
            try:
                groups = [df[target_col][df[cat_col] == level].dropna() for level in df[cat_col].unique()]
                if all(len(g) >= 2 for g in groups):
                    # Comprobamos normalidad y homocedasticidad
                    all_data = np.concatenate(groups)
                    is_normal = check_normality(all_data)
                    is_homoscedastic = check_homoscedasticity(*groups)

                    if is_normal and is_homoscedastic:
                        print(f"La distribución de {target_col} es normal y homocedástica.")
                        if len(groups) == 2:
                            t_stat, p_val = stats.ttest_ind(groups[0], groups[1])
                            print(f"Student t (p_value): {p_val}")
                        else:
                            f_val, p_val = stats.f_oneway(*groups)
                            print(f"Oneway ANOVA (p_value): {p_val}")
                    else:
                        print(f"La distribución de {target_col} NO es normal o homocedástica.")
                        if len(groups) == 2:
                            u_stat, p_val = stats.mannwhitneyu(groups[0], groups[1])
                            print(f"MannWhitney U (p_value): {p_val}")
                        else:
                            h_stat, p_val = stats.kruskal(*groups)
                            print(f"Kruskal (p_value): {p_val}")

                    # Comprobamos si el p-valor es menor que el p-valor especificado
                    if p_val < pvalue:
                        significant_cat_features.append(cat_col)
            except Exception as e:
                print(f"Error al procesar la columna {cat_col}: {str(e)}")
                continue
    # Si no hay columnas significativas
    if not significant_cat_features:
        print("\nNo se encontraron características categóricas significativas.")
        return None
    # Graficar histogramas agrupados para las columnas significativas
    for cat_col in significant_cat_features:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=target_col, hue=cat_col,
                     kde=True, multiple="stack", bins=30)
        plt.title(f"Distribución de {target_col} por {cat_col}")
        plt.xlabel(target_col)
        plt.ylabel("Frecuencia")
        plt.show()
        # Si 'with_individual_plot' es True, graficar histogramas individuales por cada categoría
        if with_individual_plot:
            for level in df[cat_col].unique():
                plt.figure(figsize=(10, 6))
                sns.histplot(df[df[cat_col] == level],
                             x=target_col, kde=True, bins=30)
                plt.title(f"Distribución de {target_col} para {cat_col} = {level}")
                plt.xlabel(target_col)
                plt.ylabel("Frecuencia")
                plt.show()
    return significant_cat_features

# Función para detectar outliers usando IQR
def detect_outliers(df, feature):
    feature_data = df[feature].dropna()
    Q1 = feature_data.quantile(0.25)
    Q3 = feature_data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
    return outliers