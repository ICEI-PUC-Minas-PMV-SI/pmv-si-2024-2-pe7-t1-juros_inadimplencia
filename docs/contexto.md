# Introdução

Em uma sociedade capitalista, uma grande preocupação dos órgãos reguladores é manter as relações de consumo e oferta de recursos de forma sadia, protegendo o sistema financeiro de cenários de grande inadimplência, que, de forma exagerada, pode contribuir para a bancarrota financeira não só de empresas, mas de nações. Além das empresas, as famílias também podem contrair dívidas além das suas capacidades de pagamento, e, por isso, entender qual é o perfil de endividamento pode contribuir para manter este sistema financeiro operando de forma saudável, evitando que as famílias atinjam níveis de endividamento irreparáveis.<br>

Com esse projeto, buscamos analisar se existe uma relação entre a taxa Selic e o endividamento das famílias brasileiras, separando por categoria de linha de crédito, considerando também o impacto de fatores como a inflação e o Índice de Confiança do Consumidor.<br>

Devido a importancia do crédito no cotidiano das famílias, e sua influência direta na saúde financeira da população brasileira, é importante entender como o endividamento das famílias reage às políticas de facilitação de acesso ao crédito realizadas pelo Comitê de Política Monetária (COPOM), quando o mesmo reduz a taxa Selic, ou quando este mesmo comitê opta pela limitação de concessão de crédito, elevando esta taxa.<br>

O objetivo geral deste trabalho é identificar padrões e correlações que possam fornecer dados sobre como a variação na Selic impacta diferentes categorias do endividamento familiar. Entender estes padrões facilita o entendimento do nível de endividamento das famílias brasileiras e suas consequências sobre a economia, como a inadimplência e a retração do consumo.<br>


## Problema

A principal questão que gostariamos de responde é "Com base na taxa Selic, é possível estimar o percentual de endividamento das famílias por categoria de crédito no Brasil?"

A pergunta sobre a possibilidade de estimar o percentual de endividamento familiar por categoria de crédito a partir da taxa Selic revela a necessidade de uma análise mais profunda sobre a sensibilidade de cada tipo de crédito às variações da taxa básica de juros. Em um cenário de alta inflação e incertezas econômicas, compreender como o crédito pessoal, consignado e imobiliário respondem às oscilações da Selic é crucial para as famílias, que buscam equilibrar seus orçamentos e evitar o endividamento excessivo.

O problema abordado é relevante porque as famílias enfrentam desafios ao tentar equilibrar suas finanças em um ambiente de taxas de juros variáveis, o que pode resultar em um endividamento excessivo ou insustentável.

Este projeto será desenvolvido a partir da análise de datasets que incluem dados da Selic, inflação, Índice de Confiança do Consumidor e dados de endividamento por categoria de crédito, com o foco acadêmico e analítico. 


## Questão de pesquisa

Diante do cenário econômico brasileiro, marcado por oscilações frequentes na taxa Selic e variações nos índices de inflação surge a necessidade de entender como esses fatores afetam o comportamento financeiro das famílias e sua qualidade de vida. Portanto, a questão central que norteia nossa pesquisa é:

Como a variação da taxa Selic influencia o percentual de endividamento das famílias brasileiras por categoria de crédito, considerando também o impacto da inflação?

Pensamos que esta questão é fundamental para desvendar as relações entre política monetária e o endividamento familiar. Ao final da pesquisa, gostariamos de responder a essa questão, contribuindo para uma compreensão mais ampla do impacto das flutuações na vida das pessoas. 


## Objetivos preliminares

Como objetivos para esta pesquisa, buscamos:  
- Projetar o endividamento das famílias com base na taxa Selic e a inflação, a partir de dados históricos
- Com base nos dados de endividamento atuais, estimar qual deve ser o tipo de política financeira a ser adotada


## Justificativa

Escolhemos trabalhar com os dados de Selic, inflação e endividamento por linha de crédito, porque acreditamos que esses fatores estão intrinsecamente conectados na qualidade de vida das famílias. A análise desses dados permite não apenas entender as dinâmicas econômicas, mas também oferece valiosas ideias para a formulação de políticas públicas mais eficazes, capazes de proteger a saúde financeira das famílias, pois a inadimplência afeta diretamente a capacidade das famílias de consumir, fazer novos investimentos para movimentar a economia. No Brasil as taxas de juros são elevadas tornando o crédito mais caro provocando risco de inadimplência. Seguiremos nesse trabalho com a definição do Banco Central de endividamento: a relação entre o valor atual das dívidas das famílias com o Sistema Financeiro Nacional e a renda das famílias acumulada nos últimos doze meses (BANCO CENTRAL DO BRASIL, 2024).

Dados do Banco Central do Brasil mostram que, em períodos de alta na taxa Selic, a tendência é que o custo do crédito aumente, o que pode impactar diretamente o nível de endividamento das famílias. Por outro lado, períodos de baixa na Selic podem incentivar o consumo, mas também elevar o risco de endividamento excessivo, especialmente em categorias de crédito de maior risco. Com um cenário de 40% das famílias inadimplentes e taxas de juros extremanmente elevadas é necessário entender como as políticas de crédito e a regulamentação das taxas podem aliviar as contas nos lares dos brasileiros.

São dados preocupantes onde tivemos recentemente ações da equipe econômica em relação a taxa de juros média do cartão de crédito rotativo superior a 400% ao ano, uma das mais alts do mundo e do cheque especial que tinha taxa média de 130% ao ano. Números como esses revelam a urgência de mudanças profundas no sistema financeiro brasileiro. A equipe econômica já iniciou um movimento para conter esses abusos, mas é preciso ir além. A população precisa de soluções concretas para lidar com esse endividamento excessivo.

Em resumo, a motivação para este trabalho é mostrar como o endividamento das famílias esta ligado a politicas economicas e como podemos mitigar para promover uma economia mais saudável e sustentável. 


## Público-Alvo

Com esta pesquisa temos o potencial de beneficiar diversos grupos. Um dos principais beneficiados são os economistas e profissionais que atuam em órgãos reguladores e instituições financeiras. Esses especialistas, que possuem um profundo conhecimento em economia e finanças, utilizam tecnologias avançadas para analisar dados e prever tendências econômicas. Eles são fundamentais na formulação de políticas públicas e financeiras. Ao entender melhor como a Selic impacta o endividamento familiar, esses profissionais estarão melhor equipados para tomar decisões que garantam a estabilidade econômica e evitem crises financeiras.

Além disso, acadêmicos e pesquisadores nas áreas de economia e ciência da computação também se beneficiarão dessa pesquisa. Esses indivíduos, que estão explorando o uso de técnicas de aprendizado de máquina para a análise de dados macroeconômicos, encontram nesta investigação uma oportunidade de aprofundar seus estudos. Com uma sólida base teórica, mas ainda em processo de aplicação prática dessas novas tecnologias, esses acadêmicos ocupam posições como professores, pesquisadores e estudantes de pós-graduação. A pesquisa não só contribuirá para o avanço de suas carreiras, como também impulsionará o desenvolvimento de novos métodos de previsão econômica que podem transformar a forma como entendemos a economia.

Por ultimo e não menos importante, as famílias brasileiras, embora de forma indireta, são as beneficiadas principais desta pesquisa. Pois compreender como a variação da Selic influencia o endividamento pode capacitá-las a tomar decisões financeiras mais informadas, evitando o risco de endividamento excessivo. Essas famílias, muitas vezes com conhecimentos limitados em economia, podem não estar diretamente envolvidas no estudo, mas os resultados têm o potencial de resultar em políticas públicas que promovam sua saúde financeira. Dessa forma, a pesquisa pode contribuir significativamente para a qualidade de vida dessas famílias, ajudando a construir uma economia mais estável e sustentável para todos.


## Estado da arte

O aprendizado de máquina (comumente chamado de machine learning) é uma técnica de inteligência artificial (IA) baseada em matemática e estatística que, através da utilização de algoritmos, consegue extrair informações de dados brutos e os representa por meio de um modelo matemático. Este modelo, por sua vez, é usado para fazer inferências – ou predições – a partir de novos conjuntos de dados, estimulando os sistemas de IA a solucionar problemas de forma autônoma, aprendendo sobre eles e propondo uma saída. (GOMES, 2019; ESCOVEDO, 2020).

Tendo em vista o escopo do presente trabalho, buscamos literatura nas áreas de ciência da computação e de ciências econômicas que embasem a utilização de aprendizado de máquina na análise e previsão de dados macroeconômicos, como a taxa de juros e a inflação.  Alguns métodos de aprendizado de máquina já vêm sendo utilizados na previsão desses dados, como feito por Araújo e Gaglianone (2024) em relação aos índices de inflação no Brasil e por Souza Júnior (2021) na previsão da Estrutura a Termo da Taxa de Juros (ETTJ - a relação entre o retorno e o prazo de vencimento de instrumentos financeiros de renda fixa) brasileira. 

O trabalho de Araújo e Gaglianone (2024) conclui, entre outras descobertas, que, em horizontes mais curtos, as combinações de previsão são úteis, especialmente as que se baseiam no model confidence set e que em horizontes mais longos, métodos baseados em árvores, como o Random Forest e XGBoost, funcionam bem e dominam outros modelos em vários horizontes. Além disso, o boletim Focus e a inflação implícita também pertencem ao conjunto das principais previsões em muitos horizontes (para a inflação mensal, melhoram a qualidade do conjunto de informações usado como insumo nas combinações, enquanto para a inflação acumulada em 12 meses pertencem ao conjunto de melhores previsões em quase todos os horizontes).

Já em Souza Júnior (2021), os resultados da pesquisa - que buscou estimar qual o modelo de aprendizado de máquina mais adequado para a projeção da ETTJ brasileira - são de que não é possível determinar um modelo, para os dados brasileiros, que consistentemente produza menor erro de previsão que o Passeio Aleatório em todos os horizontes de projeção. O Passeio Aleatório (PA) é o modelo mais simples de aprendizado de máquina e é referência na literatura de projeção de curva de juros. Além disso, as análises indicaram que inclusão de mais variáveis macroeconômicas para o treinamento, como a inflação e o câmbio, não acarretou melhores resultados nas projeções de forma consistente.

A taxa de juros da economia brasileira também foi o objeto de análise por parte de Amaral et al. (2023) através da utilização de redes neurais recorrentes (RNA), que se trata de uma técnica de aprendizado máquina focada em identificar padrões em um banco de dados. Os resultados dessa pesquisa foram que os modelos com múltiplas camadas de entradas possuem maior aderência e geram precisões mais assertivas, em especial a LSTM (long short term memory) multivariante, usando  todas  nossas  variáveis  macroeconômicas  como  inputs  (Câmbio, Inflação, Selic, PIM e a variável que queremos prever acumulada no ano). Ou seja, os modelos de melhor desempenho foram o de tipo Multivariado  (com  Séries  de  Múltiplas  Entradas),  isto  é,  os que  possuem  os  quatro indicadores macroeconômicos (IPCA, SELIC, PIM - produto industrial mencial - e Câmbio), pois apresentaram o menor percentual de erro em todas as previsões realizadas nos testes. Como ressalva, cabe salientar que, de acordo com os autores, mesmo com a precisão matemática do modelo, a análise de outros indicadores jamais pode ser descartada, permanecendo imprescindível que as decisões sejam baseadas não apenas no modelo de aprendizado de máquina, mas também em conhecimentos técnicos do profissional da área, contexto histórico e a partir da observação de outros índices macroeconômicos.

Nesse sentido, nota-se que já há um volume de literatura que discuta a previsão de dados macroeconômicos através da IA, e que boa parte dessa literatura é recente, ressaltando que parte considerável dos algoritmos são usados para a previsão e não para entendimento de casualidade entre variáveis macroeconômicas, como é em grande parte o trabalho na econometria tradicional. (FREITAS, 2019). Assim, conclui-se que a economia, por ser um sistema complexo e interconectado, com uma infinidade de variáveis que influenciam umas às outras de maneiras não-lineares, pode ser mais bem compreendido à luz da IA e e do Machine Learning, permitindo previsões mais precisas e sofisticadas. (BARBOSA FILHO, 2024). 

  
# Descrição do _dataset_ selecionado

Para este projeto, foram selecionados três datasets principais que, em conjunto, permitem uma análise abrangente da relação entre a taxa Selic e o endividamento das famílias brasileiras, considerando também o impacto da inflação e do Índice de Confiança do Consumidor. <br>  

**Estatísticas Monetária e de Credito: Endividamento das Famílias**
Com esse dataset, podemos ter uma base direta para analisar o endividamento das famílias. Ele apresenta a relação entre o valor das dívidas e a renda das famílias, permitindo identificar como essa relação varia em função da taxa Selic.

**Índice de Confiança do Consumidor (ICC)**
O ICC nos ajuda a medir a percepção dos consumidores sobre a economia, que pode influenciar suas decisões de contrair novas dívidas ou liquidar as existentes. Um ICC alto pode indicar maior propensão ao endividamento, enquanto um ICC baixo pode indicar medo do endividamento.

**Inflação e variações do IPCA**
A inflação, medida pelo IPCA, afeta o poder de compra das famílias e, consequentemente, sua capacidade de pagar dívidas ou de assumir novas. Em períodos de alta inflação, a renda real das famílias diminui, o que pode aumentar o percentual de endividamento relativo à renda.


### Estatisticas Monetaria e de Credito: Endividamento das Famílias  

#### Links de acesso ao Dataset: 

https://www3.bcb.gov.br/sgspub/consultarmetadados/consultarMetadadosSeries.do?method=consultarMetadadosSeriesInternet&hdOidSerieSelecionada=29038  

https://dados.gov.br/dados/conjuntos-dados/29038-endividamento-das-familias-com-o-sistema-financeiro-nacional-exceto-credito-habitacional-  
<br>

#### Descrição: 

Este dataset apresenta uma série temporal mensal que mede a relação entre o valor atual das dívidas das famílias com o Sistema Financeiro Nacional e a renda acumulada das famílias nos últimos doze meses. Essa relação é expressa em percentual, permitindo acompanhar o peso das dívidas sobre a renda familiar ao longo do tempo.<br>

#### Atributos:

Campo: Periodo. Tipo: Date. Informa mes e ano de referencia<br>
Campo: Endividamento1/ - Total. Tipo: Decimal (18,2). Porcentagem do comprometimento total das famílias <br>
Campo: Endividamento1/ - Sem financiamento imobiliário. Tipo: Decimal (18,2) Porcentagem do comprometimento sem financiamento imobiliário <br>
Campo: Comprometimento de renda2/ - Dados dessazonalizados - Total. Tipo: Decimal (18,2) Porcentagem do comprometimento dessazonalizados total <br>
Campo: Comprometimento de renda2/ - Dados dessazonalizados - Sem financiamento imobiliário. Tipo: Decimal (18,2) Porcentagem do comprometimento dessazonalizados sem financiamento imobiliário<br>  

#### Data: 
MAI/2011 a MAI/2024<br>
Este dataset não apresenta valores faltantes.<br>

### Índice de Confiança do Consumidor (ICC)

#### Link de acesso: 

https://dados.gov.br/dados/conjuntos-dados/4393-indice-de-confianca-do-consumidor<br>

https://www3.bcb.gov.br/sgspub/consultarmetadados/consultarMetadadosSeries.do?method=consultarMetadadosSeriesInternet&hdOidSerieSelecionada=4393  
<br>

#### Descrição: 
O ICC é um indicador que acompanha as expectativas dos consumidores em relação à situação econômica atual e futura. Este dataset é crucial para entender como a confiança dos consumidores pode influenciar suas decisões de endividamento e consumo.  
O valor do índice de confiança do consumidor (ICC) indica o nível de confiança dos consumidores em relação à sua capacidade de compra e à situação do país. Um valor mais alto significa que os consumidores estão mais dispostos a consumir, enquanto um valor mais baixo indica que eles têm menos vontade de aquecer a economia. 
O ICC é calculado com base em uma escala que varia de 0 a 200 pontos, sendo que 0 representa pessimismo total e 200 otimismo total. 
O ICC é um indicador importante para a economia, pois ajuda a antecipar os rumos da economia a curto prazo. Para uma melhor compreensão dos índices, é importante acompanhar o desempenho de meses anteriores. 

#### Atributos:
<br>
Campo: Data. Tipo: Date. Informa mes e ano de referencia<br>
Campo: valor Formato: Decimal(18,02). Valor referente ao ICC que varia de 0 a 200<br>

#### Data: 
JUN/2011 a JUN/2024<br>
Este dataset não apresenta valores faltantes.<br>

### Inflação

#### Link de acesso: 

https://www.kaggle.com/datasets/fidelissauro/inflacao-brasil?resource=download

https://dados.gov.br/dados/conjuntos-dados/relatorios-de-inflacao-publicados
<br>

#### Descrição: 
O dataset de inflação inclui uma série temporal que mede as variações no Índice de Preços ao Consumidor Amplo (IPCA), utilizado para calcular a inflação no Brasil. A inflação afeta diretamente o poder de compra das famílias e, consequentemente, seu comportamento em relação ao crédito e ao endividamento.

#### Atributos:

Campo: Referencia. Tipo: Date. Informa mês e ano de referencia (yyyy-MM)<br>
Campo: ano. Tipo: String. Informa o ano de referencia no formato (yyyy)<br>
Campo: mes. Tipo: String. Informa o mes de referencia no formato (m)<br>
Campo: ano_mes. Tipo: Date.  Informa mes e ano de referencia(yyyyMM)<br>
Campo: ipca_variacao. Tipo: Decimal (18,2) Informa a variação do IPCA no mês de referência<br>
Campo: ipca_acumulado_ano. Tipo: Decimal (18,2) Informa a variação do IPCA acumulado para o ano<br>
Campo: ipca_acumulado_doze_meses. Tipo: Decimal (18,2) Informa a variação do IPCA acumulado nos últimos 12 meses<br>
Campo: inpc_variacao. Tipo: Decimal (18,2) Informa a variação do INPC no mês de referência<br>
Campo: inpc_acumulado_ano. Tipo: Decimal (18,2) Informa a variação do INPC acumulado para o ano<br>
Campo: inpc_acumulado_doze_meses. Tipo: Decimal (18,2) Informa a variação do INPC acumulado nos últimos 12 meses<br>
Campo: ipa_variacao. Tipo: Decimal (18,2) Informa a variação do IPA no mês de referência<br>
Campo: ipa_acumulado_ano. Tipo: Decimal (18,2) Informa a variação do IPA acumulado para o ano<br>
Campo: ipc_fipe_variacao. Tipo: Decimal (18,2) Informa a variação do IPC Fipe no mês de referência<br>
Campo: ipc_fipe_acumulado_ano. Tipo: Decimal (18,2) Informa a variação do IPC Fipe acumulado para o ano<br>
Campo: incc_variacao. Tipo: Decimal (18,2) Informa a variação do INCC Fipe no mês de referência<br>
Campo: incc_acumulado_ano. Tipo: Decimal (18,2) Informa a variação do INCC Fipe acumulado para o ano<br>
Campo: salario_minimo. Tipo: Decimal (18,2). Informa o salario mínimo referente ao mês e ano dos dados.<br>
Campo: consolidado_ano. Tipo: booleano (TRUE FALSE). Informa se a linha contém valores referentes ao último mês do ano.<br>

#### Data: 
MAI/2011 a MAI/23<br>
Atributos Faltantes: Este dataset não apresenta valores faltantes.<br>  

### Selic Anualizada

#### Link de acesso: 
[https://dadosabertos.bcb.gov.br/dataset/29263-sgs](https://dadosabertos.bcb.gov.br/dataset/1178-taxa-de-juros---selic-anualizada-base-252)

#### Descrição: 
O dataset inclui informações sobre a taxa selic anualizada, para todos os dias da série histórica.

#### Atributos:
Campo: data. Tipo: Date (dd/mm/yyyy). Informa dia, mês e ano de referência. <br>
Campo: valor. Tipo: Decimal (10,40). Informa a Selic anualizada definida na última reunião do COPOM anterior a data de referência. <br>

#### Data:
04/06/1986 a 20/08/2024<br>
Atributos Faltantes: Este dataset não apresenta valores faltantes<br>

# Canvas analítico 

![image](https://github.com/user-attachments/assets/e0ced4d1-44ee-4364-bf0f-faaaf12beb55)

![image](https://github.com/user-attachments/assets/5e77686e-f358-4df8-9aae-653860d1f862)



**REFERÊNCIAS**

> - AMARAL ET AL., **Previsão de variáveis econômicas com aprendizado de máquina: previsão com redes neurais**. Revista Observatorio De La Economia Latinoamericana. Curitiba, v.21, n.9, p. 11279-11299. 2023. Disponível em: https://ojs.observatoriolatinoamericano.com/ojs/index.php/olel/article/view/1394/861. Consulta em 25 ago. 2024.

> - ARAÚJO, Gustavo Silva; GAGLIANONE, Wagner Piazza. **Métodos de Aprendizado de Máquina para Previsão de Inflação no Brasil.** BC Blog, 26/03/2024. Disponível em: https://www.bcb.gov.br/noticiablogbc/10/noticia. Consulta em 25 ago. 2024.  

> - BANCO CENTRAL DO BRASIL **Endividamento das famílias com o Sistema Financeiro Nacional exceto crédito habitacional em relação à renda acumulada dos últimos 12 meses (RNDBF).** Disponível em: https://dados.gov.br/dados/conjuntos-dados/29038-endividamento-das-familias-com-o-sistema-financeiro-nacional-exceto-credito-habitacional-. Consulta em 27 set. 2024.  

> - BARBOSA FILHO, Luiz Henrique. **IA e Previsão Macroeconômica usando Python.** Análise Macro. 04/03/2024. Disponível em: https://analisemacro.com.br/economia/macroeconometria/ia-e-previsao-macroeconomica-usando-python/. Consulta em 25 ago. 2024.  

> - ESCOVEDO, Tatiana. **Machine Learning: Conceitos e Modelos — Parte I: Aprendizado Supervisionado.** 28/06/2020. Disponível em: https://tatianaesc.medium.com/machine-learning-conceitos-e-modelos-f0373bf4f445. Consulta em 25 ago. 2024.  

> - FREITAS, Gabriel Belmino. **O Uso De Machine Learning Na Modelagem Da Previsão De Inflação: Revisão Bibliográfica.** Universidade de Brasília. 2019. Disponível em: https://bdm.unb.br/bitstream/10483/25328/1/2019_GabrielBelminoFreitas_tcc.pdf. Consulta em 25 ago. 2024.  

> - GOMES, Pedro César Tebaldi. **Principais algoritmos de machine learning.** Data Geeks. 18/02/2019. Disponível em: https://www.datageeks.com.br/algoritmos-de-machine-learning/. Consulta em 25 ago. 2024.  

> - SOUZA JÚNIOR, Pedro Ivo Ferreira de. **Estrutura a termo da taxa de juros no Brasil: Projeções utilizando aprendizado de máquina.** Universidade de Brasília. 2021. Disponível em: http://icts.unb.br/jspui/bitstream/10482/41996/1/2021_PedroIvoFerreiradeSouzaJunior.pdf. Consulta em 25 ago. 2024.  
