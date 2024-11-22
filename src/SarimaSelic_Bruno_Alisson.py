import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Carregar os dados para análise
dados = pd.read_csv('C:\Modelo\dataset_normal_final.csv')

# Definir data como índice
dados['Periodo'] = pd.to_datetime(dados['Periodo'], format='%m/%d/%Y')
dados = dados.set_index('Periodo')

# Definir frequência explícita
dados = dados.asfreq('MS')

# Visualizar os primeiros registros do dataset
dados.head(5)

# Removendo colunas para facilitar o entendimento do modelo
dados_selic = dados.drop(['Confianca_Valor', 'Endividamento_Total', 'Inflacao_Acumulada'],axis=1)

dados_selic.head(5)

# Visualização gráfica da série temporal
dados_selic.plot()
plt.xticks(rotation=45)
plt.xlabel('Periodo')
plt.ylabel('Selic_Valor')
plt.tight_layout()

# Definição do treinamento e testes do modelo
dados_treino = dados_selic[dados_selic.index < '2019-06-01']
dados_teste = dados_selic[dados_selic.index >= '2019-06-01']

# Verificar estacionariedade (resultado precisa ser menor que 0.05)
result = adfuller(dados_selic)
print("p-valor:", result[1])

# Ajuste do modelo - Parâmetros a serem alterados para trazer mais confiabilidade ao modelo
#   order = (p, d, q) e seasonal_order = (P, D, Q, s)
#    p = 1: Captura um efeito de dependência autorregressiva básica
#    d = 1: Para tornar a série estacionária, caso necessário
#    q = 1: Permite capturar flutuações curtas com média móvel
#    s = 12: Mantido como padrão, caso sazonalidade residual seja detectada
#    P = 0, D = 0, Q = 0: Sem padrão sazonal esperado

modelo = SARIMAX(dados_treino, order=(0,1,6), seasonal_order=(0,1,10,12)) 
resultado = modelo.fit()

# Impressão dos coeficientes
print('Coefficients: %s' % resultado.params)

# Predições do modelo
predicao_teste = resultado.predict(start=dados_teste.index[0], end=dados_teste.index[-1])

# Previsão para o modelo
passos_futuros = 36 # Variável recebe a quantidade de meses que faremos a previsão dos indicadores futuros
previsao = resultado.get_forecast(steps=passos_futuros)

# Obter o intervalo de confiança para as previsões
intervalo_confianca = previsao.conf_int()

# Obter a série original e as previsões
index_futuro = pd.date_range(dados_teste.index[-1] + pd.DateOffset(1), periods=passos_futuros, freq='M')
serie_previsao = previsao.predicted_mean
serie_previsao.index = index_futuro

print(type(dados_treino))
print(dados_treino.index)

# Alinhar índices do intervalo de confiança
intervalo_confianca.index = serie_previsao.index

# Gráfico 1: Série histórica com previsões para o período de teste
plt.figure(figsize=(12, 6))
plt.plot(dados_treino.index, dados_treino, label="Treinamento", color="blue")
plt.plot(dados_teste.index, dados_teste, label="Teste", color="green")
plt.plot(predicao_teste.index, predicao_teste, label="Previsão (Teste)", color="red", linestyle="--")
plt.title("Série Temporal - Selic (Treinamento e Teste)")
plt.legend()
plt.xlabel("Período")
plt.ylabel("Selic")
plt.grid()
plt.show()

# Gráfico 2: Previsão de n períodos com intervalo de confiança
plt.figure(figsize=(12, 6))
plt.plot(dados_selic['Selic_Valor'], label="Histórico", color="blue")
plt.plot(serie_previsao, label="Previsão (36 meses)", color="red")
plt.fill_between(
    serie_previsao.index,
    intervalo_confianca.iloc[:, 0],
    intervalo_confianca.iloc[:, 1],
    color='pink', alpha=0.3, label="Intervalo de Confiança"
)

plt.title("Previsão da Selic - Próximos 36 Meses")
plt.legend()
plt.xlabel("Período")
plt.ylabel("Selic")
plt.grid()
plt.show()

# Combinar previsões e intervalo de confiança em um DataFrame
df_previsoes = pd.DataFrame({
    'Previsão': serie_previsao,
    'Limite Inferior': intervalo_confianca.iloc[:, 0],
    'Limite Superior': intervalo_confianca.iloc[:, 1]
})

# Exportar para CSV
df_previsoes.to_csv('previsoes_sarima.csv', index=True)

from sklearn.metrics import mean_squared_error

# Calcular erros
MSE = mean_squared_error(dados_teste,predicao_teste)

RMSE = np.sqrt(MSE)
print("RMSE = {:0.2f}".format(RMSE))

from sklearn.metrics import mean_squared_error, r2_score

mse_inflacao = mean_squared_error(dados_teste, predicao_teste)
r2_inflacao = r2_score(dados_teste, predicao_teste)

print(mse_inflacao)
print(r2_inflacao)
