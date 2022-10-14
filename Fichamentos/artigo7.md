<div align="justify">

# An Empirical Investigation on the Effect of Code Smells on Resource Usage of Android Mobile Applications

M. A. Alkandari, A. Kelkawi and M. O. Elish, "An Empirical Investigation on the Effect of Code Smells on Resource Usage of Android Mobile Applications," in IEEE Access, vol. 9, pp. 61853-61863, 2021. doi: [10.1109/ACCESS.2021.3075040](https://doi.org/10.1109/ACCESS.2021.3075040)

## 1. Fichamento de Conteúdo

O recente crescimento exponencial do desenvolvimento de *softwares* para vertentes de aplicações móveis, coloca em evidência a atuação desses relacionados ao trabalho de desenvolvedores no que tange a decorrência de práticas de códigos e o atendimento ou não de requisitos durante o desenvolvimento. Em tal promulgação, postula-se sobre a existência direta de performance e manutenção desses em relação à consequência da presença de *code smells*. Logo, o problema abordado pelo artigo se pactua no efeito que *code smells* podem acarretar ao uso de recursos como CPU e memória em aplicativos móveis Android. Assim, para resolver essa questão foram selecionados no *Github* oito *softwares* *open source* Android com o intuito de realização de testes.Por meio, da investigação de presença de três *code smells* estipulados, paralelamente a realização de refatoração pontual com o intuíto de observar uma ligação direta de tais fatores com a causalidade de utilização de recursos. Concomitantemente, obtiveram resultados que demonstram uma determinada classificação de *code smell* se relaciona a um  maior uso de CPU e outra classificação a um maior uso memória.Não obstante, ao se realizar a refatoração desses observa-se a não  avaliabilidade  positiva de uso quando as três classificações são refatorados conjuntamente e sim quando realizada a refatoração de apenas uma classificação. 


## 2. Fichamento Bibliográfico 

* _CPU Usage_ (Uso de CPU) Medida de esforço de quanto trabalho está sendo performado pelo processador (página 61855).
* _Memory Usage_ (Uso de memória) Medida do quanto de memória está sendo utilizada por uma aplicação móvel (página 61855).
* _Member Ignoring Method_ (Método de Ignorar Membro) Segmentação de *code smell* que atenta sobre a classificação errônea de um método estático ou dinâmico (página 61854).
* _Slow Loop_ (Loop Lento) Segmentação de *code smell* que atenta sobre a lentidão de um loop sobre um loop for-each (página 61854).


## 3. Fichamento de Citações 

* _"Applications with high CPU usage are a cause for concern, as it has a negative effect on battery life and device speed."_
* _"It was found that aDoctor failed to detect HashMap Usage code smell in several projects. Therefore, this code smell was detected through a simple search using Android Studio’s utilities."_
* _"Refactoring of indiviual code smells HashMap Usage, Slow Loop, Memory Ignoring Method often results in lower average CPU usage. However, the combined refactoring of these code smells may result in an increased average CPU usage in some cases."_
* _"This result indicates that code smells are not independent in improving or worsening the performance of Android applications and refactoring multiple code smells does not necessarily translate to an improvement in performance, and may even negatively impact the application’s performance."_
* _"Applying only one of the refactoring methods is enough to enhance the CPU usage and improve its quality. Thus, no need to apply all refactoring methods because their impacts will not be significant."_
* _"All tests were conducted on an Android emulator to eliminate any side effects such as the effect of other applications on battery usage and background CPU/Memory usage that may arise from testing on a physical device."_

<div>