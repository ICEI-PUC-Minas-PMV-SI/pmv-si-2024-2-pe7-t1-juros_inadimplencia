#Montar Google Drive
from google.colab import drive

drive.mount('/content/drive')

#Importar pandas e ler dataset
import pandas as pd

dados = pd.read_csv('/content/drive/My Drive/dataset/dataset_divida_fam1.csv', encoding="utf-8", sep = ';')
dados.head()

data = pd.DataFrame(dados)
data['Periodo'] = pd.to_datetime(data['Periodo'], format='%d/%m/%Y')
data['Ano'] = data['Periodo'].dt.year

#separar os dados das variáveis, dependente e independente
x = dados[['Inflacao_Acumulada']] #variável dependente (Inflação Acumulada)
y = dados[['Endividamento_SFN']] #variável independente (Endividamento)

#Dividir dados para treinamento e teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste, data_treino, data_teste = train_test_split(x, y, data, test_size = 0.2, random_state = 42)

x_teste.shape

x_treino.shape

y_teste.shape

y_treino.shape

data_teste.shape

data_treino.shape

#Criar o modelo de Regressão LInear Simples e Treinar o modelo
from sklearn import linear_model
modelo = linear_model.LinearRegression()
modelo.fit(x_treino, y_treino)

y_pred = modelo.predict(x_teste)

#Métricas do modelo
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
print(mean_absolute_error(y_teste, y_pred))
print(mean_squared_error(y_teste, y_pred))
print(r2_score(y_teste, y_pred))

# Coeficiente (inclinação da reta)
coeficiente = modelo.coef_[0]
print(coeficiente)

# Visualizar a base de dados
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Dados Reais ', color='green', marker='o')
plt.plot(x_teste, y_pred, label='Predição - Endividamento', color='blue')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel("Inflação Acumulada")
plt.ylabel("Endividamento SFN")
plt.legend()
plt.title("Regressão Linear - Endividamento SFN X Inflação Acumulada")

plt.show()