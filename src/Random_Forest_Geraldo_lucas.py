import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Carregar os dados
dados = pd.read_csv('dataset_normal_final.csv')
data = pd.DataFrame(dados)

# Processar a coluna de datas e criar uma coluna com o ano
data['Periodo'] = pd.to_datetime(data['Periodo'], format='%d/%m/%Y')
data['Ano'] = data['Periodo'].dt.year

# Separar as variáveis independentes (features) e as variáveis dependentes (targets)
X = data[['Ano']]
y_Endividamento_Total = data['Endividamento_Total']
y_Confiança_Valor = data['Confiança_Valor']

# Dividir os dados em conjuntos de treino e teste (uma única divisão)
X_train, X_test, y_train_Endividamento_Total, y_test_Endividamento_Total, y_train_Confiança_Valor, y_test_Confiança_Valor = train_test_split(
    X, y_Endividamento_Total, y_Confiança_Valor, test_size=0.3, random_state=42
)

# Criar os modelos de Random Forest
model_Endividamento_Total = RandomForestRegressor(n_estimators=100, random_state=42)
model_Confiança_Valor = RandomForestRegressor(n_estimators=100, random_state=42)

# Treinar os modelos
model_Endividamento_Total.fit(X_train, y_train_Endividamento_Total)
model_Confiança_Valor.fit(X_train, y_train_Confiança_Valor)

# Fazer previsões
y_pred_Endividamento_Total = model_Endividamento_Total.predict(X_test)
y_pred_Confiança_Valor = model_Confiança_Valor.predict(X_test)

# Avaliar os modelos
mse_Endividamento_Total = mean_squared_error(y_test_Endividamento_Total, y_pred_Endividamento_Total)
r2_Endividamento_Total = r2_score(y_test_Endividamento_Total, y_pred_Endividamento_Total)

mse_Confiança_Valor = mean_squared_error(y_test_Confiança_Valor, y_pred_Confiança_Valor)
r2_Confiança_Valor = r2_score(y_test_Confiança_Valor, y_pred_Confiança_Valor)

print(f'Endividamento_Total - Mean Squared Error: {mse_Endividamento_Total}')
print(f'Endividamento_Total - R^2 Score: {r2_Endividamento_Total}')
print(f'Confiança_Valor - Mean Squared Error: {mse_Confiança_Valor}')
print(f'Confiança_Valor - R^2 Score: {r2_Confiança_Valor}')

# Plotar os resultados
plt.figure(figsize=(14, 7))

# Gráfico do Endividamento_Total
plt.subplot(1, 2, 1)
plt.scatter(X_test, y_test_Endividamento_Total, label='Dados Reais - Endividamento_Total', color='purple', marker='s')
plt.scatter(X_test, y_pred_Endividamento_Total, label='Previsões - Endividamento_Total', color='magenta', marker='x')
plt.xlabel('Ano')
plt.ylabel('Endividamento_Total')
plt.title('Random Forest - Endividamento_Total vs. Ano')
plt.legend()
plt.grid(True, linestyle=':')

# Gráfico da Confiança_Valor
plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test_Confiança_Valor, label='Dados Reais - Confiança_Valor', color='brown', marker='^')
plt.scatter(X_test, y_pred_Confiança_Valor, label='Previsões - Confiança_Valor', color='darkorange', marker='x')
plt.xlabel('Ano')
plt.ylabel('Confiança_Valor')
plt.title('Random Forest - Confiança_Valor vs. Ano')
plt.legend()
plt.grid(True, linestyle=':')

plt.tight_layout()
plt.show()
