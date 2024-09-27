# Conhecendo os dados

Nesta seção, deverá ser registrada uma detalhada análise descritiva e exploratória sobre a base de dados selecionada na Etapa 1 com o objetivo de compreender a estrutura dos dados, detectar eventuais _outliers_ e também, avaliar/detectar as relações existentes entre as variáveis analisadas.

Para isso, sugere-se que sejam utilizados cálculos de medidas de tendência central, como média, mediana e moda, para entender a centralidade dos dados; sejam exploradas medidas de dispersão como desvio padrão e intervalos interquartil para avaliar a variabilidade dos dados; sejam utilizados gráficos descritivos como histogramas e box plots, para representar visualmente as características essenciais dos dados, pois essas visualizações podem facilitar a identificação de padrões e anomalias; sejam analisadas as relações entre as variáveis por meio de análise de correlação, gráficos de dispersões, mapas de calor, entre outras técnicas. 

Inclua nesta seção, gráficos, tabelas e demais artefatos que você considere relevantes para entender os dados com os quais você irá trabalhar.  Além disso, inclua e comente os trechos de código mais relevantes desenvolvidos para realizar suas análises. Na pasta "src", inclua o código fonte completo.

# Selic e Confiança 

Iniciamos com a base de dados selecionada que contém informações, sobre a taxa selic, a inflação e
o endividamento das familias. Tentamos compreender a estrutura dos dados e suas inter-relações, focando 
na correlação desses dados junto aos gráficos para ver se podemos reconhecer padrões.

A análise de correlação foi realizada para entender melhor a relação das variáveis. A correlação entre a taxa
selic e o indice de confiança do consumidor mostrou uma relação moderada, com um coeficiente de aproximadamente
-0,5 . Isso significa que, à medida que a selic aumenta a confiança do consumidor tende a diminuir, o que faz 
sentido em um contexto econômico onde o aumento dos juros desestimula o consumo e o crédito, afetando 
a perceplçao dos consumidores sobre a economia. 

Começando pelo mapa de calor e histograma(Codigo)

![image](https://github.com/user-attachments/assets/79f89cb7-6b22-4e0b-82aa-6658fc313ccb)


Mapa de calor

![image](https://github.com/user-attachments/assets/e7ffa186-5858-4699-a83a-8238db6a8b40)


Histograma

![image](https://github.com/user-attachments/assets/dcc7cf71-9c0d-4b0e-b0ee-28543c3c298e)


# IPCA e ICC

Buscamos identificar a correlação entre os atributos IPCA e ICC para verificar se existe alguma influência da inflação no Índice de Confiança do Consumidor.

Foram utilizados dados do período de maio de 2011 a maio de 2023, considerando a variação mensal da inflação e o valor do ICC de cada mês.

Foi utilizado o Google Planilhas para organizar os dados mensais adquiridos dos conjuntos de dados previamente definidos e apliquei a fórmula de correlação para obter o coeficiente de correlação:

=CORREL(B2:B148;C2:C148)

O coeficiente de correlação encontrado foi de -0,03329.

Essa correlação negativa indica uma leve tendência inversa, ou seja, quando o IPCA aumenta, o ICC tende a diminuir. No entanto, a força dessa relação é extremamente fraca, com o valor muito próximo de zero, sugerindo que não existe uma correlação significativa entre o ICC e o IPCA nos dados analisados.

Há uma fraca influência do IPCA sobre o ICC, indicando que outros fatores podem estar impactando o ICC de forma mais significativa.

Em resumo, a relação entre o IPCA e o ICC é muito fraca, o que sugere que a inflação não está fortemente relacionada às variações do ICC.

Grafico de Dispersão

![Image](https://github.com/user-attachments/assets/3bfddc8d-5d03-4f35-8ae3-ea71574ec67e)


## Selic e Endividamento Total

Analisando e comparando as informações dos dados de Endividamento e da taxa Selic entre março de 2011 e maio de 2024.

Nota-se que o endividamento total apresenta uma tendência de aumento gradual ao longo do tempo, principalmente a partir de 2021, aumento que se deu provavelmente por mudanças econômicas, políticas e até mesmo a pandemia. Já a taxa Selic, apesar das variações durante o período, sofreu uma grande queda de 2016 à 2020 e assim como o endividamento um grande aumento de 2021 pra cá.

Em alguns períodos, parece que quando a taxa Selic cai, o endividamento tende a aumentar, isso pode indicar que quando as taxas de juros estão mais baixas, acaba incentivando o aumento do endividamento possivelmente com custo de empréstimos e financiamentos estando mais acessíveis.

Foi realizada a organização dos dados através do Google Planilhas e o cálculo de correlação ( =CORREL(B2:B160;C2:C160) ) e o resultado encontrado foi de 0,1451650055.

Esse resultado indica que a relação entre o endividamento total e a taxa Selic é fraca. Isso sugere que, embora possa haver alguma influência da taxa Selic sobre o endividamento, essa influência não é forte e outros fatores provavelmente desempenham um papel mais significativo.


Histograma
![image](https://github.com/user-attachments/assets/344f3231-244b-4a93-b186-6fc8d8e36bc1)



## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a atenção? Foi possível identificar correlação entre os atributos? Que tipo de correlação (forte, fraca, moderada)? 

Com essa análise, foi possível identificar padrões claros de como a política monetária impacta diretamente 
a percepção dos consumidores e o comportamento de crédito das famílias. Os gráficos e cálculos fornecem uma
 base para que possamos aprofundar as investigações sobre a relação entre as variáveis, especialmente em períodos de crise e dificuldade .

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação. Vale destacar que, preferencialmente, as análises deverão ser realizadas utilizando a linguagem de programação Python.

Pycharm : IDE que usei para os codigos em python.  
Python (Pandas, Numpy, Matplotlib e Seaborn): Pandas e o Numpy são bibliotecas de manipulação e análise dos dados, incluindo cálculo de médias, medianas, desvio padrão e correlação.  
O Matplotlib e Seaborn também são bibliotecas utilizadas para visualização e geração dos gráficos dos dados, incluindo histogramas, gráficos de correlação e mapas de calor.



