<div align="justify">

# An Are Code Smell Co-occurrences Harmful to Internal Quality Attributes? A Mixed-Method Study

Júlio Martins, Carla Bezerra, Anderson Uchôa, and Alessandro Garcia. 2020. Are Code Smell Co-occurrences Harmful to Internal Quality Attributes? A Mixed-Method Study. In Proceedings of the XXXIV Brazilian Symposium on Software Engineering (SBES '20). Association for Computing Machinery, New York, NY, USA, 52–61.  doi: [10.1145/3422392.3422419](https://doi.org/10.1145/3422392.3422419)



## 1. Fichamento de Conteúdo

 Por meio da prerrogativa de *code smells* como atuadores diretos no que tange a evolução e manutenção de *softwares*, uma vez que esses podem apontar fatores como a qualidade do código desenvolvido, conjuntamente ao questionamento sobre sua função percussora degradante em um sistema. O artigo aponta uma visão relacional da promoção da qualidade de *software* conforme a ocorrência conjunta de dois ou mais *code smells*. A partir de tal enfoque, a problemática do mesmo se instaura com base na escassez de aferições concretas do impacto da realização de *refactoring* sobre *code smells* em *softwares* com dominância positiva ou negativa, atreladamente ao aferimento de atributos de qualidade como: coesão, acoplamento, herança e complexidade. Logo, aborda esse questionamento por meio de um experimento empírico sobre a co-ocorrência de *code smells* em três sistemas *closed source* através da análise de 11 realeases. Para tal subjunção, realiza a verificação primeiramente de *code smells* individuais e posteriormente válida a maior ocorrência de *code smells* correlacionados. Não obstante, realizam medições a despeito dos atributos de qualidade presentes, performam *refactoring* dos conjuntos mais encontrados por meio da prerrogativa de *bord count technique* e executam novamente uma aferição de valores de qualidade no intuito de apontar disparidades entre os sistemas antes e depois da realização de *refactoring*. Como resultados, promulgam a co-oconcorrência de dois *code smells* de modo direto, os denominados *God Class–Long Method* e *Disperse Coupling–Long Method*. Ademais, a resolução de que a remoção de alguns *code smells* podem estar diretamente atrelados a redução da complexidade do sistema, entretato é pontuado que os valores de coesão e acoplamento tendem a piorar. 
  


## 2. Fichamento Bibliográfico 


* _Code smells co-occurrences_ (co-ocorrência de code smells) Quando existe uma relação direta entre dois ou mais  *code smells* encontrados (página 53).
* _Training session_ (Sessão de treinamento) Prerrogativa de instrução dos desenvolvedores participantes a despeito da temática (página 56).
* _Bord count technique_ (Técnica de contagem de borda) Técnica de classificação que usa da prerrogativa de concenso ao invés de maioria (página 59).


## 3. Fichamento de Citações 

* _"The ranking of the top-5 co-occurrence of code smells per system, from the most frequent to the less frequent indicate that God Class–Long Method and Disperse Coupling–Long Method, are the co-occurrences that most tend to co-occur together."_
* _"These results suggest that co-occurrences tend to increase over time. One of the factors that can explain this phenomenon is the number of features in each release. The latest releases have more features than the first."_
* _"The removal of code smells co-occurrences did not have a positive impact on attributes such as cohesion and coupling."_
* _" God Class–Long Method and Disperse Coupling–Long Method are the most frequent co- occurrences in the three systems and also the most difficult co- occurrences to refactor in developers’ perspective."_
* _" co-occurrence at class level happens when there is a God Class or Refused Parent Bequest along with some other code smell, in which case the developers could also choose which of the code smells to removal, thus de- characterizing the class-level co-occurrence.."_
* _"The comparison was made through the results of the quality metrics, and the comparison it was done with the most current version of each system before removing the co-occurrences and with that same system after the procedure of removing code smell co-occurrences."_

<div>