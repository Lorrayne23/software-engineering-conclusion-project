<div align="justify"> 

# An Empirical Study of Refactorings and Technical Debt in Machine Learning Systems

Y. Tang, R. Khatchadourian, M. Bagherzadeh, R. Singh, A. Stewart and A. Raja, "An Empirical Study of Refactorings and Technical Debt in Machine Learning Systems," 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE), 2021, pp. 238-250. doi: [10.1109/ICSE43902.2021.00033](https://doi.org/10.1109/ICSE43902.2021.00033)

## 1. Fichamento de Conteúdo

Grandes sistemas de *Machine Learning* (*ML*) não diferente de outros sistemas complexos, se apresentam dificultosos a despeito de seu mantenimento, na apresentação de débitos técnicos e em problemas de execução. Apesar de a engenharia de *software* ser aplicada no que tangencia a evolução do mesmo, ainda existe uma presente preocupação em relação à ocorrência de manutenção nesses sistemas. A problemática  manifesta-se em maior proporção com o decorrer do tempo, quando se torna difícil manter sua atuação e o gasto necessário para essa realização, somando-se  a atividade dispendiosa de desenvolvedores na solução de complicações em relação a refatoração. Assim, foram realizadas explorações de métodos específicos de refatoração que são fortemente tangenciadas ao *ML*, com ocorrência dentro e fora de códigos relacionados a esse setor.A partir, da criação de sujeitos de análise e de observâncias intituladas como *commit mining*,*refactoring identification* e *refactoring classification*,os resultados demonstram que a refatoração de sistemas relacionadas ou não ao *ML* em sua grande maioria se apresentam como categorias de dívida técnica e duplicação de código. Ademais, foram geradas novas refatorações específicas de ML e categorias de dívida técnica, além da introdução de recomendações, melhores práticas e anti-padrões.

## 2. Fichamento Bibliográfico 

* _Refactoring hierarchical taxonomy_ (refatoração de taxonomia hierárquica) criação de grupos hierárquicos de classificação para *ML* (página 238).
* _Refactoring Classification_ (classificação de refatoração) ato de classificar a refatoração em uma categoria de acordo como essa foi identificada (página 239).
* _Refactoring Identification_ (identificação de refatoração) verificação de correspondência aleatória para identificação (página 239).

## 3. Fichamento de Citações 

* _"Duplicate code elimination was a major refactoring theme in ML system evolution, and we conjecture such systems are more prone to duplication due to slight variations in learning algorithms."_
* _"Refactorings in all parts of the system were considered, as opposed to only modules responsible for ML. This is done because “only a small fraction of real-world ML systems is composed of ML code."_
* _"Refactorings are separated into two top-level categories, namely, those specifically related to ML systems (ML-specific) and those tangentially related,i.e., those that apply to general systems (generic). Categories in the former division are novel; they were formulated as a result of this study and are a key contribution of this work."_
* _"Generic dead code elimination (DED), which may be accomplished via reorganization or deletion, was another refactoring that crosscut categories but was not prevalent (only.11%)."_
* _"Dead experimental code paths [1] are those used to prototype new learning algorithm variants. If successful, they are eventually incorporated into the mainline logic, making the experimental paths irrelevant (and disabled)."_
* _"Although poor variable name quality can cause confusion and inhibit effective software evolution in general, it is especially problematic in ML systems due to the high reliance on matrix calculations that may involve many temporary variables thus compounding theissue."_

<div>
