# Introdução

*Texto descritivo introdutório apresentando a visão geral do projeto a ser desenvolvido considerando o contexto em que ele se insere, os objetivos gerais, a justificativa e o público-alvo do projeto.*

Em uma sociedade captalista, uma grande preocupação dos órgãos reguladores é manter as relações de consumo e oferta de recursos de forma sadia, protegendo o sistema financeiro de cenários de grande inadimplência, que, de forma exagerada, pode contribuir para a bancarrota financeira não só de empresas, mas de nações. Além das empresas, as famílias também podem contrair dívidas além das suas capacidades de pagamento, e, por isso, entender qual é o perfil de endividamento pode contribuir para manter este sistema financeiro operando de forma saudável, evitando que as famílias atinjam níveis de endividamento irreparáveis.<br>

Com esse projeto, buscamos analisar se existe uma relação entre a taxa Selic e o endividamento das famílias brasileiras, separando por categoria de linha de crédito, considerando também o impacto de fatores como a inflação e o Índice de Confiança do Consumidor.<br>

Devido a importancia do crédito no cotidiano das famílias, e sua influência direta na saúde financeira da população brasileira, é importante entender como o endividamento das famílias reage à políticas de facilitação de acesso ao crédito realizadas pelo Comitê de Política Monetária (COPOM), quando o mesmo reduz a taxa Selic, ou quando este mesmo comitê opta pela limitação de concessão de crédito, elevando esta taxa.<br>

O objetivo geral deste trabalho é identificar padrões e correlações que possam fornecer dados sobre como a variação na Selic impacta diferentes categorias do endividamento familiar. Entender estes padrões facilita o entendimento do nível de endividamento das famílias brasileiras e suas consequências sobre a economia, como a inadimplência e a retração do consumo.<br>

## Problema

*Nesta seção, você deve apresentar o problema que a sua investigação/experimentação busca resolver. Por exemplo, caso o _dataset_ selecionado, seja um _dataset_ que contenha uma série temporal com o preço de diversas ações da bolsa de valores, o problema pode estar relacionado a dificuldade em saber a melhor hora (hora certa??) de comprar ou então, de executar a venda de uma determinada ação.*
*Descreva ainda o contexto em que essa aplicação será usada, se houver: empresa parceira, tecnologias etc. Novamente, descreva apenas o que de fato existir, pois ainda não é a hora de apresentar requisitos  detalhados ou projetos.*

A principal questão que gostariamos de responde é "Com base na taxa Selic, é possível estimar o percentual de endividamento das famílias por categoria de crédito no Brasil?"

A partir desta pergunta, surge a necessidade de compreender como diferentes categorias de crédito, como crédito pessoal, consignado e imobiliário, reagem às oscilações da Selic, especialmente em contextos de alta inflação e mudanças no Índice de Confiança do Consumidor. O problema abordado é relevante porque as famílias enfrentam desafios ao tentar equilibrar suas finanças em um ambiente de taxas de juros variáveis, o que pode resultar em um endividamento excessivo ou insustentável.

Este projeto será desenvolvido a partir da análise de datasets que incluem dados da Selic, inflação, Índice de Confiança do Consumidor e dados de endividamento por categoria de crédito, com o foco acadêmico e analítico. 

> **Links Úteis**:
> - [Objetivos, Problema de pesquisa e Justificativa](https://medium.com/@versioparole/objetivos-problema-de-pesquisa-e-justificativa-c98c8233b9c3)
> - [Matriz Certezas, Suposições e Dúvidas](https://medium.com/educa%C3%A7%C3%A3o-fora-da-caixa/matriz-certezas-suposi%C3%A7%C3%B5es-e-d%C3%BAvidas-fa2263633655)
> - [Brainstorming](https://www.euax.com.br/2018/09/brainstorming/)

## Questão de pesquisa

*A questão de pesquisa é a base de todo o trabalho que será desenvolvido. É ela que motiva a realização da pesquisa e deverá ser adequada ao problema identificado. Ao término de sua pesquisa/experimentação, o objetivo é que seja encontrada a resposta da questão de pesquisa previamente definida.*

Pensamos que diante do cenário econômico brasileiro, marcado por oscilações frequentes na taxa Selic e variações nos índices de inflação surge a necessidade de entender como esses fatores afetam o comportamento financeiro das famílias e sua qualidade de vida. Portanto, a questão central que norteia nossa pesquisa é:

Como a variação da taxa Selic influencia o percentual de endividamento das famílias brasileiras por categoria de crédito, considerando também o impacto da inflação?

Pensamos que esta questão é fundamental para desvendar as relações entre política monetária e o endividamento familiar. Ao final da pesquisa, gostariamos de responder a essa questão, contribuindo para uma compreensão mais ampla do impacto das flutuações na vida das pessoas. 


> **Links Úteis**:
> - [Questão de pesquisa](https://www.enago.com.br/academy/how-to-develop-good-research-question-types-examples/)
> - [Problema de pesquisa](https://blog.even3.com.br/problema-de-pesquisa/)

## Objetivos preliminares

*Aqui você deve descrever os objetivos preliminares do trabalho indicando que o objetivo geral é experimentar modelos de aprendizado de máquina adequados para solucionar o problema apresentado acima.*
*Apresente também alguns (pelo menos 2) objetivos específicos dependendo de onde você vai querer concentrar a sua prática investigativa, ou como você vai aprofundar no seu trabalho.*
*Por exemplo: um objetivo específico pode estar relacionado a predizer a tendência de alta, estabilidade ou queda de uma determinada ação em uma determinada janela do tempo ou então, predizer o valor exato de uma determinada ação.*
*Lembre-se que, à medida que a pesquisa/experimentação evolui, os objetivos podem evoluir também, portanto, não se esqueça de fazer as atualizações necessárias.*

Como objetivos para esta pesquisa, buscamos:  
- Projetar o endividamento das famílias com base na taxa Selic e a inflação, a partir de dados históricos
- Com base nos dados de endividamento atuais, estimar qual deve ser o tipo de política financeira a ser adotada


> **Links Úteis**:
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)

## Justificativa

*Descreva a importância ou a motivação para trabalhar com o conjunto de dados escolhido. Indique as razões pelas quais você escolheu seus objetivos específicos, as razões para aprofundar o estudo do problema identificado e qual o impacto que tal problema provoca na sociedade. Lembre-se de quantificar (com dados reais e suas respectivas fontes) este impacto.*

Escolhemos trabalhar com os dados de Selic, inflação porque acreditamos que esses fatores estão intrinsecamente conectados na qualidade de vida das famílias. A análise desses dados permite não apenas entender as dinâmicas econômicas, mas também oferece valiosas ideias para a formulação de políticas públicas mais eficazes, capazes de proteger a saúde financeira das famílias.<br>
Dados do Banco Central do Brasil mostram que, em períodos de alta na taxa Selic, a tendência é que o custo do crédito aumente, o que pode impactar diretamente o nível de endividamento das famílias. Por outro lado, períodos de baixa na Selic podem incentivar o consumo, mas também elevar o risco de endividamento excessivo, especialmente em categorias de crédito de maior risco. Entender esses padrões é essencial para tentarmos prever os efeitos de futuras decisões financeiras.<br>
Em resumo, a motivação para este trabalho é mostrar como o endividamento das famílias esta ligado a politicas economicas e como podemos mitigar para promover uma economia mais saudável e sustentável.<br>

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)

## Público-Alvo

*Descreva quem serão as pessoas que poderão se beneficiar com a sua investigação indicando os diferentes perfis. O objetivo aqui não é definir quem serão os clientes ou quais serão os papéis dos usuários na aplicação. A ideia é, dentro do possível, conhecer um pouco mais sobre o perfil dos usuários: conhecimentos prévios, relação com a tecnologia, relações hierárquicas, etc.*
*Adicione informações sobre o público-alvo por meio de uma descrição textual, diagramas de personas e mapa de stakeholders.*

### Descrição Textual do Público-Alvo:

**1. Estudantes e Professores de Economia e Finanças:**
   - **Conhecimentos prévios:** Pessoas que estudam ou ensinam economia e finanças, com uma boa base teórica sobre como funcionam a taxa Selic, a inflação e o crédito.
   - **Relação com a tecnologia:** Estudantes geralmente têm mais facilidade com novas tecnologias e ferramentas de análise de dados, enquanto professores podem usar métodos mais tradicionais.
   - **Relações hierárquicas:** Estudantes estão em processo de aprendizado, enquanto professores guiam e orientam, além de desenvolverem conteúdos para as aulas.

**2. Analistas e Gestores de Políticas Públicas:**
   - **Conhecimentos prévios:** Profissionais que trabalham criando políticas econômicas e sociais, com um bom entendimento de como as decisões sobre a taxa Selic e outros indicadores econômicos afetam a vida das pessoas.
   - **Relação com a tecnologia:** Eles têm um conhecimento moderado em tecnologia, usando principalmente relatórios e planilhas para tomar decisões.
   - **Relações hierárquicas:** Costumam trabalhar em cargos intermediários ou superiores dentro do governo, auxiliando líderes na tomada de decisões que afetam o país.

**3. Profissionais do Mercado Financeiro:**
   - **Conhecimentos prévios:** Pessoas que trabalham com finanças, como gerentes de banco e analistas financeiros, que conhecem bem como a economia funciona e como as taxas de juros afetam os investimentos e o crédito.
   - **Relação com a tecnologia:** Alto, já que usam ferramentas avançadas de análise de dados e modelos para prever o comportamento do mercado e tomar decisões.
   - **Relações hierárquicas:** Geralmente ocupam posições de liderança em empresas financeiras e tomam decisões importantes sobre investimentos e riscos.

### Diagrama de Personas:

**1. Persona 1: Carlos, o Professor de Economia**
   - **Idade:** 45 anos
   - **Cargo:** Professor Universitário
   - **Tecnologia:** Usa ferramentas como planilhas e software para análises, mas não é um expert em programação.
   - **Necessidades:** Ferramentas que ajudem a explicar e entender como a economia do Brasil funciona.
   - **Objetivos:** Ensinar seus alunos e criar materiais didáticos que sejam claros e úteis.

**2. Persona 2: Fernanda, a Gestora de Políticas Públicas**
   - **Idade:** 38 anos
   - **Cargo:** Analista Sênior no Governo
   - **Tecnologia:** Usa principalmente Excel e relatórios para analisar dados.
   - **Necessidades:** Informações claras e diretas que ajudem a tomar decisões políticas.
   - **Objetivos:** Desenvolver políticas que ajudem a reduzir o endividamento das famílias brasileiras.

**3. Persona 3: João, o Analista Financeiro**
   - **Idade:** 30 anos
   - **Cargo:** Gestor de Riscos em um Banco
   - **Tecnologia:** Trabalha com ferramentas modernas de análise de dados e previsões financeiras.
   - **Necessidades:** Modelos que ajudem a prever o impacto das mudanças na Selic nos empréstimos e investimentos.
   - **Objetivos:** Minimizar riscos e aumentar os lucros para o banco e seus clientes.

### Mapa de Stakeholders:

- **Principais Interessados:**
  - **Estudantes e Professores de Economia e Finanças:** São diretamente impactados pelos resultados e métodos desenvolvidos, pois usarão esses dados para aprendizado e ensino.
  - **Analistas e Gestores de Políticas Públicas:** Precisam das análises para criar políticas que impactam a economia do país.

- **Secundários:**
  - **Profissionais do Mercado Financeiro:** Usam os resultados para tomar decisões estratégicas, mas não são o foco principal da pesquisa.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)

## Estado da arte

*Nesta seção, deverão ser descritas outras abordagens identificadas na literatura que foram utilizadas para resolver problemas similares ao problema em questão. Para isso, faça uma pesquisa detalhada e identifique, no mínimo, 5 trabalhos que tenham utilizado dados em contexto similares e então: (a) detalhe e contextualize o problema, (b) descreva as principais características do _dataset_ utilizado, (c) detalhe quais abordagens/algoritmos foram utilizados (e seus parâmetros), (d) identifique as métricas de avaliação empregadas, e (e) fale sobre os resultados obtidos.*  

O aprendizado de máquina (*machine learning*) é uma técnica de inteligência artificial (IA) baseada em matemática e estatística que, através da utilização de algoritmos, é capaz de extrair informações de dados brutos e os representa por meio de um modelo matemático. Este modelo, por sua vez, é utilizado para fazer inferências – ou predições – a partir de novos conjuntos de dados, estimulando os sistemas de IA a solucionar problemas de forma autônoma, aprendendo sobre eles e propondo uma saída. (GOMES, 2019; ESCOVEDO, 2020).  

Tendo em vista o escopo do presente trabalho, buscamos literatura nas áreas de ciência da computação e de ciências econômicas que embasem a utilização de aprendizado de máquina para a análise de dados macroeconômicos, como a taxa de juros e a inflação, permitindo a previsão de cenários a partir de dados históricos. Com base em algumas pesquisas realizadas, evidenciamos a utilização de métodos de aprendizado de máquina sendo utilizados na previsão desses cenários, como feito por Araújo e Gaglianone (2024) em relação aos índices de inflação no Brasil e por Souza Júnior (2021) na previsão da Estrutura a Termo da Taxa de Juros Brasileira*(a relação entre o retorno e o prazo de vencimento de instrumentos financeiros de renda fixa)*. A taxa de juros da economia brasileira também foi o objeto de análise por parte de Amaral et al. (2023) através da utilização de redes neurais recorrentes (RNA), que se trata de uma técnica de aprendizado máquina focada em identificar padrões em um banco de dados.  

Nesse sentido, nota-se que já há um volume de pesquisas que discutem a previsão de dados macroeconômicos através da IA, e que boa parte dessa literatura é recente, tendo em vista que também é um tema relativamente novo no mercado, ressaltando que parte considerável dos algoritmos são usados para a previsão e não para entendimento de casualidade entre variáveis macroeconômicas, como é em grande parte o trabalho na econometria tradicional (FREITAS, 2019). Assim, por a economia ser um sistema complexo e interconectado, com uma infinidade de variáveis que influenciam umas às outras de maneiras não-lineares, pode ser melhor compreendido com a utilização de IA e do *Machine Learning*, permitindo previsões mais precisas e sofisticadas (BARBOSA FILHO, 2024).  

**REFERÊNCIAS**  

> - AMARAEL ET AL., **Previsão de variáveis econômicas com aprendizado de máquina: previsão com redes neurais.** Revista Observatorio De La Economia Latinoamericana. Curitiba, v.21, n.9, p. 11279-11299. 2023. Disponível em: file:///C:/Users/vinin/Downloads/OBSERVATORIO042.pdf. Consulta em 25 ago. 2024.  

> - ARAÚJO, Gustavo Silva; GAGLIANONE, Wagner Piazza. **Métodos de Aprendizado de Máquina para Previsão de Inflação no Brasil.** BC Blog, 26/03/2024. Disponível em: https://www.bcb.gov.br/noticiablogbc/10/noticia. Consulta em 25 ago. 2024.  

> - BARBOSA FILHO, Luiz Henrique. **IA e Previsão Macroeconômica usando Python.** Análise Macro. 04/03/2024. Disponível em: https://analisemacro.com.br/economia/macroeconometria/ia-e-previsao-macroeconomica-usando-python/. Consulta em 25 ago. 2024.  

> - ESCOVEDO, Tatiana. **Machine Learning: Conceitos e Modelos — Parte I: Aprendizado Supervisionado.** 28/06/2020. Disponível em: https://tatianaesc.medium.com/machine-learning-conceitos-e-modelos-f0373bf4f445. Consulta em 25 ago. 2024.  

> - FREITAS, Gabriel Belmino. **O Uso De Machine Learning Na Modelagem Da Previsão De Inflação: Revisão Bibliográfica.** Universidade de Brasília. 2019. Disponível em: https://bdm.unb.br/bitstream/10483/25328/1/2019_GabrielBelminoFreitas_tcc.pdf. Consulta em 25 ago. 2024.  

> - GOMES, Pedro César Tebaldi. **Principais algoritmos de machine learning.** Data Geeks. 18/02/2019. Disponível em: https://www.datageeks.com.br/algoritmos-de-machine-learning/. Consulta em 25 ago. 2024.  

> - SOUZA JÚNIOR, Pedro Ivo Ferreira de. **Estrutura a termo da taxa de juros no Brasil: Projeções utilizando aprendizado de máquina.** Universidade de Brasília. 2021. Disponível em: http://icts.unb.br/jspui/bitstream/10482/41996/1/2021_PedroIvoFerreiradeSouzaJunior.pdf. Consulta em 25 ago. 2024.  

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

# Descrição do _dataset_ selecionado

*Nesta seção, você deverá descrever detalhadamente o _dataset_ selecionado. Lembre-se de informar o link de acesso a ele, bem como, de descrever cada um dos seus atributos (a que se refere, tipo do atributo etc.), se existem atributos faltantes etc.*<br>

Para este projeto, foram selecionados quatro datasets principais que, em conjunto, permitem uma análise abrangente da relação entre a taxa Selic e o endividamento das famílias brasileiras, considerando também o impacto da inflação e do Índice de Confiança do Consumidor. <br>

Endividamento das Famílias

Links de acesso: 

https://www3.bcb.gov.br/sgspub/consultarmetadados/consultarMetadadosSeries.do?method=consultarMetadadosSeriesInternet&hdOidSerieSelecionada=29038


https://dados.gov.br/dados/conjuntos-dados/29038-endividamento-das-familias-com-o-sistema-financeiro-nacional-exceto-credito-habitacional-
<br>

Descrição: Este dataset apresenta uma série temporal mensal que mede a relação entre o valor atual das dívidas das famílias com o Sistema Financeiro Nacional e a renda acumulada das famílias nos últimos doze meses. Essa relação é expressa em percentual, permitindo acompanhar o peso das dívidas sobre a renda familiar ao longo do tempo.<br>
Atributos:

Periodo: date<br>
Endividamento1/ - Total: Decimal (18,2)<br>
Endividamento1/ - Sem financiamento imobiliário: Decimal (18,2)<br>
Comprometimento de renda2/ - Dados dessazonalizados - Total: Decimal (18,2)<br>
Comprometimento de renda2/ - Dados dessazonalizados - Sem financiamento imobiliário: Decimal (18,2)

<br>
Data: MAI/2011 a MAI/2024<br>
Percentual de Endividamento: Percentual que representa a relação entre a dívida total das famílias e sua renda acumulada nos últimos doze meses .<br>
Este dataset não apresenta valores faltantes.<br>

Índice de Confiança do Consumidor (ICC)
<br>
Link de acesso: <br>

https://dados.gov.br/dados/conjuntos-dados/4393-indice-de-confianca-do-consumidor<br>

https://www3.bcb.gov.br/sgspub/consultarmetadados/consultarMetadadosSeries.do?method=consultarMetadadosSeriesInternet&hdOidSerieSelecionada=4393
<br>
Descrição: O ICC é um indicador que acompanha as expectativas dos consumidores em relação à situação econômica atual e futura. Este dataset é crucial para entender como a confiança dos consumidores pode influenciar suas decisões de endividamento e consumo.<br>
Atributos:
<br>
Campo: data Formato: Date<br>
Campo: valor Formato: Decimal(18,02)
<br>
Data: JUN/2011 a JUN/2024<br>
Este dataset não apresenta valores faltantes.<br>

Inflação
<br>
Link de acesso: 


https://www.kaggle.com/datasets/fidelissauro/inflacao-brasil?resource=download

https://dados.gov.br/dados/conjuntos-dados/relatorios-de-inflacao-publicados
<br>
Descrição: O dataset de inflação inclui uma série temporal que mede as variações no Índice de Preços ao Consumidor Amplo (IPCA), utilizado para calcular a inflação no Brasil. A inflação afeta diretamente o poder de compra das famílias e, consequentemente, seu comportamento em relação ao crédito e ao endividamento.
<br>
Atributos:<br>

referencia: Date<br>
ano: String<br>
mes: String<br>
ano_mes: String<br>
ipca_variacao: Decimal (18,2)<br>
ipca_acumulado_ano: Decimal (18,2)<br>
ipca_acumulado_doze_meses: Decimal (18,2)<br>
inpc_variacao: Decimal (18,2)<br>
inpc_acumulado_ano: Decimal (18,2)<br>
inpc_acumulado_doze_meses: Decimal (18,2)<br>
ipa_variacao: Decimal (18,2)<br>
ipa_acumulado_ano: Decimal (18,2)<br>
ipc_fipe_variacao: Decimal (18,2)<br>
ipc_fipe_acumulado_ano: Decimal (18,2)<br>
incc_variacao: Decimal (18,2)<br>
incc_acumulado_ano: Decimal (18,2)<br>
salario_minimo: Decimal (18,2)<br>

<br>
Data: MAI/2011 a MAI/23<br>
Atributos Faltantes: Este dataset não apresenta valores faltantes.<br>

# Canvas analítico

*Nesta seção, você deverá estruturar o seu Canvas Analítico. O Canvas Analítico tem o papel de registrar a organização das ideias e apresentar o modelo de negócio. O Canvas Analítico deverá ser preenchido integralmente mesmo que você não tenha "tantas certezas".*

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Referências

*Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.*

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
