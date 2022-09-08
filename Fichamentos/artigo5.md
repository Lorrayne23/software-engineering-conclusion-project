<div align="justify">

# Automated Repair of Feature Interaction Failures in Automated Driving Systems

Raja Ben Abdessalem, Annibale Panichella, Shiva Nejati, Lionel C. Briand, and Thomas Stifter. 2020. Automated repair of feature interaction failures in automated driving systems. In Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA 2020). Association for Computing Machinery, New York, NY, USA, 88–100. https://doi.org/10.1145/3395363.3397386

## 1. Fichamento de Conteúdo

Os *softwares* utilizados em Sistemas de Direção Autônomos (ADSs, do inglês *Autonomous Driving Systems*) são comumente divididos em componentes a partir de sua particularidade, no que tange o decorrer do funcionamento direcional e a atuação desse no controle de execuções relacionadas a movimentações e percepções para o seu entendimento de ambiente e atuação com o meio. Dado tal paradigma, a problemática do artigo se baseia em erros encontrados no desenvolvimento que afetam a modularidade e a coordenação de atuação do sistema, onde interações não desejadas são realizadas entre funções por meio de uma prerrogativa de prioridade  executiva. Assim, é proposta uma técnica corretiva que detecta falhas em componentes de *ADSs* e automaticamente efetiva reparos, realizando buscas integradas a procura de erros nos programas com totalidade e não parcialidade de nível, conjuntamente a localização de *bugs* em código e de seu reparo por meio da abordagem denominada Reparo Automatizado de Regras de Integração (ARIEL, do inglês *Automated Repair of Integration Rules*). Os resultados demonstram a efetividade na estratégia de correção realizada para retificar tais falhas de interoperabilidade e se sobressai quando comparadas a outras técnicas já existentes no mercado tecnológico, com fomento da factualidade aplicativa por engenheiros atuantes no desenvolvimento de sistemas autônomos.

## 2. Fichamento Bibliográfico 

* _ADS features_ (recursos *ADSs*) unidades de funcionamento do *software* de sistemas de direção autônoma que se correlacionam quando em operação e possuem uma função específica (página 88).
* _integration rules_ (regras de integração) definição de condições de priorização para execução de um recurso de *ADS* (página 88).
* _multi-objectivization_ (multi-objetivação) estratégia de procura utilizada para fazer a reparação de um caminho (página 94).

## 3. Fichamento de Citações 

* _"Given that ADS testing is performed via simulators, each test tci specifies initial conditions and parameters for the simulator to mimic a specific self-driving scenario. To run a test case, the simulator that is initialized using a test case is executed for a time duration T set by the user."_
* _"ARIEL receives as input the test suite T S and the faulty self- driving system (f1, . . . , fn, Π), where Π denotes the faulty integration rules. The output are a set of repaired integration rules (denoted by Π∗) that pass all test cases in TS."_
* _"Note that even though our repair algorithm is multi-objective, it generates only one final solution. This is because our algorithm, being a single-state search, generates one solution in each iteration and stops if that solution is Pareto optimal, i.e., it dominates all partial patches in the archive."_
* _"AutoDrive1 and AutoDrive2 also include test suites with nine and seven system-level test cases, respectively. The test suite for AutoDrive1 contains four failing test cases, while the test suite for AutoDrive2 has two failing tests. Each failing test case for Auto- Drive1 and AutoDrive2 violates one of the safety requirements in Table 1."_
* _"We note that ARIEL is not able to handle integration failures when the failure is due to a missing integration rule. In such cases, engineers can review the unaddressed failing test cases and try to manually synthesize rules that can handle such failures."_
* _"We distinguish two dimensions for external validity: (1) the applicability of our approach beyond our case study system, and (2) obtaining the same level of benefits as observed in our case study."_
* _"In our approach, the search objectives are based on the failures exposed by the test suite T S . Each failing test tc ∈ TS exposes one (or more) failure(s) whose intensity is O(tc(u),rj)∈[−1;0],whererj istheviolatedsafetyrequirements."_

<div>