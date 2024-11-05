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


Neste momento, vou descrever os algoritmos de aprendizado de máquina que escolhemos para a construção dos modelos de predição: Regressão Linear e Random Forest. 
Ambos os algoritmos foram selecionados devido às suas características distintas e aos benefícios que oferecem para entender e prever o comportamento dos dados em 
relação ao endividamento das famílias.

Em cada modelo, testamos diferentes configurações de parâmetros. Para a Regressão Linear, focamos em uma abordagem direta, sem regularização adicional. 
No caso do Random Forest, experimentamos valores crescentes de n_estimators e diferentes profundidades máximas para garantir um equilíbrio entre precisão e performance. 
Essas escolhas foram justificadas pela observação dos erros e da variabilidade dos dados.

Regressão Linear

A Regressão Linear é um dos algoritmos mais amplamente utilizados para tarefas de predição. Ela parte do princípio de que existe uma relação linear entre as variáveis 
independentes e a variável dependente. Neste caso, utilizamos variáveis como a taxa Selic, o índice de confiança do consumidor e a inflação para prever o nível de 
endividamento familiar.

A principal vantagem da Regressão Linear é sua simplicidade e interpretabilidade, permitindo uma análise direta sobre o impacto de cada variável independente. 
No entanto, sua limitação mais relevante é a suposição de uma relação linear entre as variáveis, o que pode não fornecer os melhores resultados em análises mais 
complexas.

A Regressão Linear foi escolhida devido à sua capacidade de fornecer uma linha de base para comparação com outros modelos mais complexos. 
Ela ajuda a identificar se uma simples relação linear é suficiente para explicar os dados. Neste primeiro teste, optamos por uma Regressão Linear simples como
ponto de partida.

![RegressaoLinear](https://github.com/user-attachments/assets/cef0306a-c524-4c98-b654-e90d54417fb4)

Algoritimo correspondente na pasta SRC.

Random Forest

O Random Forest é um modelo de aprendizado de máquina baseado em árvores de decisão. Ele funciona criando múltiplas árvores de decisão aleatórias a partir dos 
dados e combinando suas previsões para obter uma predição.

A principal vantagem do Random Forest é sua capacidade de capturar relações complexas entre variáveis, o que torna o modelo eficaz para dados que não seguem 
uma estrutura linear. Uma das desvantagens é que o modelo pode ser bastante custoso e mais difícil de interpretar em comparação à Regressão Linear. 
Escolhemos o Random Forest como um modelo para analisar relações não-lineares entre as variáveis independentes e o nível de endividamento.

![RandomForest](https://github.com/user-attachments/assets/5fdc57d2-2985-40ac-a6b4-037dc2ba98cf)

Algoritimo correspondente na pasta SRC.

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
