# Conhecendo os dados

Nesta seção, deverá ser registrada uma detalhada análise descritiva e exploratória sobre a base de dados selecionada na Etapa 1 com o objetivo de compreender a estrutura dos dados, detectar eventuais _outliers_ e também, avaliar/detectar as relações existentes entre as variáveis analisadas.

Para isso, sugere-se que sejam utilizados cálculos de medidas de tendência central, como média, mediana e moda, para entender a centralidade dos dados; sejam exploradas medidas de dispersão como desvio padrão e intervalos interquartil para avaliar a variabilidade dos dados; sejam utilizados gráficos descritivos como histogramas e box plots, para representar visualmente as características essenciais dos dados, pois essas visualizações podem facilitar a identificação de padrões e anomalias; sejam analisadas as relações entre as variáveis por meio de análise de correlação, gráficos de dispersões, mapas de calor, entre outras técnicas. 

Inclua nesta seção, gráficos, tabelas e demais artefatos que você considere relevantes para entender os dados com os quais você irá trabalhar.  Além disso, inclua e comente os trechos de código mais relevantes desenvolvidos para realizar suas análises. Na pasta "src", inclua o código fonte completo.

# Selic e Confiança 

Iniciamos com a base de dados selecionada que contém informações, sobre a taxa selic, a inflação e
o endividamento das familias. Tentamos compreender a estrutura dos dados e suas inter-relações, focando 
na correlação desses dados junto aos gráficos para ver se podemos reconhecer padroões.

A análise de correlação foi realizada para entender melhor a relação das variáveis. A correlação entre a taxa
selic e o indice de confiança do consumidor mostrou uma relação moderada, com um coeficiente de aproximadamente
-0,5 . Isso significa que, à medida que a selic aumenta a confiança do consumidor tende a diminuir, o que faz 
sentido em um contexto econômico onde o aumento dos juros desestimula o consumo e o crédito, afetando 
a perceplçao dos consumidores sobre a economia. 

Começando pelo mapa de calor e historiograma(Codigo)

![image](https://github.com/user-attachments/assets/e5f08a84-aca8-468c-a926-dca7a5a18b7b)



Mapa de calor

![image](https://github.com/user-attachments/assets/1b69d447-be47-4900-8173-17b0e17a2e9a)


Historiograma

![image](https://github.com/user-attachments/assets/259c86dd-31bb-4f39-be15-ee9df929475d)




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



