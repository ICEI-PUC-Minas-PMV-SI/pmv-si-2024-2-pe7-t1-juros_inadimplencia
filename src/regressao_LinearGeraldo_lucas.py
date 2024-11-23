import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Carregar os dados
dados = pd.read_csv('dataset_normal_final.csv')

# Criar o DataFrame
data = pd.DataFrame(dados)
data['Periodo'] = pd.to_datetime(data['Periodo'], format='%d/%m/%Y')
data['Ano'] = data['Periodo'].dt.year

# Separar as variáveis independentes (features) e a variável dependente (target)
X = data[['Ano']]
y_Endividamento_Total = data['Endividamento_Total']
y_Confiança_Valor = data['Confiança_Valor']

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train_Endividamento_Total, y_test_Endividamento_Total = train_test_split(
    X, y_Endividamento_Total, test_size=0.3, random_state=42
)
_, _, y_train_Confiança_Valor, y_test_Confiança_Valor = train_test_split(
    X, y_Confiança_Valor, test_size=0.3, random_state=42
)

# Criar o modelo de regressão linear
model_Endividamento_Total = LinearRegression()
model_Confiança_Valor = LinearRegression()

# Treinar os modelos
model_Endividamento_Total.fit(X_train, y_train_Endividamento_Total)
model_Confiança_Valor.fit(X_train, y_train_Confiança_Valor)

# Fazer previsões
y_pred_Endividamento_Total = model_Endividamento_Total.predict(X_test)
y_pred_Confiança_Valor = model_Confiança_Valor.predict(X_test)

# Avaliar os modelos
mse_endividamento_total = mean_squared_error(y_test_Endividamento_Total, y_pred_Endividamento_Total)
r2_endividamento_total = r2_score(y_test_Endividamento_Total, y_pred_Endividamento_Total)
mse_confiança_valor = mean_squared_error(y_test_Confiança_Valor, y_pred_Confiança_Valor)
r2_confiança_valor = r2_score(y_test_Confiança_Valor, y_pred_Confiança_Valor)

print(f'Endividamento_Total - Mean Squared Error: {mse_endividamento_total}')
print(f'Endividamento_Total - R^2 Score: {r2_endividamento_total}')
print(f'Confiança_Valor - Mean Squared Error: {mse_confiança_valor}')
print(f'Confiança_Valor - R^2 Score: {r2_confiança_valor}')

# Plotar os resultados
plt.figure(figsize=(14, 7))

# Gráfico do Endividamento Total
plt.subplot(1, 2, 1)
plt.plot(data['Ano'], y_Endividamento_Total, label='Dados Reais - Endividamento_Total', color='blue', marker='o')
plt.scatter(X_test, y_pred_Endividamento_Total, label='Previsões - Endividamento_Total', color='red')
plt.xlabel('Ano')
plt.ylabel('Endividamento_Total')
plt.title('Regressão Linear - Endividamento_Total vs. Ano')
plt.legend()
plt.grid(True)

# Gráfico da Confiança_Valor
plt.subplot(1, 2, 2)
plt.plot(data['Ano'], y_Confiança_Valor, label='Dados Reais - Confiança_Valor', color='green', marker='o')
plt.scatter(X_test, y_pred_Confiança_Valor, label='Previsões - Confiança_Valor', color='orange')
plt.xlabel('Ano')
plt.ylabel('Confiança_Valor')
plt.title('Regressão Linear - Confiança_Valor vs. Ano')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
