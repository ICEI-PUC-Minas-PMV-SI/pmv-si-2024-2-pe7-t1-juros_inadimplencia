# Conhecendo os dados

Nesta seção, deverá ser registrada uma detalhada análise descritiva e exploratória sobre a base de dados selecionada na Etapa 1 com o objetivo de compreender a estrutura dos dados, detectar eventuais _outliers_ e também, avaliar/detectar as relações existentes entre as variáveis analisadas.

Para isso, sugere-se que sejam utilizados cálculos de medidas de tendência central, como média, mediana e moda, para entender a centralidade dos dados; sejam exploradas medidas de dispersão como desvio padrão e intervalos interquartil para avaliar a variabilidade dos dados; sejam utilizados gráficos descritivos como histogramas e box plots, para representar visualmente as características essenciais dos dados, pois essas visualizações podem facilitar a identificação de padrões e anomalias; sejam analisadas as relações entre as variáveis por meio de análise de correlação, gráficos de dispersões, mapas de calor, entre outras técnicas. 

Inclua nesta seção, gráficos, tabelas e demais artefatos que você considere relevantes para entender os dados com os quais você irá trabalhar.  Além disso, inclua e comente os trechos de código mais relevantes desenvolvidos para realizar suas análises. Na pasta "src", inclua o código fonte completo.

# Selic e Confiança 

O início será com a base de dados selecionada que contém informações, sobre a taxa SELIC, a inflação e
o endividamento das famílias. Serão verificados a estrutura dos dados e suas inter-relações, focando 
na correlação desses dados junto aos gráficos para ver se podemos reconhecer padrões.

A análise de correlação foi realizada para entender melhor a relação das variáveis. A correlação entre a taxa
selic e o indice de confiança do consumidor mostrou uma relação moderada, com um coeficiente de aproximadamente
-0,5 . Isso significa que, à medida que a SELIC aumenta a confiança do consumidor tende a diminuir, o que faz 
sentido em um contexto econômico onde o aumento dos juros desestimula o consumo e o crédito, afetando 
a perceplçao dos consumidores sobre a economia. 

Começando pelo mapa de calor e histograma(Codigo completo na pasta SRC)

![image](https://github.com/user-attachments/assets/4eb7a339-31ef-4307-bbe5-c2ebb5478e45)
![image](https://github.com/user-attachments/assets/7f8406e5-713e-45a0-a225-de79b9033e4e)



Mapa de calor

![Mapa de Calor](https://github.com/user-attachments/assets/dc7e9b75-4fa4-4cac-bcf0-376b530106f2)



Histograma

![Histogramas](https://github.com/user-attachments/assets/88ec9591-5337-4025-a54f-8911230db464)


Evolução 

![Evolução](https://github.com/user-attachments/assets/a906cfcb-753d-4fa7-b10f-404b51c13e43)

# SELIC, IPCA e INPC

Com esta análise, buscou-se identificar se havia uma relação entre as taxas SELIC e os valores de IPCA e INPC, que são índices que medem a inflação de preços ao consumidor amplo e de inflação de preços de produtos consumidos pelas famílias com renda entre 1 e 5 salários mínimos.  
Para esta análise, iremos utilizar os dados de fevereiro de 2010 a março de 2023, uma vez que é o intervalo de dados descritos nos datasets utilizados para esta análise. Para o modelo em questão, utilizar este intervalo de datas irá reforçar as informações aqui descritas.  
Com base nesta análise, observada nos gráficos a seguir, pode-se estabelecer uma relação direta entre a SELIC definida no período avaliado, sendo que, conforme as análises, a SELIC tende a subir quando temos períodos de aumento na inflação.  
Uma observação importante, é que em alguns momentos, esta tendência não se confirmou de forma mais evidente, sendo entre novembro de 2012 a julho de 2013 e entre junho de 2022 e o fim da série avaliada (março de 2023). Como sabemos, a SELIC é definida em reuniões do COPOM, realizadas a cada 45 dias, e leva em consideração diversos fatores econômicos e políticos, além de outros aspectos que possam alterar as relações de consumo do país. Sendo assim, durante estes períodos, algum fato relevante aconteceu para que houvesse este movimento observado.  

![Selic vs IPCA e INPC](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-2-pe7-t1-juros_inadimplencia/blob/main/docs/img/Selic%20X%20IPCA%20e%20INPC.png)

A análise descrita nessa sessão foi realizada através do Power BI. O tratamento dos dados foi realizado para adequação das datas, uma vez que os dados informados da SELIC por exemplo, consideram todos os dias desde 04/06/1986. Além disso, filtros de datas foram utilizados, para desconsiderar os intervalos não computados dos datasets.  

# IPCA e ICC

Buscou-se identificar a correlação entre os atributos IPCA e ICC para verificar se existe alguma influência da inflação no Índice de Confiança do Consumidor.

Foram utilizados dados do período de maio de 2011 a maio de 2023, considerando a variação mensal da inflação e o valor do ICC de cada mês.

Foi utilizado o Google Planilhas para organizar os dados mensais adquiridos dos conjuntos de dados previamente definidos e apliquei a fórmula de correlação para obter o coeficiente de correlação:

=CORREL(B2:B148;C2:C148)

O coeficiente de correlação encontrado foi de -0,03329.

Essa correlação negativa indica uma leve tendência inversa, ou seja, quando o IPCA aumenta, o ICC tende a diminuir. No entanto, a força dessa relação é extremamente fraca, com o valor muito próximo de zero, sugerindo que não existe uma correlação significativa entre o ICC e o IPCA nos dados analisados.

Há uma fraca influência do IPCA sobre o ICC, indicando que outros fatores podem estar impactando o ICC de forma mais significativa.

Em resumo, a relação entre o IPCA e o ICC é muito fraca, o que sugere que a inflação não está fortemente relacionada às variações do ICC.

Grafico de Dispersão

![Image](https://github.com/user-attachments/assets/3bfddc8d-5d03-4f35-8ae3-ea71574ec67e)


## SELIC e Endividamento Total

Analisando e comparando as informações dos dados de Endividamento e da taxa SELIC entre março de 2011 e maio de 2024.

Nota-se que o endividamento total apresenta uma tendência de aumento gradual ao longo do tempo, principalmente a partir de 2021, aumento que se deu provavelmente por mudanças econômicas, políticas e até mesmo a pandemia. Já a taxa SELIC, apesar das variações durante o período, sofreu uma grande queda de 2016 à 2020, enquanto foi acompanhada por um grande aumento do endividamento a partir de 2021.

Em alguns períodos, parece que quando a taxa SELIC cai, o endividamento tende a aumentar, isso pode indicar que quando as taxas de juros estão mais baixas, acaba incentivando o aumento do endividamento possivelmente com custo de empréstimos e financiamentos estando mais acessíveis.

Foi realizada a organização dos dados através do Google Planilhas e o cálculo de correlação ( =CORREL(B2:B160;C2:C160) ) e o resultado encontrado foi de 0,1451650055.

Esse resultado indica que a relação entre o endividamento total e a taxa SELIC é fraca. Isso sugere que, embora possa haver alguma influência da taxa SELIC sobre o endividamento, essa influência não é forte e outros fatores provavelmente desempenham um papel mais significativo.


Histograma
![image](https://github.com/user-attachments/assets/344f3231-244b-4a93-b186-6fc8d8e36bc1)

## Taxa Selic e Endividamento das famílias

A análise indica que a uma correlação positiva , pois quando uma variável aumenta , a outra aumenta.
O coeficienta encontrado foi de 0,15 pela análise dos dados da planilha aplicando a fórmula de correlação.
Sendo que a elevação das taxas de juros impacta diretamente no endividamento das famílias, quando está mais alta limita o poder de compra, o acesso ao crédito e consequentemente eleva o endividamento das famílias.
É uma análise complexa, pois envolve vários fatores como: investimentos internos e externos, indice de confiança no atual governo, politicas para estimulo da economia, entre outros.
Dados extraídos entre março de 2011 a maio de 2024.

![image](https://github.com/user-attachments/assets/d7cdb98c-1c39-43f5-84de-b9dad86a159f)

![image](https://github.com/user-attachments/assets/066d7094-772c-4273-b1b3-e59ed4dd4f8b)

![image](https://github.com/user-attachments/assets/8cb5a87d-4730-46a8-8cc0-5b92d4f154ac)


## Descrição dos achados

A análise descritiva dos dados revela padrões interessantes. A taxa SELIC, por exemplo, tem um impacto significativo no endividamento, enquanto a inflação afeta de forma mais branda a confiança do consumidor. 

A combinação de medidas estatísticas e gráficos permitiu uma compreensão mais profunda dos dados e foi possível identificar padrões claros de como a política monetária impacta diretamente a percepção dos consumidores e o comportamento de crédito das famílias. Os gráficos e cálculos fornecem uma base sólida para aprofundar as investigações sobre a relação entre as variáveis, especialmente em períodos de crise. Assim, conclui-se que a relação entre o endividamento geral das famílias e a variação da SELIC na série temporal trabalhada exige a adição de novas variáveis para a geração de um modelo que gere resultados robustos na previsão do nível de endividamento. Além disso, a percepção das famílias sobre o cenário futuro da inflação pode servir como indicador da variável a ser melhor trabalhada como diferencial na construção do modelo.


## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação. Vale destacar que, preferencialmente, as análises deverão ser realizadas utilizando a linguagem de programação Python.

Pycharm : IDE que usei para os codigos em python.  
Python (Pandas, Numpy, Matplotlib e Seaborn): Pandas e o Numpy são bibliotecas de manipulação e análise dos dados, incluindo cálculo de médias, medianas, desvio padrão e correlação.  
O Matplotlib e Seaborn também são bibliotecas utilizadas para visualização e geração dos gráficos dos dados, incluindo histogramas, gráficos de correlação e mapas de calor.



