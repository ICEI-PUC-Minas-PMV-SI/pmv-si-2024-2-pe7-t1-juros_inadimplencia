import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Dados fornecidos
dados = pd.read_csv('C:/Users/Lucas Lima/Desktop/Juros/Dataset_Normal.csv')
# Criar o DataFrame
data = pd.DataFrame(dados)
data['Periodo'] = pd.to_datetime(data['Periodo'], format='%d/%m/%Y')
data['Ano'] = data['Periodo'].dt.year

# Separar as variáveis independentes (features) e a variável dependente (target)
X = data[['Ano']]
y_selic = data['Selic_Valor']
y_inflacao = data['Inflação_Acumulada']

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train_selic, y_test_selic = train_test_split(X, y_selic, test_size=0.3, random_state=42)
_, _, y_train_inflacao, y_test_inflacao = train_test_split(X, y_inflacao, test_size=0.3, random_state=42)

# Criar o modelo de Random Forest
model_selic = RandomForestRegressor(n_estimators=100, random_state=42)
model_inflacao = RandomForestRegressor(n_estimators=100, random_state=42)

# Treinar os modelos
model_selic.fit(X_train, y_train_selic)
model_inflacao.fit(X_train, y_train_inflacao)

# Fazer previsões
y_pred_selic = model_selic.predict(X_test)
y_pred_inflacao = model_inflacao.predict(X_test)

# Avaliar os modelos
mse_selic = mean_squared_error(y_test_selic, y_pred_selic)
r2_selic = r2_score(y_test_selic, y_pred_selic)
mse_inflacao = mean_squared_error(y_test_inflacao, y_pred_inflacao)
r2_inflacao = r2_score(y_test_inflacao, y_pred_inflacao)

print(f'Selic - Mean Squared Error: {mse_selic}')
print(f'Selic - R^2 Score: {r2_selic}')
print(f'Inflação - Mean Squared Error: {mse_inflacao}')
print(f'Inflação - R^2 Score: {r2_inflacao}')

# Plotar os resultados
plt.figure(figsize=(14, 7))

# Gráfico da Selic
plt.subplot(1, 2, 1)
plt.plot(data['Ano'], y_selic, label='Dados Reais - Selic', linestyle='--', color='purple', marker='s')
plt.scatter(X_test, y_pred_selic, label='Previsões - Selic', color='magenta', marker='x')
plt.xlabel('Ano')
plt.ylabel('Selic Valor')
plt.title('Random Forest - Selic Valor vs. Ano')
plt.legend()
plt.grid(True, linestyle=':')

# Gráfico da Inflação
plt.subplot(1, 2, 2)
plt.plot(data['Ano'], y_inflacao, label='Dados Reais - Inflação', linestyle='--', color='brown', marker='^')
plt.scatter(X_test, y_pred_inflacao, label='Previsões - Inflação', color='darkorange', marker='x')
plt.xlabel('Ano')
plt.ylabel('Inflação_Acumulada')
plt.title('Random Forest - Inflação_Acumulada vs. Ano')
plt.legend()
plt.grid(True, linestyle=':')

plt.tight_layout()
plt.show()
