# Resumo do Projeto

O desenvolvimento deste projeto foi bem desafiador, em vários aspectos. Inicialmente, precisávamos entender conceitos de estatística a fim de não apenas executar modelos prontos, mas também entender como funcionavam as etapas utilizadas peo mesmo. A ciência de dados não consiste apenas em aplicar modelos prontos, e sim de entender como dados brutos podem virar informações valiosas para gestores e até mesmo a população em geral.  

Além disso, foi necessário entender sobre a linguagem Python, que, apesar de ser uma linguagem com sintaxe bem simplificada, ainda sim representava um novo aprendizado, o que se mostra desafiador por si só.  

A aplicação dos modelos exigiu bastante também, uma vez que, além dos conhecimentos estatísticos e da linguagem a ser utilizada, bem como o conhecimento sobre o tratamento dos dados, entender sobre o tema a qual os dados se referiam ajudou a nossa análise para estabelecer correlações entre atributos diferentes dentro da nossa base. Perguntas como "qual a relação da inflação (IPCA) com a Selic?", ou "como o endividamento das famílias se comportaria com um aumento na inflação, por exemplo?" só seria possível de entender a partir do conhecimento também sobre o "negócio".  

O que se mostrou bastante evidente durante o desenvolvimento do projeto, até mesmo como uma regra para a ciência de dados, não apenas conhecer a tecnologia não é suficiente, sem o conhecimento do assunto não é possível realizar análise que realmente vão gerar valor para o público alvo do desenvolvimento dos software.

# Implantação da solução

A importância de poder prever o nível de endividamento das famílias brasileiras nos próximos anos vem do fato que isso nos ajuda a entender melhor a saúde financeira dessas famílias e os impactos disso na economia nacional. Utilizando dados históricos das taxas SELIC e de Inflação e do índice de Confiança do Consumidor conseguimos fazer algumas previsões do comportamento dos níveis de endividamento futuros. Essas previsões podem auxiliar na criação de políticas públicas, na gestão de riscos por instituições financeiras e no planejamento das próprias famílias.

Com base no tema, desenvolvemos um sistema que utiliza técnicas de machine learning para prever os níveis de endividamento das famílias brasileiras. Esse sistema foi treinado com os dados históricos começando em 2011 e é fundamental para compreender os fatores que influenciam o comportamento financeiro das famílias.

A principal funcionalidade do sistema é projetar os níveis de endividamento nos próximos meses e anos, permitindo identificar possíveis tendências ou alertas precoces sobre cenários de risco. Essa capacidade de identificar tendências pode ser fundamental na elaboração de políticas públicas e na adequação de estratégias entre as autoridades monetárias e fiscais do País. Além disso, essas previsões podem ser utilizadas pelos consumidores para auxiliar em um melhor planejamento de suas finanças com o objetivo de contribuir para um ambiente econômico mais equilibrado.

## Política

Para que o sistema proposto gere o valor para qual foi desenvolvido, é necessário o estabelecimento de uma política para aquilo que ele se propõe a entrega.
O sistema, para que realize predições sobre os indicadores referentes ao Endividamento das famílias brasilieiras, utilizará de uma base de dados pré estabelecida (janeiro de 2010 a maio de 2024), juntamente com o período que será designado pelo usuário a partir do campo disponível para tal. O período para qual o modelo irá trazer a previsão dos indicadores (entre as opoções 12, 24 e 36 meses), esta limitação que será imposta tem como objetivo salvar recursos do servidor que irá processar as requisições e também, para não gerar dados fora da realidade, uma vez que quanto maior o prazo estabelecido para a predição, menor é a capacidade de acerto dos modelos, exemplificada pela taxa de confiança.

Com a junção destas informações, os modelos serão executados, e com base no indicador “R2” (erro quadrático), os modelos serão ranqueados para que o sistema demonstre o modelo com maior probabilidade de acerto ao usuário.

## Máquina Virtual

![img 1](https://github.com/user-attachments/assets/dca358ab-857e-4558-b643-00bedb6d240b)

Para hospedar nossa máquina virtual escolhemos o Azure, pois ele poderia nos fornecer as ferramentas necessárias para executar o trabalho.  
O nome que escolhemos foi JurosRegressao a localização do servidor é no brasil e o ID da máquina é o: “ID da VM: e1c6e3c7-a4c9-4758-b418-7c77d49f1f37”.  
Na questão do hardware escolhemos na azure a versão “Standard_DS1_v2”. Com sistema operacional Windows, onde foi utilizada a imagem “WindownsServer 2019 Versão: latest (17763.6532.241101) . PAra o disco foi utilizado um de 127 GB.

![img 2](https://github.com/user-attachments/assets/ae1d671a-d646-4dbe-818b-06b52a53e9e4)

## Configurações de Rede

![img 3](https://github.com/user-attachments/assets/85855475-56e3-4552-82ba-454cc6acb11d)

Para configurar a rede da máquina virtual, escolhemos o Azure pois o mesmo oferece as ferramentas necessárias para garantir a segurança e o acesso à máquina. O nome da interface de rede é jurosregressao731_z1.
O endereço IP público utilizado é 20.195.168.9, enquanto o endereço IP privado da rede é 10.0.0.4. A rede está configurada na sub-rede padrão de JurosRegressao-vnet.
Regras de segurança da rede
O grupo de segurança configurado foi o JurosRegressao-nsg, que possui as seguintes regras principais para portas de entrada:
Prioridade: 200
Porta: 5000
Protocolo: TCP
Origem: Qualquer
Destino: Qualquer
Ação: Permitir
Prioridade: 300
Porta: 22
Protocolo: TCP
Origem: Qualquer
Destino: Qualquer
Ação: Permitir
Observação: Utilizada para acesso SSH.
Por padrão, o acesso de saída é irrestrito (permitido para qualquer destino o que possibilita o acesso as APIs).

![img4](https://github.com/user-attachments/assets/8f06e20d-4fe5-4ff9-b5c5-ff9f7ecd531c)

## API

Nossa API foi desenvolvida utilizando o Flask, um framework Python, ideal para a construção de aplicações web e APIs RESTful. A escolha pelo Flask foi baseada em sua simplicidade e flexibilidade, o que nos permitiu integrar os recursos necessários para atender aos requisitos do projeto. Com relação aos modelos, eles foram adaptados para o retorno das apis.

Configuração da API

A API foi hospedada na máquina virtual JurosRegressao, garantindo escalabilidade e segurança. O servidor Flask foi configurado para escutar a porta 5000, conforme as regras de segurança definidas no grupo de segurança de rede do Azure.

Os principais endpoints da API foram projetados para facilitar a comunicação entre o frontend e o backend. 

![img4](https://github.com/user-attachments/assets/83de4578-ad46-4f4e-bc93-f6540cc4ab69)

Para o funcionamento da API, instalamos as bibliotecas necessárias diretamente na máquina virtual, utilizando o gerenciador de pacotes pip. Algumas das dependências principais incluem:

Flask
Pandas
Scikit-learn (para a integração com os modelos de aprendizado de máquina)
Flask-CORS (para habilitar o acesso da API por diferentes origens)

O teste da API foi realizado através de ferramentas como Postman e cURL, simulando os acessos que ocorreriam em produção. A API está acessível pelo endereço público da máquina virtual, utilizando o IP público e a porta 5000.

![img 6](https://github.com/user-attachments/assets/103ebb32-e871-460f-a149-c9319caad399)

o código da api e instância está na pasta SRC

## Frontend

O frontend foi desenvolvido para oferecer uma interface simples e funcional, priorizando a clareza na apresentação dos dados e a facilidade de uso. Decidimos utilizar HTML5, CSS3 e JavaScript

![img6 5](https://github.com/user-attachments/assets/8d4fb70f-8b59-45bc-958a-ff7428385589)

A estrutura do frontend é composta por um único arquivo HTML que organiza as seções e interage com a API via JavaScript. Ele está hospedado na mesma máquina virtual que a API, e o acesso é feito através de um servidor web Apache, configurado para servir o frontend na porta padrão 8000.
Toda comunicação entre o frontend e o backend acontece via requisições AJAX, realizadas com fetch() em JavaScript. Foi configurado o CORS no Flask para permitir o consumo da API a partir do domínio do frontend.
Para testar e hospedar, utilizamos o endereço IP público da máquina virtual e configuramos o Apache para servir o frontend na URL(http://20.195.168.9). Assim, o usuário pode acessar o frontend diretamente.

![img 7](https://github.com/user-attachments/assets/06d727ac-2f28-4f9b-8035-ebebb2e3d1e5)

## Testes de carga e stress

Os testes de carga e stress são usados para avliar o desempenho e a estabilidade de um sistema, eles simulam condições específicas de uso para identificar limites, gargalos e possíveis falhas, sendo:
Teste de carga  - Avalia o desempenho da VM sob carga realista ex. quantos usuários simultâneos  o sistema pode suportar antes da degradação.
Teste de stress - Exceder os limites normais para verificar a estabilidade. ex. forçar uso de CPU, memória, ou disco acima da capacidade esperada.
Segue abaixo a a aplicação dos testes.

Optamos pelo Apache JMeter para simular a carga e stress na API. A ferramenta foi configurada em uma máquina local e direcionada ao IP público da VM com o monitoramento do Azure monitor.  
Para o teste de Carga simulei 50, 100 e 200 usuários simultâneos enviando requisições para o endpoint. Onde cada usuário realizou 20 requisições consecutivas com diferentes combinações de dados de entrada.  
Para o teste de stress simulei um aumento progressivo de usuários, começando com 50 e subindo até 500 em intervalos de 1 minuto onde monitoramos o tempo de resposta da API e o número de requisições que resultaram em erro (códigos 5xx).
Os resultados foram que durante os testes, acompanhamos as métricas em tempo real através do Azure Monitor. Alguns dos comportamentos observados foram. A CPU chegou a picos de 90% durante o teste de stress com 500 usuários simultâneos, mas a memória se manteve estável, sem atingir 75%. Quanto à latência da API ela aumentou progressivamente com a carga, mas se manteve dentro de um tempo aceitável (500ms em média).  
A conclusão foi que a simulação demonstrou que a VM consegue lidar bem com cargas moderadas, mas apresenta gargalos em cenários de stress extremo. Para situações de maior demanda, poderia ser necessário aumentar os recursos alocados ou configurar um balanceador de carga para distribuir as requisições em mais instâncias.

![img 8](https://github.com/user-attachments/assets/64e77c00-443b-43a7-bd2f-b88276f419c7)

# Apresentação da solução

Nesta seção, um vídeo de, no máximo, 5 minutos onde deverá ser descrito o escopo todo do projeto, um resumo do trabalho desenvolvido, incluindo a comprovação de que a implantação foi realizada e, as conclusões alcançadas.

##  Vídeo

Segue o link para o vídeo da solução 

Link: https://www.youtube.com/watch?v=vz1am5Su-l8
