import pandas as pd 

tabela = pd.read_excel ("JurosInadimplencia.xlsx")

display (tabela)

# Importa as bibliotecas necessárias
from sklearn.metrics import mean_absolute_error
import pandas as pd
from prophet import Prophet

# Carrega os dados do arquivo Excel
tabela = pd.read_excel("JurosInadimplencia.xlsx")

# Exibe as primeiras linhas para verificação
display(tabela)

# Renomeia as colunas principais para o formato esperado pelo Prophet
tabela.rename(columns={"data": "ds", "y": "y"}, inplace=True)


# Divida os dados para treino e teste (exemplo de 80% treino e 20% teste)
train_size = int(0.6 * len(tabela))
train, test = tabela[:train_size], tabela[train_size:]

# Inicializa o modelo Prophet
model = Prophet()



# Ajusta o modelo aos dados
model.fit(tabela)

# Cria um dataframe para prever os próximos 60 meses
future = model.make_future_dataframe(periods=60, freq='MS')



# Realiza a previsão
forecast = model.predict(future)

# Exibe as previsões
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
import matplotlib.pyplot as plt

# Configura o gráfico
plt.figure(figsize=(12, 6))

# Plota os valores reais
plt.plot(tabela['ds'], tabela['y'], label='Dados Reais', color='blue', marker='o')

# Plota as previsões
plt.plot(forecast['ds'], forecast['yhat'], label='Previsão', color='orange')

# Plota os intervalos de confiança
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], 
                 color='orange', alpha=0.3, label='Intervalo de Confiança')

# Adiciona títulos e legendas
plt.title('Previsão de Séries Temporais com Prophet')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.legend(loc='upper left')  # Posiciona a legenda
plt.grid(True)
plt.tight_layout()

# Exibe o gráfico
plt.show()
# Plota os componentes sazonais
fig2 = model.plot_components(forecast)

# Ajusta o gráfico, caso deseje
plt.suptitle("Componentes Sazonais da Previsão", y=1.02)  # Define o título geral para os subplots
plt.show()
from sklearn.metrics import mean_squared_error, r2_score

# Previsões para o conjunto de teste
forecast_test = model.predict(test)
y_true = test['y']
y_pred = forecast_test['yhat']

# Calculando MSE e R²
mse = mean_squared_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

print("MSE:", mse)
print("R²:", r2)
