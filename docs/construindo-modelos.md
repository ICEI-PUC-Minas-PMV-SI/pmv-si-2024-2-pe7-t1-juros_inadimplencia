# Preparação dos dados

Nesta etapa, deverão ser descritas todas as técnicas utilizadas para pré-processamento/tratamento dos dados.

Algumas das etapas podem estar relacionadas à:

* Limpeza de Dados: trate valores ausentes: decida como lidar com dados faltantes, seja removendo linhas, preenchendo com médias, medianas ou usando métodos mais avançados; remova _outliers_: identifique e trate valores que se desviam significativamente da maioria dos dados.

* Transformação de Dados: normalize/padronize: torne os dados comparáveis, normalizando ou padronizando os valores para uma escala específica; codifique variáveis categóricas: converta variáveis categóricas em uma forma numérica, usando técnicas como _one-hot encoding_.

* _Feature Engineering_: crie novos atributos que possam ser mais informativos para o modelo; selecione características relevantes e descarte as menos importantes.

* Tratamento de dados desbalanceados: se as classes de interesse forem desbalanceadas, considere técnicas como _oversampling_, _undersampling_ ou o uso de algoritmos que lidam naturalmente com desbalanceamento.

* Separação de dados: divida os dados em conjuntos de treinamento, validação e teste para avaliar o desempenho do modelo de maneira adequada.
  
* Manuseio de Dados Temporais: se lidar com dados temporais, considere a ordenação adequada e técnicas específicas para esse tipo de dado.
  
* Redução de Dimensionalidade: aplique técnicas como PCA (Análise de Componentes Principais) se a dimensionalidade dos dados for muito alta.

* Validação Cruzada: utilize validação cruzada para avaliar o desempenho do modelo de forma mais robusta.

* Monitoramento Contínuo: atualize e adapte o pré-processamento conforme necessário ao longo do tempo, especialmente se os dados ou as condições do problema mudarem.

* Entre outras....

Avalie quais etapas são importantes para o contexto dos dados que você está trabalhando, pois a qualidade dos dados e a eficácia do pré-processamento desempenham um papel fundamental no sucesso de modelo(s) de aprendizado de máquina. É importante entender o contexto do problema e ajustar as etapas de preparação de dados de acordo com as necessidades específicas de cada projeto.

## Preparação dos dados

Quanto à limpeza dos dados e remoção de outliers, as bases selecionadas não apresentavam dados faltantes nem a necessidade de remoção de outliers.
Já na Transformação de Dados, verifiquei a escala das variáveis, especialmente para a Regressão Linear, pois os algoritmos de aprendizado se beneficiam de dados em
uma mesma escala. Decidi manter as variáveis na escala original devido ao uso de Random Forest, que não é sensível a escalas, e para permitir uma interpretação direta 
dos coeficientes na Regressão Linear. A coluna Período, que representa o tempo, foi convertida para o tipo datetime para garantir a manipulação e ordenação corretas dos 
dados, uma vez que ela representa uma variável temporal importante para o modelo.

No Manuseio de Dados Temporais, foi essencial ordenar a coluna Período em ordem 
crescente para manter a sequência temporal e uma visualização e análise consistentes ao longo do tempo. Essa ordenação permite observar melhor as tendências e relações 
ao longo dos períodos. Quanto à Separação de Dados, dividi os dados em conjuntos de treino e teste usando uma proporção de 70/30 para uma avaliação confiável do modelo. 
O conjunto de treino foi utilizado para ajustar os modelos, enquanto o conjunto de teste ajudou a avaliar a performance dos mesmos em dados não vistos. Essas etapas de 
preparação de dados foram fundamentais para garantir que os modelos tivessem uma base confiável e representativa dos dados reais, aumentando a precisão e a generalização
dos modelos de predição. A preparação dos dados busca assegurar que o aprendizado dos algoritmos capture padrões importantes, maximizando o desempenho e a validade das 
previsões feitas para o endividamento das famílias.



# Descrição dos modelos

Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever os algoritmos de aprendizado de máquina selecionados para a construção dos modelos propostos. Inclua informações abrangentes sobre cada algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha de cada um dos algoritmos. 

Explore aspectos específicos, como o ajuste dos parâmetros livres de cada algoritmo. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas.

Como parte da comprovação de construção dos modelos, um vídeo de demonstração com todas as etapas de pré-processamento e de execução dos modelos deverá ser entregue. Este vídeo poderá ser do tipo _screencast_ e é imprescindível a narração contemplando a demonstração de todas as etapas realizadas.

## Descrição dos modelos


Vou descrever os algoritmos de aprendizado de máquina que escolhemos para a construção dos modelos de predição. Foram eles a Regressão Linear e o Random Forest. 
Ambos os algoritmos foram selecionados devido às suas características distintas e aos benefícios que oferecem para entender e prever o comportamento dos dados em 
relação ao endividamento das famílias.

Em cada modelo, testamos diferentes configurações de parâmetros. Para a Regressão Linear, focamos em uma abordagem direta, sem regularização adicional. 
No caso do Random Forest, experimentamos valores crescentes de n_estimators e diferentes profundidades máximas para garantir um equilíbrio entre precisão e performance. 
Essas escolhas foram justificadas pela observação dos erros e da variabilidade dos dados.

Regressão Linear

A regressão linear é um método estatístico usado para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. O objetivo é ajustar uma linha reta que minimiza a soma dos quadrados das diferenças entre os valores observados e os valores previstos. Também observamos que ele possui apenas o parâmetro de coeficiente de inclinação da linha.
A Regressão Linear foi escolhida devido à sua capacidade de fornecer uma linha de base para comparação com outros modelos mais complexos. 
Ela ajuda a identificar se uma simples relação linear é suficiente para explicar os dados. Neste primeiro teste, optamos por uma Regressão Linear simples como
ponto de partida.

![RegressaoLinear](https://github.com/user-attachments/assets/57316d07-b0ec-479f-b299-f45c6494c935)


Algoritimo correspondente a imagem está na pasta SRC. Com o nome Regressao_Linear_LucasLima_Geraldo.

Random Forest

O Random Forest é um algoritmo de aprendizado de máquina baseado em conjuntos que constrói múltiplas árvores de decisão durante o treinamento e apresenta a média das previsões individuais das árvores para melhorar a precisão. Uma das vantagens é sua robustez em relação a outliers e sua capacidade de lidar bem com grandes conjuntos de dados por outro lado, pode ser complicado ter poder computacional suficiente para processar os dados e sua interpretação pode ser mais complicada.
Com os parâmetros livres alteramos os:

n_estimators. Que é o número de árvores na floresta.

max_depth. que é a profundidade máxima de cada árvore.

min_samples_split que é o número mínimo de amostras necessárias para dividir um nó interno.

Escolhemos o Random Forest como um modelo para analisar relações não-lineares entre as variáveis independentes alem de experimentarmos diferentes valores para n_estimators e max_depth para encontrar o melhor ajuste, buscando tentar prever o nível de endividamento.

![RandomForest](https://github.com/user-attachments/assets/fce3e796-4927-409c-b3c0-b939d73017cf)


Algoritimo correspondente a imagem está na pasta SRC. Com o nome Random_Forest_LucasLima_Geraldo.

# Avaliação dos modelos criados

## Métricas utilizadas

Nesta seção, as métricas utilizadas para avaliar os modelos desenvolvidos deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 

## Observações importantes

Todas as tarefas realizadas nesta etapa deverão ser registradas em formato de texto junto com suas explicações de forma a apresentar  os códigos desenvolvidos e também, o código deverá ser incluído, na íntegra, na pasta "src".

Além disso, deverá ser entregue um vídeo onde deverão ser descritas todas as etapas realizadas. O vídeo, que não tem limite de tempo, deverá ser apresentado por **todos os integrantes da equipe**, de forma que, cada integrante tenha oportunidade de apresentar o que desenvolveu e as  percepções obtidas.

## Avaliação dos modelos criados

Aqui resolvi compilar os itens solicitados na parte da avaliação dos modelos. Começando pelas métricas onde usamos a Mean Squared Error a MSE. Ela mede a média dos quadrados dos erros, que são as diferenças entre os valores previstos e os valores observados. Escolhemos o MSE pois é uma métrica comum para problemas de regressão e é fácil de interpretar. Além da MSE escolhemos o R^2 Score. Ele representa a proporção da variância da variável dependente que é explicada pelas variáveis independentes no modelo. O R^2 também foi escolhido pois ele fornece uma medida de quão bem os valores previstos se ajustam aos dados reais.

Agora vamos falar sobre os resultados obtidos. A Regressão Linear forneceu uma linha de base simples, mas completa para a análise dos dados. A MSE foi de de 13.91 indica que a média dos erros ao quadrado das previsões do modelo foi relativamente alta, mostrando que as previsões não estavam muito próximas dos valores reais. Além disso, o R^2 Score negativo de -0.06 nos diz que o modelo não foi capaz de capturar a variação nos dados de forma eficaz, o que significa que as previsões feitas pela regressão linear são menos confiáveis. Isto pode ser atribuído à simplicidade do modelo, que assume uma relação linear entre as variáveis, não capturando as complexidades e não linearidades presentes nos dados .

![image](https://github.com/user-attachments/assets/4f55d4fe-1134-407f-b425-fa1418bbaed4)


Já no modelo de Random Forest em comparação à Regressão Linear. A MSE de 7.07, menor do que a da Regressão Linear, indica que o modelo de Random Forest fez previsões mais próximas dos valores reais. No entanto, o R^2 Score de -0.22 ainda sugere que tenha sido mais eficiente em explicar as variações dos dados. 

![image](https://github.com/user-attachments/assets/369cb0c0-dca6-4a96-9765-ad3327742d1f)


Ambos os modelos mostram a necessidade de uma análise mais profunda e possivelmente a integração de dos e metodos adicionais para demostrar melhor as variações nos dados de endividamento familiar. A Regressão Linear, apesar de ser uma boa linha de base, não é suficiente para este conjunto de dados, enquanto o Random Forest, mesmo sendo mais eficaz, ainda precisa ser ajustado para um desempenho superior.

Estas análises e interpretações apesar de não retornarem o resultado desejavamos foram essenciais para entendermos as limitações dos modelos e dados utilizados e apontam para futuras melhorias e ajustes, visando previsões mais precisas e confiáveis.

Finalizando com a nossa pipeline iniciamos os trabalhos reunindo os dados históricos sobre o valor da selic representada na base de dados como (Selic_Valor), a inflação acumulada representada na base de dados como (Inflação_Acumulada) e a confiança do consumidor representada na base de dados como (Confiança_Valor).
Na preparação dos dados realizamos a limpeza e formatação dos dados, convertendo datas, alterando a virgula por ponto e separando e normalisando os dados selecionados.
Para a contrução do modelo implementamos os algoritmos de Regressão Linear e Random Forest, ajustando os hiperparâmetros e treinando os modelos.
Com ela veio a avaliação do modelo e utilizamos métricas como MSE e R^2 Score para avaliar o desempenho dos modelos.
Sobre os resultados criamos gráficos para comparar dados reais e previstos a fim de tentar prever o endividamento das familias. 
Para finalizar com a interpretação e as discuções onde analisamos os resultados no contexto dos objetivos do estudo e realmente foi muito engrandecedor conseguir avançar, aprender e concluir essa pesquisa. Deixo os agradecimentos aos colegas de grupo e a professora Luciana. 
