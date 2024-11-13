import pandas as pd 

tabela = pd.read_excel ("JurosInadimplencia.xlsx")

display (tabela)

# Importa as bibliotecas necessárias
import pandas as pd
from prophet import Prophet

# Carrega os dados do arquivo Excel
tabela = pd.read_excel("JurosInadimplencia.xlsx")

# Exibe as primeiras linhas para verificação
display(tabela)

# Inicializa o modelo Prophet
model = Prophet()

# Ajusta o modelo aos dados
model.fit(tabela)

# Cria um dataframe para prever os próximos 12 meses
future = model.make_future_dataframe(periods=12, freq='MS')

# Realiza a previsão
forecast = model.predict(future)

# Exibe as previsões
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

import matplotlib.pyplot as plt

# Plota as previsões
fig = model.plot(forecast)

# Adiciona legendas manualmente
plt.xlabel("Data")
plt.ylabel("Previsão (y)")
plt.title("Previsão usando o Prophet")
plt.legend(["Previsão", "Intervalo de Confiança"], loc="upper left")
plt.show()

# Plota os componentes sazonais
fig2 = model.plot_components(forecast)

# Ajusta o gráfico, caso deseje
plt.suptitle("Componentes Sazonais da Previsão", y=1.02)  # Define o título geral para os subplots
plt.show()