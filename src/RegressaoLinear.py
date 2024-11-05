import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# dados
data = pd.read_csv('C:/Users/Lucas Lima/Desktop/Juros/JurosInadimplenciaParametrizado1.csv')


# Ordenar por 'Periodo'
data = data.sort_values(by='Periodo')

# Definir variáveis de entrada e saída
X = data[['Confiança_Valor', 'Selic_Valor', 'Inflação_Mensal']]
y = data['Endividamento_Total']
period = data['Periodo']

# Separar dados de treino e teste
X_train, X_test, y_train, y_test, period_train, period_test = train_test_split(
    X, y, period, test_size=0.3, random_state=42
)

# Treinar o modelo de Regressão Linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Plotar previsões e valores reais
plt.figure(figsize=(10, 6))
plt.plot(period_test, y_test, 'o', color='blue', label='Valores Reais')
plt.plot(period_test, y_pred, 'o', color='red', label='Previsões')
plt.xlabel("Período de Tempo")
plt.ylabel("Endividamento Total")
plt.title("Regressão Linear - Previsão vs Real")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()