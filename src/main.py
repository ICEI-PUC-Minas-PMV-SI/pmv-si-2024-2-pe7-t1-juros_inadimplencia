from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sklearn.metrics import mean_squared_error, r2_score

app = Flask(__name__)

# Carregar e preparar o dataset
dataset_path = "Dataset_Normal.csv"
data = pd.read_csv(dataset_path)

# Preparo da série temporal
data["Periodo"] = pd.to_datetime(data["Periodo"], format="%m/%d/%Y")
data.set_index("Periodo", inplace=True)
endividamento_series = data["Endividamento_Total"]

# Treinar o modelo SARIMA
def train_sarima(series):
    # Configurar os parâmetros do SARIMA (valores iniciais podem ser ajustados com grid search)
    p, d, q = 1, 1, 1  # Componentes ARIMA
    P, D, Q, s = 1, 1, 1, 12  # Componentes sazonais (s = 12 para sazonalidade anual)

    # Treinamento
    model = SARIMAX(series, order=(p, d, q), seasonal_order=(P, D, Q, s), enforce_stationarity=False, enforce_invertibility=False)
    sarima_model = model.fit(disp=False)
    return sarima_model

sarima_model = train_sarima(endividamento_series)

# Função para gerar previsões, gráficos, e métricas
def generate_sarima_prediction(model, periods):
    forecast = model.get_forecast(steps=periods)
    forecast_index = pd.date_range(end=endividamento_series.index[-1], periods=periods + 1, freq="M")[1:]
    forecast_values = forecast.predicted_mean
    confidence_intervals = forecast.conf_int()

    # Calcular métricas (R² e MSE)
    if len(endividamento_series) >= periods:
        real_values = endividamento_series[-periods:]
        mse = mean_squared_error(real_values, forecast_values[:len(real_values)])
        r2 = r2_score(real_values, forecast_values[:len(real_values)])
    else:
        mse = None
        r2 = None

    # Gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(endividamento_series, label="Dados Históricos")
    plt.plot(forecast_index, forecast_values, label="Previsão SARIMA")
    plt.fill_between(
        forecast_index,
        confidence_intervals.iloc[:, 0],
        confidence_intervals.iloc[:, 1],
        color="gray",
        alpha=0.2,
        label="Intervalo de Confiança"
    )
    plt.legend()
    plt.title("Previsão do Endividamento Total com SARIMA")
    plt.xlabel("Período")
    plt.ylabel("Endividamento (%)")
    plt.grid()

    # Salvar gráfico como string base64
    img = BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return forecast_values.tolist(), graph_url, r2, mse

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    periodo = int(data["periodo"])

    # Gerar previsões com SARIMA
    forecast_values, graph_url, r2, mse = generate_sarima_prediction(sarima_model, periodo)

    # Retornar os resultados
    return jsonify({
        "grafico_sarima": f"data:image/png;base64,{graph_url}",
        "previsoes": forecast_values,
        "r2": r2 if r2 is not None else "N/A",
        "mse": mse if mse is not None else "N/A"
    })

if __name__ == "__main__":
    app.run(debug=True)
