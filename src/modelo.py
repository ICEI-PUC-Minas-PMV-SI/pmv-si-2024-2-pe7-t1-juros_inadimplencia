import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Função para treinar os modelos
def treinar_modelos():
    # Carregar os dados
    dados = pd.read_csv('C:/Users/LucasLima/Desktop/Regressao/DataSet_Normal.csv')

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

    # Criar o modelo de regressão linear
    model_selic = LinearRegression()
    model_inflacao = LinearRegression()

    # Treinar os modelos
    model_selic.fit(X_train, y_train_selic)
    model_inflacao.fit(X_train, y_train_inflacao)

    # Fazer previsões para avaliação
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

    # Salvar os modelos treinados
    joblib.dump(model_selic, 'model_selic.pkl')
    joblib.dump(model_inflacao, 'model_inflacao.pkl')
    print("Modelos salvos com sucesso!")

# Função para carregar os modelos e fazer previsões
def calcular(ano):
    try:
        # Carregar os modelos
        model_selic = joblib.load('model_selic.pkl')
        model_inflacao = joblib.load('model_inflacao.pkl')

        # Previsão para o ano fornecido
        entrada = [[ano]]
        previsao_selic = model_selic.predict(entrada)[0]
        previsao_inflacao = model_inflacao.predict(entrada)[0]

        return {
            'selic': previsao_selic,
            'inflacao': previsao_inflacao
        }
    except Exception as e:
        print(f"Erro ao calcular: {str(e)}")
        return None

# Treinar os modelos ao executar este arquivo
if __name__ == '__main__':
    treinar_modelos()
