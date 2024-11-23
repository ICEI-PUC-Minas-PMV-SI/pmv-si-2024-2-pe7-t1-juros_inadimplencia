# Preparação dos dados

Na etapa de preparação de dados, começamos constatando que as bases selecionadas não apresentavam dados faltantes nem a necessidade de remoção de outliers. Prosseguindo com a transformação de Dados, foi verificado a escala das variáveis, especialmente para a Regressão Linear, pois os algoritmos de aprendizado se beneficiam de dados em uma mesma escala. Decidimos manter as variáveis na escala original devido ao uso de Random Forest, tendo em vista que este modelo não é sensível a escalas, e também para permitir uma interpretação direta dos coeficientes na Regressão Linear. A coluna Período, que representa o tempo, foi convertida para o tipo datetime para garantir a manipulação e ordenação corretas dos dados, uma vez que ela representa uma variável fundamental para o modelo.

No Manuseio de Dados Temporais, foi essencial ordenar a coluna Período em ordem  crescente para manter a sequência temporal em visualização, possbilitando uma análise consistente ao longo do tempo. Essa ordenação permite observar melhor as tendências e relações ao longo do período trabalhado. Quanto à Separação de Dados, dividimos os dados em conjuntos de treino e teste usando uma proporção de 70/30 para uma avaliação confiável do modelo. O conjunto de treino foi utilizado para ajustar os modelos, enquanto o conjunto de teste ajudou a avaliar a performance dos mesmos em dados não vistos. Essas etapas de preparação de dados foram fundamentais para garantir que os modelos tivessem uma base confiável e representativa dos dados reais, aumentando a precisão e a generalização dos modelos de predição. Na preparação dos dados buscamos assegurar que o aprendizado dos algoritmos capturasse padrões importantes, maximizando o desempenho e a validade das previsões feitas para o endividamento das famílias.

![IMG 1](https://github.com/user-attachments/assets/cf9f418b-ec28-4473-a875-01738e19df1a)

Base utilizada para Regressão Linear, Random Forest e Prophet.(Arquivo presente na pasta SRC)

# Descrição dos modelos

Os modelos de predição baseados em algoritmos de aprendizado de máquina escolhidos foram: Regressão Linear, Random Forest e análise de séries temporais (Prophet). 
Os algoritmos foram selecionados devido às suas características distintas e aos benefícios que ofereciam para entender e prever o comportamento dos dados em relação ao endividamento das famílias.

Em cada modelo, foram testados diferentes configurações de parâmetros. Na Regressão Linear decidimos utilizar uma abordagem direta, sem regularização adicional. 
No caso do Random Forest, experimentamos valores crescentes de n_estimators e diferentes profundidades máximas para garantir um equilíbrio entre precisão e performance. Já no Prophet, optamos por adicionar diferentes regressores (que se tratam de diversos índices macroeconômicos) para estimarmos a variação do endividamento das famílias no decorrer do tempo. Essas escolhas se justificam pela observação dos erros e pela variabilidade dos dados.

# Experimento #1

## Regressão Linear Simples
A análise realizada utilizou regressão linear simples para explorar a relação entre o percentual de endividamento das famílias baseado no Sistema Financeiro Nacional (SFN) e as variáveis "Selic_Valor", "Confiança_Valor" e "Inflacao_Acumulada". O objetivo era investigar como a variação da taxa Selic influencia o endividamento, considerando também o impacto da inflação e do índice de confiança do consumidor.

Para construir os modelos, foi utilizada a biblioteca `sklearn` para dividir os dados em conjuntos de treino e teste e ajustar um modelo linear. O trecho do código abaixo exemplifica o processo:

```python
#separar os dados das variáveis, dependente e independente
x = dados[['Selic_Valor']] #variável dependente (Selic)
y = dados[['Endividamento_SFN']] #variável independente (Endividamento)

#dividir dados para treinamento e teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste, data_treino, data_teste = train_test_split(x, y, data, test_size = 0.2, random_state = 42)

#criar o modelo de Regressão LInear Simples e Treinar o modelo
from sklearn import linear_model
modelo = linear_model.LinearRegression()
modelo.fit(x_treino, y_treino)

#métricas do Modelo
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
print(mean_absolute_error(y_teste, y_pred))
print(mean_squared_error(y_teste, y_pred))
print(r2_score(y_teste, y_pred))

#coeficiente (inclinação da reta)
coeficiente = modelo.coef_[0]
print(coeficiente)
```
### Endividamento vs Selic

```
Mean Absolute Error 2.513171289925124
Mean Squared Error: 8.717099884190315
R2-Score: -0.049468720426556034
Coeficiente: [0.12235752]
```

Os resultados para a variável "Selic_Valor" mostraram que o coeficiente da regressão foi 0,1224, indicando que, em média, um aumento de 1 ponto percentual na taxa Selic está associado a um aumento de 0,1224% no endividamento SFN. No entanto, o valor de R² foi -0,049, sugerindo que a Selic, sozinha, não explica a variação no endividamento.

> [!NOTE]
> Para ver o código deste modelo clique no link 👉 [endividamento_selic.py](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/src/endividamento_selic_alisson_bruno.py).

<div align="center">
  
![Endividamento vs Selic - Regressão Linear Simples](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/docs/img/endividamento_selic.png)

</div>

### Endividamento vs Índice de Confiança do COnsumidor
```
Mean Absolute Error 1.9215478332539357
Mean Squared Error: 7.593682007823295
R2-Score: 0.08578175701187307
Coeficiente: [0.05027029]
```
Para "Confiança_Valor", o coeficiente foi 0,0503, indicando que um aumento de 1 ponto no índice de confiança está associado a um aumento médio de 0,0503% no endividamento SFN. O R² foi 0,086, mostrando uma explicação um pouco melhor que a Selic, mas ainda muito limitada.

> [!NOTE]
> Para ver o código deste modelo clique no link 👉 [endividamento_confianca.py](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/src/endividamento_confianca_alisson_bruno.py).

<div align="center">

![Endividamento vs ICC - Regressão Linear Simples](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/docs/img/endividamento_confianca.png)

</div>

### Endividamento vs Inflação Acumulada
```
Mean Absolute Error 2.475296029909461
Mean Squared Error: 9.044113375438034
R2-Score: -0.0888385148285209
Coeficiente: [0.36940184]
```
Por último, "Inflacao_Acumulada" apresentou um coeficiente de 0,3694, sugerindo que cada aumento de 1% na inflação acumulada está associado a um aumento médio de 0,3694% no endividamento SFN. No entanto, o valor de R² foi -0,088, reforçando que a inflação, sozinha, também não é um bom preditor do endividamento.

> [!NOTE]
> Para ver o código deste modelo clique no link 👉 [endividamento_inflacao.py](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/src/endividamento_selic_alisson_bruno.py).

<div align="center">

![Endividamento vs Inflação - Regressão Linear Simples](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/docs/img/endividamento_inflacao.png)

</div>


### Conclusão do experimento
Em síntese, os modelos indicam que as variáveis analisadas possuem relações positivas, porém muito fracas, com o nível de endividamento conforme medido pelo SFN. Valores baixos ou negativos de R² indicam que as variáveis isoladamente não explicam bem o comportamento do endividamento. Isso sugere que outros fatores, como renda familiar, disponibilidade de crédito e condições macroeconômicas, devem ser considerados.

Portanto, embora a análise mostre uma influência limitada da Selic no endividamento, a resposta à questão da pesquisa requer um modelo mais robusto que inclua múltiplas variáveis simultaneamente. Isso permitirá entender melhor a relação entre a taxa Selic, a inflação e o endividamento das famílias.

# Experimento #2

# Regressão Linear

A regressão linear é um método estatístico usado para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. O objetivo é ajustar uma linha reta que minimiza a soma dos quadrados das diferenças entre os valores observados e os valores previstos. Também foi observado que ele possui apenas o parâmetro de coeficiente de inclinação da linha.

![image](https://github.com/user-attachments/assets/d762a977-3d38-40d7-be28-f27a600876ad)
![image](https://github.com/user-attachments/assets/3af2fc80-efa0-440e-820a-d0238bb04457)

A Regressão Linear foi escolhida devido à sua capacidade de fornecer uma linha de base para comparação com outros modelos mais complexos. 
Ela ajuda a identificar se uma simples relação linear é suficiente para explicar os dados. Neste primeiro teste, optamos por uma Regressão Linear simples como
ponto de partida.

![RegressaoLinear](https://github.com/user-attachments/assets/57316d07-b0ec-479f-b299-f45c6494c935)

> [!NOTE]
> Para ver o código deste modelo clique no link 👉 [Regressao_Linear_LucasLima_Geraldo .py](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/src/Regressao_Linear_LucasLima_Geraldo%20.py).



# Random Forest

O Random Forest é um algoritmo de aprendizado de máquina baseado em conjuntos que constrói múltiplas árvores de decisão durante o treinamento e apresenta a média das previsões individuais das árvores para melhorar a precisão. Uma das vantagens é sua robustez em relação a outliers e sua capacidade de lidar bem com grandes conjuntos de dados por outro lado, pode ser complicado ter poder computacional suficiente para processar os dados e sua interpretação pode ser mais complicada.
Com os parâmetros livres alteramos os:

![image](https://github.com/user-attachments/assets/d01f3556-fe05-4b41-86d1-c23e914963ec)

n_estimators. Que é o número de árvores na floresta.

max_depth. que é a profundidade máxima de cada árvore.

min_samples_split que é o número mínimo de amostras necessárias para dividir um nó interno.

![image](https://github.com/user-attachments/assets/556c1605-8574-4416-8ab9-a434e6afef35)


A escolha do Random Forest como um modelo foi para analisar relações não-lineares entre as variáveis independentes, além de experimentarmos diferentes valores para n_estimators e max_depth para encontrar o melhor ajuste, buscando tentar prever o nível de endividamento.

![RandomForest](https://github.com/user-attachments/assets/fce3e796-4927-409c-b3c0-b939d73017cf)

> [!NOTE]
> Para ver o código deste modelo clique no link 👉 [Random_Forest_LucasLima_Geraldo.py](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/src/Random_Forest_LucasLima_Geraldo.py).

## Avaliação dos modelos criados

A decisão em compilar os itens solicitados na parte da avaliação dos modelos foram: Começando pelas métricas onde foi usado a Mean Squared Error a MSE. Ela mede a média dos quadrados dos erros, que são as diferenças entre os valores previstos e os valores observados. Foi decidido a escolha do MSE, pois é uma métrica comum para problemas de regressão e é fácil de interpretar e também do R^2 Score. Ele representa a proporção da variância da variável dependente que é explicada pelas variáveis independentes no modelo. O R^2 também foi escolhido pois ele fornece uma medida de quão bem os valores previstos se ajustam aos dados reais.

Sobre os resultados obtidos: a Regressão Linear forneceu uma linha de base simples, mas completa para a análise dos dados. A MSE foi de de 13.91 indica que a média dos erros ao quadrado das previsões do modelo foi relativamente alta, mostrando que as previsões não estavam muito próximas dos valores reais. Além disso, o R^2 Score negativo de -0.06 nos diz que o modelo não foi capaz de capturar a variação nos dados de forma eficaz, o que significa que as previsões feitas pela regressão linear são menos confiáveis. Isto pode ser atribuído à simplicidade do modelo, que assume uma relação linear entre as variáveis, não capturando as complexidades e não linearidades presentes nos dados .

![image](https://github.com/user-attachments/assets/4f55d4fe-1134-407f-b425-fa1418bbaed4)


Na comparação entre os modelos de Random Forest e Regressão Linear, conclui-se que o primeiro apresentou MSE de 7.07, menor do que a da Regressão Linear, ou seja, o modelo de Random Forest fez previsões mais próximas dos valores reais. No entanto, o R^2 Score de -0.22 sugere que a Regressão Linear tenha sido mais eficiente em explicar as variações dos dados. 

![image](https://github.com/user-attachments/assets/369cb0c0-dca6-4a96-9765-ad3327742d1f)


Os dois modelos mostram a necessidade de uma análise mais profunda e de integração de métodos adicionais para demonstrar com mais clareza a variação do nível de endividamento familiar. A Regressão Linear, apesar de ser uma boa linha de base, não é suficiente para este conjunto de dados, enquanto o Random Forest, mesmo sendo mais eficaz, ainda precisa ser ajustado para um desempenho superior. Apesar das análises e interpretações não retornarem o resultado desejado, o conjunto de descobertas foi essencial para entendermos as limitações dos modelos e dados utilizados, apontando para futuras melhorias e ajustes e visando previsões mais precisas e confiáveis.

# Experimento #3

# Prophet

A análise de séries temporais é um método de estudar como uma variável muda ao longo do tempo, ajudando a identificar padrões, tendências, ciclos, sazonalidade e outliers em seus dados. Esse método também é utilizado para prever valores futuros de sua variável com base em dados históricos. 

Essa técnica se diferencia da análise de regressão em três pontos: 1) enquanto as séries temporais se concentram em como uma única variável muda ao longo do tempo, a regressão se concentra em como múltiplas variáveis interagem entre si; 2) análise de séries temporais presume que os dados são dependentes no tempo e têm autocorrelação, enquanto a análise de regressão assume que os dados são independentes e não têm multicolinearidade; 3) por fim, enquanto, os dados de séries temporais são organizados em ordem cronológica, os dados de regressão não são necessariamente ordenados. (SAMMARRAIE, 2024).

O Prophet é um algoritmo desenvolvido pelo Facebook que trabalha com previsão de séries temporais. É baseado em um modelo aditivo em que tendências não-lineares são ajustadas com sazonalidade mensal, diária e anual, além dos efeitos dos feriados. (FACEBOOK, 2023). 

Visando um maior entendimento do funcionamento do algoritmo do Prophet, optamos por gerar dois modelos: um em que o Prophet utiliziaria apenas a variação do nível de endividamento no período entre março de 2011 e maio de 2024 para gerar a previsão desse índice até 2030; e outro em que são adicionados os regressores (variação do juros medidos pela Selic, o nível de confiança e a inflação mensal medida pelo IPCA) como variáveis externas que influenciam no comportamento do nível de endividamento.

Como se vê abaixo, os resultados gerados foram discrepantes na previsão até o ano de 2030: enquanto o modelo em que o Prophet usa apenas a variação do endividamento para previsão conclui que o nível de endividamento vai seguir uma tendência de crescimento até chegar a 54% da população em 2030, o modelo que utiliza os regressores estima que o nível de endividamento chegou a uma máxima em 2021 e deve seguir em queda até chegar em 42,5% no final do período. Além dos resultados do nível de endividamento entre 2011 e 2030, através da plotagem de gráfico é possível estimar as oscilações mais frequentes em um determinado período (no caso do gráfico, na análise anual), e representar como um evento atípico impactou na variabilidade dos dados.

Modelo de Séries Temporais Prophet com Regressores
![image](https://github.com/user-attachments/assets/cefcd216-3414-4fa8-8943-1869c816d593)
![image](https://github.com/user-attachments/assets/04e6a3e5-28c5-43d4-9bdb-618ebb625073)




Modelo de Séries Temporais Prophet Baseado no Nível de Endividamento
![image](https://github.com/user-attachments/assets/cf3cbfa4-2dd0-4bf2-a94e-405f95905222)
![image](https://github.com/user-attachments/assets/d2f058d9-7838-4210-9d48-fd0322aa9c8a)



# Implementação dos modelos

A implementação do modelo foi feita através dos seguintes passos:
1.	A instalação da biblioteca Prophet.
   ````
# Importa as bibliotecas necessárias
from sklearn.metrics import mean_absolute_error
import pandas as pd
from prophet import Prophet
```` 
2.	A separação das colunas de dados (já anteriormente parametrizadas) entre a coluna ds (as séries de dados, que no caso seriam as datas separadas no modelo europeu, ou seja, aaaa-mm-dd) e a coluna y (que contem a variável dependente).
  ````
# Renomeia as colunas principais para o formato esperado pelo Prophet
tabela.rename(columns={"data": "ds", "y": "y"}, inplace=True)
```` 	
3.	O treinamento e configuração do modelo: as etapas de treinamento e teste dos dados já estão embutidas na implementação do algoritmo Prophet.
  ````
# Divida os dados para treino e teste
train_size = int(0.6 * len(tabela))
train, test = tabela[:train_size], tabela[train_size:]
````	
4.	A utilização do modelo para fazer previsões: usamos o ano de 2030 como ponto final das previsões do modelo, sendo possível estimar a variação do endividamento de 2024 até lá.
  ````
# Cria um dataframe para prever os próximos 60 meses
future = model.make_future_dataframe(periods=60, freq='MS')

# Adiciona os valores futuros para os regressores
for regressor in ['y1', 'y2', 'y3']:
    if regressor in tabela.columns:
        # Aqui assumimos que os valores futuros sejam a média dos valores passados
        # Ajuste isso com base em suas projeções ou dados específicos
        future[regressor] = tabela[regressor].mean()

# Realiza a previsão
forecast = model.predict(future)
````
5.	A visualização dos resultados através da plotagem de gráficos: os gráficos trazem algumas funções que auxiliam a entender os impactos da incorporação de regressores no modelo.
  ````
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
plt.title('Previsão de Séries Temporais com Prophet e Regressores')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.legend(loc='upper left')  # Posiciona a legenda
plt.grid(True)
plt.tight_layout()

# Exibe o gráfico
plt.show()

# Plota os componentes sazonais
fig2 = model.plot_components(forecast)
````
7.	Avaliação do modelo: cálculo do R² e do MSE.
   ````
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
````


> [!NOTE]
> Para ver o código deste modelo clique no link 👉 [Prophet_LucasSantos_Vinicius.py](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/src/Prophet_LucasSantos_Vinicius_Endividamento_e_Regrassores.py).

# Avaliação dos modelos criados

Para avaliar os modelos de séries temporais usando o Prophet, a avaliação foi feita através do Erro Quadrático Médio (MSE em inglês) e do coeficiente de determinação (R²). Em primeiro lugar, os resultados da avaliação do modelo em que foram inseridos os regressores ao modelo: enquanto o MSE apresentou um resultado moderado no desempenho do modelo (0.6242514687584728), na avaliação através do R² os resultados obtidos foram mais satisfatórios (0.9593074801682949), indicando que o modelo explica quase totalmente a variabilidade dos dados.
````
MSE: 0.6242514687584728
R²: 0.9593074801682949
````
Já no modelo em que o Prophet usou apenas a variação do endividamento para prever a série temporal, os resultados tiveram resultados piores, indicando que o modelo anterior captou melhor os ajustes de cada variável. Enquanto o MSE apresentou 2.2756528607697546, índice acima acima do 1, ou seja, os erros foram elevados ao quadrado individualmente, indicando um resultado ruim para explicar a variabilidade dos dados finais. Além disso, o R² também apresentou um resultado pior que no outro modelo (0.8516590608090697), mesmo que ainda satisfatório por estar próximo do 1.
````
MSE: 2.2756528607697546
R²: 0.8516590608090697
````


# Experimento #4

# Modelo Sarima 

O modelo SARIMA (Seasonal AutoRegressive Integrated Moving Average) é um modelo derivado do modelo ARIMA, que são técnicas que êm como objetivos a análise e a previsão de dados em séries temporais. Este é um modelo utilizado em análises econômicas, pois seu diferencial é justamente a previsão das séries temporais em conjuntos de dados. 

A implantação do modelo requer alguns passos, e os mais importantes serão detalhados a seguir:

## Carregamento e tratamento dos dados

As bibliotecas Python importadas para execução de todos os passos:
````
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
````
Após o carregamento dos dados, alguns cuidados devem ser tomados, a fim de garantir que o modelo seja capaz de identificar as séries temporais adequadamente. No trecho a seguir, definimos a coluna "Periodo" como o índice, e o seu formato de data, para delimitação da sazonalidade a ser observada pelo modelo.
````
# Definir data como índice
dados['Periodo'] = pd.to_datetime(dados['Periodo'], format='%m/%d/%Y')
dados = dados.set_index('Periodo')
````
Também foi necessário realizar a remoção de colunas, para que o modelo pudesse isolar os indicadores e executar a previsão adequadamente:
````
# Removendo colunas para facilitar o entendimento do modelo
dados_endiv = dados.drop(['Confianca_Valor', 'Selic_Valor', 'Inflacao_Acumulada'],axis=1)
````

## Delimitando os dados de treino e teste

Nesta etapa, delimitamos os dados que seriam utilizados para o aprendizado do modelo, daqueles que seriam utilizados para validação das predições, para avaliação dos resultados entregues pelo modelo. Para este exercício, dividimos a base 
````
# Definição do treinamento e testes do modelo
dados_treino = dados_endiv[dados_endiv.index < '2019-06-01']
dados_teste = dados_endiv[dados_endiv.index >= '2019-06-01']
````
É importante também que seja verificada a estacionariedade dos dados. Este trecho de código faz este trabalho, salientando que o resultado deverá ser menor que 0.05 para que o modelo funcione corretamente:
````
# Verificar estacionariedade (resultado precisa ser menor que 0.05)
result = adfuller(dados_endiv)
print("p-valor:", result[1])
````

## Aplicando o modelo
Este trecho de código é responsável pela aplicação do modelo Sarima no conjunto de dados. Vale ressaltar que os valores dentro das variáveis `order` e `seasonal_order` serão responsáveis pelos ajustes a serem realizados. Estas variáveis são definidas de acordo com as seguintes orientações:
p: Ordem do componente autorregressivo (AR). 
d: Ordem da diferenciação não sazonal. 
q: Ordem do componente de médias móveis (MA). 
P: Ordem do componente autorregressivo sazonal (SAR). 
D: Ordem da diferenciação sazonal. 
Q: Ordem do componente de médias móveis sazonais (SMA). 
m: Período da sazonalidade (por exemplo, 12 para dados mensais com sazonalidade anual). 

````
modelo = SARIMAX(dados_treino, order=(0,1,6), seasonal_order=(0,1,10,12)) 
resultado = modelo.fit()
````
Para o modelo, utilizamos os seguintes valores:
- P = 0, D = 1, Q = 6: Sem padrão sazonal esperado

- p = 0: Captura um efeito de dependência autorregressiva básica
- d = 1: Para tornar a série estacionária, caso necessário
- q = 10: Permite capturar flutuações curtas com média móvel
- s = 12: Mantido como padrão, caso sazonalidade residual seja detectada

## Predição do modelo
O modelo é aplicado em dois momentos, o primeiro, para a previsão com base no treinamento executado pelo algoritmo e validação com base nos dados de testes:
````
# Predições do modelo
predicao_teste = resultado.predict(start=dados_teste.index[0], end=dados_teste.index[-1])
````
E o segundo momento, onde é realizada uma previsão que vai além dos dados disponibilizados para treinamento e testes:
````
# Previsão para o modelo
passos_futuros = 36 # Variável recebe a quantidade de meses que faremos a previsão dos indicadores futuros
previsao = resultado.get_forecast(steps=passos_futuros)
````

## Impressão dos resultados
Como resultado das predições, encontramos os seguintes resultados, já levados para um gráfico agrupando os dados de treino, teste, predições realizadas para validação e predições para períodos futuros à série de dados fornecida para o modelo:
![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/docs/img/Treinamento%20Selic_Sarima.png)

## Avaliação do modelo

Avaliar um modelo de predição pode ser uma tarefa complexa, uma vez que, principalmente em relação a indicadores econômicos, existem inúmeros fatores externos que podem influenciar em movimentos de alta ou baixa de tais números. O Prophet e o Sarima são os modelos mais capazes de realizar tais predições, mas devemos nos atentar para o tratamento da base de dados antes de aplicar o modelo. É preciso que os dados sejam organizados e que um índice de tempo seja definido, para que o modelo possa buscar por padrões de sazonalidade e realizar predições adequadamente. Alguns fatores externos podem influenciar o resultado dos indicadores no mundo real, o que torna difícil uma predição condinzente com a realidade. Como exemplo, o resultado apresentado no gráfico a seguir, em que fica demononstrado que o modelo não foi capaz de se adaptar a uma situação inesperada com grande efeito sobre todo o cenário, como foi a pandemia da Covid-19. 

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/docs/img/Previs%C3%A3o%20Selic%2036m_Sarima.png)

Por isso, é necessário que o analista de dados use a ferramenta para realizar as predições, mas também, utilize do conhecimento relacionado a área estudada e analisada pela série de dados.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/docs/img/Resultado%20Selic_Sarima.png)


# Pipeline

Finalizando com a nossa pipeline, resolvemos fazer toda a sequência de ações tomadas para concluir a pesquisa para ajudar quem pretende trabalhar com os dados macroeconômicos e aprendizado de máquina no futuro. 
Começamos o trabalho reunindo os dados históricos sobre o valor da Selic, representada na base de dados como Selic_Valor, a inflação acumulada, representada como Inflação_Acumulada, e a confiança do consumidor, representada como Confiança_Valo. Além disso, organizamos a série histórica do período escolhido pegando os dados correspondentes ao dia primeiro de cada mês.

Preparação dos Dados: nessa etapa, realizamos a limpeza e formatação, convertendo datas, alterando a vírgula por ponto, separando e normalizando os dados selecionados. As variáveis foram mantidas na escala original para facilitar a interpretação direta, especialmente considerando o uso do Random Forest, que não é sensível a escalas.

Manuseio de Dados Temporais: A coluna Período, que representa o tempo, foi convertida para o tipo datetime para garantir a manipulação e ordenação corretas dos dados. Ordenamos a coluna em ordem crescente para manter a sequência temporal e garantir a visualização e capacidade de análise consistentes ao longo do tempo.

Separação dos Dados: Dividimos os dados em conjuntos de treino e teste na proporção de 70/30 para uma avaliação confiável dos modelos. O conjunto de treino foi usado para ajustar os modelos, enquanto o conjunto de teste ajudou a avaliar a performance em dados não vistos.

Construção do Modelo: Implementamos os algoritmos de Regressão Linear, Random Forest e Prophet. Para a Regressão Linear, focamos em uma abordagem direta, sem regularização adicional. No caso do Random Forest, experimentamos valores crescentes de n_estimators e diferentes profundidades máximas (max_depth) para garantir um equilíbrio entre precisão e performance. Os hiperparâmetros foram ajustados para otimizar o desempenho dos modelos. No caso do Prophet, os dados foram ajustados da seguinte maneira: separamos as colunas de série temporal e do y (no caso, o nível de endividamento), que é variável dependente que buscamos prever atrasvés do algoritmo. Optamos por separar a implementação do algoritmo Prophet em dois modelos, um baseado apenas na variação de y e outro com atuação de variáveis independentes y1, y2 e y3 (dados macroeconômicos do período em questão).

Avaliação do Modelo: Utilizamos métricas como MSE (Mean Squared Error) e R^2 Score para avaliar o desempenho dos modelos. A Regressão Linear forneceu uma linha de base simples, mas completa para a análise dos dados. A MSE foi de 13.91, indicando que a média dos erros ao quadrado das previsões do modelo foi relativamente alta. O R^2 Score negativo de -0.06 mostrou que o modelo não capturou a variação nos dados de forma eficaz.

Já no modelo de Random Forest, a MSE de 7.07 foi menor, indicando previsões mais próximas dos valores reais. O R^2 Score de -0.22 ainda sugere que há margem para melhorias, mas o modelo foi mais eficaz em explicar as variações dos dados.

Nos modelos de séries temporais baseado no algoritmo Prophet, a avaliação também se deu através do Erro Quadrático Médio (MSE em inglês) e do coeficiente de determinação (R²). Em primeiro lugar, os resultados da avaliação do modelo em que foram inseridos os regressores ao modelo: enquanto o MSE apresentou um resultado modesto no desempenho do modelo (0.6242514687584728, longe do 0, que indica que o desemepnho não foi satisfatório), na avaliação através do R² os resultados obtidos foram bem-sucedidos (0.96, próximo ao 1), indicando que o modelo explica quase totalmente a variabilidade dos dados.
Já no modelo em que o Prophet usou apenas a variação do endividamento para prever a série temporal, tanto MSE quanto R² indicaram resultados piores do que no outro modelo, sinalizando que a adição de regressores para treinamento do modelo pode servir como subsídio para melhor entendimento da variação do endividamento das famílias no Brasil.

Criamos gráficos para comparar dados reais e previstos, a fim de tentar prever o endividamento das famílias. Esses gráficos ajudaram a ilustrar a performance dos modelos e a identificar possíveis áreas de melhoria. Analisamos os resultados no contexto dos objetivos do estudo, discutindo as limitações e pontos fortes de cada modelo. Esta etapa foi crucial para entender as limitações dos dados e dos modelos utilizados, além de apontar direções para futuras melhorias e ajustes.

Foi muito engrandecedor conseguir avançar, aprender e concluir essa pesquisa. Espero que quem veja esse trabalho consiga aproveitar algo. Agradeçemos à professora Luciana pelo suporte.

# Vídeo Completo

O vídeo contem toda a apresentação e explicação dos experimentos realizados. 

Link: 
