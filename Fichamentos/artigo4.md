<div align="justify"> 

# A Comprehensive Study of Autonomous Vehicle Bugs

J. Garcia, Y. Feng, J. Shen, S. Almanee, Y. Xia and Q. A. Chen, "A Comprehensive Study of Autonomous Vehicle Bugs," 2020 IEEE/ACM 42nd International Conference on Software Engineering (ICSE), 2020, pp. 385-396. doi: [10.1145/3377811.3380397](https://doi.org/10.1145/3377811.3380397)


## 1. Fichamento de Conteúdo

Veículos autônomos(AVs, do inglês *Autonomous Vehicles*) se ambientam e conquistam cada vez mais lugar perante a sociedade, com diversas corporações de alto patamar como *Uber* e *Google* focalizando a importância do desenvolvimento de projetos que se atrelam a evolução e utilização dessa propulsão. Para que os veículos posam estar em atividade perante o meio, uma série de fatores devem ser obedecidos durante sua criação através do seguimento sistemático de regras de segurança e conformidade pré-estabelecidas. Logo, dado que o desenvolvimento de tais requerimentos e o funcionamento desses ocorre pelo conjunto união entre *software* e componentes físicos, o problema se estabelece em relação à fragilidade de alguns softwares em seu modo atuante, tais sistemas quando executados causam falhas de operação possivelmente geradas por *bugs* e que consequentemente levam a acidentes graves de trânsito. Assim, por meio uma investigação realizada em *commits* de repositório *open source* em relação a erros encontrados, posteriormente a classificação desses conforme ocorrência de operação que afetam componentes diretos do *software*, é proposto um guia de monitoramento para direcionamento, localização e reparo. Como resultado, obtém-se uma classificação de erros recorrentes que afetam diretamente a ação de softwares, com a identificação de 13 causas principais e 20 consequências geradas através de 499 bugs encontrados.

## 2. Fichamento Bibliográfico 

* _Root causes_ (causas raiz) lista de classificação principal de erros cometidos por desenvolvedores (página 387).
* _Symptoms of AV bugs_ (sintomas de erros de *AV*) classificação de "sintomas" referentes a erros que ocorrem quando uma execução de *AV* esperada falha (página 388).
* _Other category_ (outra categoria) grupo de erros os quais não foram encontrados dados suficientes para classificação (página 394).


## 3. Fichamento de Citações 

* _"In this work, we focus on L4 AV systems since they have the highest autonomy level among the AVs in production today and thus their software bugs and defects have the highest importance in terms of safety and robustness."_
* _"If any tags or title of a pull request contain at least one key- word, we identify it as a bug-fix pull request. This process resulted in 336 and 430 merged pull requests for Apollo and Autoware that meet the criteria, respectively."_
* _" This result indicates that configuring, compiling, ensuring compatibility, and enabling instal- lations of AV systems is highly challenging and deserves greater attention by the software-engineering research community."_
* _"Apollo’s bugs exhibit significantly more of these types of symptoms. However, this does not necessarily indicate that Apollo has more driving bugs than Autoware. Apollo developers may focus more on identifying and fixing these kinds of bugs than Autoware developers."_
* _"Given that many lines of code (i.e., 104 lines of code on average) often need to be added or modified to fix AV bugs arising due to incorrect algorithm implementations, a wide variety of AV-specific and safety-critical bugs are likely to be inapplicable for state-of-the-art fault localization and automatic program-repair techniques ."_
* _"Crash bugs occur throughout critical AV components—especially Perception, Localization, and Planning— making them susceptible to more dangerous secondary effects."_
* _"When issues, pull requests, or code were insufficient for facilitat- ing classification into a particular category, we assigned the corre- sponding bug to the OT (Other) category."_

<div>