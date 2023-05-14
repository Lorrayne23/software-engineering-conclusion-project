<div align="justify">
  
# Análise da relação entre *code smells* e métricas qualitativas em repositórios de Sistemas de direção autônoma

## Alunos integrantes da equipe

* Lorrayne Reis Silva

## Orientadores

* Jose Laerte Pires Xavier Junior (TCCI)
* Cleiton Silva Tavares (TCCI)
* Simone de Assis Alves da Silva (TCCI)
* Johnatan Alves De Oliveira (TCCII)

## Introdução

1. A área da Engenharia de Software tratada neste trabalho é qualidade de *software*.
1. O problema a ser resolvido se pontua na escassez informacional da qualidade de repositórios de *softwares* *open source* simuladores na promoção de *code smells*, que podem ocasionar em simulações de baixa confiabilidade.
1.Resolver o problema desse trabalho é importante, pois outras abordagens da literatura não apontam a necessidade atencional da relação entre a *softwares* ADSs *open source* e a qualidade do código na promoção de *code smells* que podem contribuir para simulações falhas no desenvolvimento de AVs. 
1. O objetivo geral do trabalho visa identificar o relacionamento entre atributos de qualidade de *softwares* simuladores *open source ADSs* na ocorrência de *code smells*.
1. Os *três* objetivos específicos deste trabalho são : 1) Classificação de code smells frequentes em repositórios simuladores de ADSs, 2) Relação entre métricas qualitativas e a ocorrência de code smells classificados 3) Comparação e correlação da tendência quantitativa  de *code smells* de acordo com a presença ou não de *releases* nestes repositórios.

## Fundamentação Teórica

1. O conceito/teoria principal associado a este trabalho é qualidade de *software* . A sua definição neste trabalho  é conforme definido no trabalho: 
a qualidade de software se estabelece não somente nos problemas que esse tange resolver, mas em seu modo ocorrente de execução, estruturação e de organização. Tais características se refletem nos atributos de um *software denominados*: não funcionais ou de qualidade. Os mesmos, são responsáveis por promulgar propriedades determinísticas para a atuação de um *software* como manutenibilidade, confiança e eficiência. Não obstante, existem diversos estudos que proclamam a qualidade apresentada por um software como fator declarativo na criação de relações de dependência que podem fomentar a difusão de *bugs*.Pelos autores : Ian Sommerville,Chen et al.
3. O conceito/teoria secundário associado a este trabalho é análise etática de *software* .A sua definição neste trabalho é conforme definido no trabalho:Análises estáticas em software se referem a uma avaliação em código fonte estático com o intuito de checar à existência de possíveis padrões errôneos, violações de programação e a identificação de inverídicos paradigmas de qualidade em código. Os resultados apresentados por essas, podem apregoar o relacionamento direto na qualidade externa demonstrada pelo software. Outrossim, tais análises apontam a comunicação verídica de dados qualitativos no consumo de recursos usados em programas .Por fim, são altamente recomendadas pela ISO 26262/2011 para reduzir bugs em tempos de execução, pertencente ao seguimento de padrões de segurança automotiva no desenvolvimento de software.Pelos autores: Plosch et al.,Ligian et al.,Imparato et al.
4. O conceito/teoria terciário associado a este trabalho é code smells. A sua definição neste trabalho é conforme definido no trabalho:Code smells definem implentações ou escolhas  de design realizados negativamente que impactam a evolução de softwares,contribuindo para reduzir a capacidade de programadores no manetenimento de aplicações.Esses,apontam problemas com a qualidade do desenvolvimento e concomitantemente contribuem para a identificação de possíveis erros, além da promoção do realizamento de refatoração por parte de uma equipe técnica.A partir da identificação de code smells e seu tratamento, é possível promover o aumento da qualidade do software,torna-lo mais fácil de manter e reduzir as chances de falhas em uma sistema. Hamid et al.,Sharma et al.,Seema et al.
6.  O conceito/teoria terciário associado a este trabalho é sistemas de direção autônoma.A sua definição neste trabalho é conforme definido:são sistemas complexos que possuem segurança crítica diretamente relacionados ao atendimento de requisitos pré-estabelecidos. Esta ocorrência pressupõe do recebimento de dados de vários sensores, que são analisados em tempo real por meio de redes neurais profundas . As mesmas são responsáveis por determinar parâmetros para o acionamento de atuadores de execução.Logo,os softwares desses sistemas são de fundamental importancia para operação e sua composição decorre de várias unidades de componentes, que automatizam tarefas de direções específicas. Consequentemente, estão envolvidos diretamente na atuação e execução total de funcionamento, com a solicitação de recursos sendo realiza continuamente ao longo do tempo, além da promoção de abertura e recebimento de dados de componentes advindos de outras camadas.Pelos autores: Luo et al. , Stucco et al. ,  Ben et al.

## Trabalhos Relacionados

1. O trabalho mais relacionado é *An Are Code Smell Co-occurrences Harmful to Internal Quality Attributes? A Mixed-Method Study*, publicado no ano 2020 , por que apresenta a relação existente entre *code smells* e atributos internos de qualidade por meio de métricas e com embasamento teórico.
1. O segundo trabalho mais relacionado é *A Comprehensive Study of Autonomous Vehicle Bugs*, publicado no ano 2020,  por que criam uma taxonomia de *bugs* recorrentes que afetam diretamente  *softwares* semelhantes aos almejados para investigação.
1. O terceiro trabalho mais relacionado é *Detecting Code Smells in Python Programs*, publicado no ano 2016, por que  promove a detecção de *code smells* e realizam  a classificação dos tipos que possuem maior ocorrência em sistemas dessa linguagem, por meio da ferramenta de detecção de *code smells* denominada *Pysmell*.
## Materiais e Métodos

1. O tipo de pesquisa adotado neste trabalho é  quantitativa com viés descritivo, tal embasamento pode ser justificado dado a intenção desse em compreender o relacionamento existente entre atributos qualitativos de softwares ADSs e a presença de code smells por meio da análise de dados obtidos através da mineração de repositórios no *Github*.
1. Os materiais utilizados neste trabalho são : *API GraphQL* do *Github*, *API REST* do *GitHub*, *PowerBI*, bibliotecas *multimetric* e *Radon* do *Python*.
1. Os métodos empregados neste trabalho são correlações de *Pearson*. 
1. As métricas de avaliação são métricas relacionadas a aplicações de *Halstead* como *Number of delivered bugs according to Halstead* e  *LOC*, *comment lines*, *blank lines* , *Cyclomatic Complexity*, entre outas.
1. As etapa de execução do trabalho são : 1) Coleta de repositórios, 2) Coleta de *releases*, 3) Aferimento de *code smells* e métricas e 4) Análise de resultados.
<div>
