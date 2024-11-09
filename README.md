> [!abstract]  Grupo
> - Artur Lopes Fiorindo 553481 
> - Eduardo Felipe Nunes Função 553362 
> - Jhoe Yoshio Kochi Hashimoto 553831  

> [!quote]  Link para o vídeo apresentando o projeto
> Desenvolvimento: https://youtu.be/bX3TetzVsJc
> Pitch: https://www.youtube.com/watch?v=eZkiuw65Szw


# On Data
Gerenciamento de Sinistros para planos de saúde odontológicos

![Untitled](https://github.com/user-attachments/assets/1776543b-1caa-4986-9dc3-0621b3fcce2c)
### Apresentação do Projeto
On Data é um ecossistema criado para auxiliar para o gerenciamento de pedidos de reembolso para sinistros em planos médicos (especialmente para planos dentários). Para isso, o sistema será responsável por classificar pacientes por classe de risco associado (baseado em histórico hospitalar, status socioeconômico) e analisar reivindicações de sinistros, predizendo se o procedimento solicitado deve ser aprovado com base nas informações conhecidas, e qual é o risco associado a um determinado cliente. Como um módulo adicional do sistema, haverá um modelo de análise de radiografias dentárias, que poderá ser utilizado para indicar a doença apresentada, auxiliando funcionários do plano odontológico na tomada de decisão, sem que seja necessária a avaliação de um especialista para todos os casos.

### Problema
O processo de avaliação e disputa de sinistros não é trivial. Com a possibilidade de golpes e avaliações errôneas, há grandes responsabilidades para a tomada de decisão. Como o volume de reivindicações nesta área é muito grande, e a quantidade de especialistas para análise é limitada, é inevitável que se use algum tipo de sistema computacional para tornar a dinâmica de aprovações e concessão de reembolso mais eficiente. Cada hora de um médico/dentista salva pelo uso de um sistema como este é extremamente valiosa financeiramente. Além disso, é importante ressaltar o aspecto humanitário do desenvolvimento deste sistema. Quanto mais rapidamente e de forma precisa acontecer a tomada de decisão para aprovações de procedimento médicos, menor será o tempo de espera médio que um paciente deve aguardar até que possa ser operado. Resulta disso que, quadros críticos ou de piora repentina devem diminuir com a implementação deste projeto.

### Alternativas de Solução
Existem inúmeras alternativas para gerenciamento de recurso (os ERPs como da Salesforce, Oracle, etc). Esses produtos, sobreviventes à validação do mercado, tem uma enorme qualidade é podem fornecer soluções para os mais diversos ramos da indústria.
No geral, essas alternativas se estabelecem como produtos mais generalistas. o Projeto On Data vai fornecer uma solução especializada para o gerenciamento de reivindicações de sinistros de planos médicos. A vantagem disso é que funcionalidades mais direcionadas podem ser implementadas no sistema, como por exemplo o analisador de radiografias, ou o classificador de risco de clientes.

### DER
![Untitled](https://github.com/user-attachments/assets/01d4a307-9504-49e8-9306-ffbdfaae393c)


### Modelagem
#### Técnicas de Machine Learning / IA
A seguir serão listadas todas as funcionalidades de inteligência artificial que estarão incluídas no projeto:
1. **Classificador de radiografias dentárias para detecção de doenças** --> Utilização de modelos pré-treinados para visão computacional, como pro exemplo o modelo fornecido pela roboflow, que facilita seu treinamento através do website.
2. **Classificador de nível de categoria de risco de clientes, com base em histórico médico, idade, condições genéticas** --> pode ser implementado com um modelo classificatório KMeans. Como os casos não tem label, é um modelo rápido e eficiente para a classificação.
3. **Atribuição de escore de risco de processo para a empresa seguradora, definindo quais clientes devem ser atendidos prioritariamente** --> Pode ser implementado com técnicas de regressão, por exemplo com um árvore de decisão de regressão. Dependendo das features avaliadas, o modelo pode colocar cada cliente em ramos diferentes da árvore de decisão, categorizando-os.
4. **Auxiliador de aprovação, que deve alertar o revisor do processo em caso de fraudes e tentativas de golpe** --> implementado com algum algoritmo de identificação de anomalia, que avalia o dataset e busca por fugas de padrão. Por exemplo, Isolation Forest.

### Utilzando IA na prática
Como desenvolvimento inicial para o projeto, vemos que é extremamente importante que uma empresa seguradora de planos odontológicos possa categorizar seus pacientes, seja com base no status financeiro, seja com base em assiduaidade ou com base em saúde odontológica de fato. Dessa forma, com um Proof of Concept, foi desenvolvido um modelo Kmeans de categorização de pacientes. Para mais informações sobre o andamento do projeto, verificar o vídeo vinculado no início do README.


#### Bibliotecas utilizadas
- Plataforma Roboflow para detecção/classificação em visão computacional
- Sklearn para o uso dos algoritmos de Kmeans, DecisionTreeRegressor, IsolationForest
- Pandas para importação e tratamento dos dados
- MatplotLib para visualização dos dados

