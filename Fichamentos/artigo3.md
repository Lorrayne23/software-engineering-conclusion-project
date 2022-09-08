<div align="justify">

# Targeting Requirements Violations of Autonomous Driving Systems by Dynamic Evolutionary Search

Y. Luo et al., "Targeting Requirements Violations of Autonomous Driving Systems by Dynamic Evolutionary Search," 2021 
36th IEEE/ACM International Conference on Automated Software Engineering (ASE), 2021, pp. 279-291. doi: [10.1109/ASE51524.2021.9678883](https://doi.org/10.1109/ASE51524.2021.9678883)

## 1. Fichamento de Conteúdo

Sistemas de direção autônoma(*ADSs*, do inglês *Autonomous Driving Systems*) estão cada vez mais sendo utilizados no contexto mercantil e industrial, como no transporte de 
mercadorias *delivery* e na produção de carros *self-driving*, tais sistemas apresentam alto grau de complexidade.De tal modo, necessitam abarcar uma série de requerimentos que 
vão desde a segurança fornecida ao utente à obediência de regras de trânsito determinadas por localidade. Assim, o principal problema gira em torno da promoção de requisitos
a serem satisfeitos por parte dos desenvolvedores de *ADSs* que precisam saber combinações de violações que podem ocorrer e que gerarão falhas de atuação. Adversamente não 
existem testes de geração de cenários que possam expor diferentes combinações de requerimentos, o artigo promove então a criação de um *requirements violation pattern* para 
caracterizar diferentes requisitos de contravenção atreladamente a utilização de um teste denominado *EMOOD* que a partir de um algoritmo encontra diferentes violações possíveis.
Os resultados obtidos demonstram a efetividade de EMOOD atrelado a busca evolucionária para a realização e  geração de testes de cenário que demonstram alto nível de violações e
com procedência de nível crítico alta.


## 2. Fichamento Bibliográfico 

* _Likelihood of occurrence of patterns_ (probabilidade de ocorrência de padrões) verificação realizada através da busca por *EMOOD* da ocorrência de um requisito de violação (página 280).
* _Ego vehicle_ (veículo ego) veículo autônomo que faz o uso e executa o *ADS* (página 280).
* _Criticality ranking_ (classificação de criticidade) uma lista em ordem decrescente dos requisitos de violação padrões com base no seu nível crítico (página 282).
* _Search-based testing_ (testes baseados em pesquisa) por meio de otimização são criados cenários críticos de testes em veículos autônomos com propositais testes falhos (página 289).
* _Requirements-based testing_ (testes baseados em requisitos) checagem dos requisitos durante o desenvolvimento com o intuito de refrear recursos não prescindíveis no *design* de sistemas (página 289).
* _EMOOD_ teste responsável por gerar cenários diferentes para tornar visível distintas combinações de violações em ADS.


## 3. Fichamento de Citações 

* _"EMOOD conducts a type of dynamic evolutionary search, i.e., Evolutionary Many-Objective Optimization (EMOO), whose objectives are determined by Dynamic Prioritization (DP) that prioritizes the patterns in terms of criticality and likelihood to occur."_
* _"To evaluate the violation of requirement Ri, we compare Xi with the threshold gi specified in the definition of Ri; in this way, we get the evaluation result yi = f(Xi,Ri), ranging over the Boolean domain Di."_
* _"We cast the problem of generating ADS critical test scenarios for a specific requirements violation pattern as a many-objective optimiza- tion problem [28], where the fitness functions are defined as the indicators for requirements satisfaction/violation."_
* _"Thus, DP first computes a ranking of patterns based on their likelihood of occurrence. Then, DP merges this ranking with the ranking based on the criticality."_
* _"We observe that the time costs of EMOO, EMOO-IP, and EMOOD are less than Random, because these three approaches could generate more scenarios with violations of R2.1, and these scenarios are terminated earlier."_
* _"Our evaluation results on an industrial ADS have shown that EMOOD outperforms the baseline random testing and evolutionary search, and generates test scenarios that expose more violation patterns with higher criticality."_
* _"In simpler scenarios such as ST , the difference between the baseline approaches and EMOOD is lower, showing that EMOOD is particularly useful in finding critical patterns in large search spaces."_

<div>