<div align="justify">

# Does mutation testing improve testing practices?

G. Petrović, M. Ivanković, G. Fraser and R. Just, "Does Mutation Testing Improve Testing Practices?," 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE), 2021, pp. 910-921. doi: [10.1109/ICSE43902.2021.00087](https://doi.org/10.1109/ICSE43902.2021.00087)

## 1. Fichamento de Conteúdo

Testes são fundamentais no desenvolvimento de *software*, se tornando indubitável a necessidade de um guia prático a ser seguido para aqueles que desenvolvem grandes aplicações e no que se refere a escalação desses, se mostram presentes diversos teoremas práticos pontuados no desenvolvimento como gargalos executivos. A partir de tal ideal, o artigo  baseia-se em pontos de estudo realizados por pesquisadores com a colocação de mutantes como possíveis auxiliadores na proposta de uma prerrogativa de examino. A problemática instala-se na verificação de validades em sistemas grandes quando mutantes são mostrados a desenvolvedores, por tal ação são examinadas se a produção de testes por parte desses realmente se torna mais efetiva. Metodologicamente observam-se os efeitos de se mostrar mutantes como testes meta a desenvolvedores com o intuito de esclarecer a despeito de melhor qualidade no código gerado, ademais, como os testes afetam o efeito de sobrevivência dos mutantes em um determinado projeto examinado e a relação entre mutantes encontrados e falhas no próprio *software*.Os resultados promulgam que desenvolvedores expostos a testes mutantes realizam mais testes efetivos por um longo período e concomitantemente se mostra eficaz e de valor no que tange a aplicação em grande escala, inclusive industrial.

## 2. Fichamento Bibliográfico 

* _Coupling effect_ (efeito de acoplamento) falhas simples estão acopladas a falhas complexas, assim testes que identificam falhas simples identificarão comutantemente falhas complexas (página 915).
* _Mutant redundancy_ (redundância mutante) é o registro da geração e avaliação de vários mutantes em uma mesma linha (página 918).
* _Mutant sampling_ (amostragem de mutantes) é o conjunto de possíveis mutantes examinados em um teste (página 920).


## 3. Fichamento de Citações 

* _"The coupling effect is a foundational assumption underlying mutation testing: Simple faults are coupled to more complex faults in such a way that a test suite that detects simple faults is sensitive enough to likely detect complex faults as well."_
* _"Mutating only changed code is key to reducing the computational costs, but further optimizations are necessary to make mutation testing feasible and actionable"_
* _"As a proxy measurement of test quality, we use mutant survivability, i.e., the probability of a generated mutant being killed. The mutant survivability for a file in a code change is calculated as the ratio of surviving mutants to the total number of generated mutants for that file. A lower mutant survivability indicates a higher test suite quality."_
* _"In the code review system, reviewers can request developers to write tests for mutants they consider important. If developers improve their test suites over time, we would expect the ratio of such requests (for all reported mutants) to gradually decrease.Therefore, we also compute the ratio of requested fixes formutants over exposure."_
* _"Our mutation testing system rests on the assumption that generating and evaluating multiple mutants in the same line is not necessary. The primary reason for this is that we do not compute the mutation score but rather report mutants as test goals and direct developers’ attention to the mutated piece of code—any one productive mutant is sufficient for the latter."_
* _"Our results confirm that the set of mutants, generated with traditional mutation operators, is indeed highly redundant and that small sampling ratios are sufficient. Moreover, our results show that multiple mutants generated for the same line of code virtually always share the same fate in practice, implying that surfacing one mutant per line is sufficient."_

<div>