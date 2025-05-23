![374370531-87ad94eb-a00e-43b5-84c4-fbf7f7b9fd7d](https://github.com/user-attachments/assets/a1615722-5ee0-4f77-b747-e4d6cca2a301)

# On Data Predictor
- Repositório: https://github.com/eduardofuncao/on-data-predictor
- Vídeo de Apresentação: https://youtu.be/owYO5RxX57A

Ferramenta para predição de custo de plano de saúde e categorização de risco de clientes utilizando técnicas de machine learning, oferecida para Odontoprev por meio do Challange Fiap.

## Estratégia do projeto
O projeto principal do qual esta ferramente faz parte é um sistema de gerenciamento de sinistros para pacientes de planos odontológicos fornecido à Odontoprev através do Challange Fiap. Devido a isso, é de extrema útilidade para a companhia que os pacientes possam ser categorizados em grupos de risco bem determinados. Uma estratégia para garantir que isso funcione é utlizando um modelo de clusterização.
Além disso, também é desejável que o sistema possa prever uma estimativa para os custos do plano de saúde odontológico de um determinado paciente com base em algumas informações básicas sobre sua saúde que fazem parte de sua ficha cadastral (como por exemplo BMI, idade, se fuma, etc.). Algumas técnicas de machine learning podem ser utilizadas para alcançar este objetivo, como por exemplo o uso de um modelo de Regressão.

## Escolha e Treinamento dos modelos
Para este projeto, foi utilizado um dataset público que contém informações sobre custos de planos de saúde com base em características dos pacientes como idade, IMC, número de filhos, sexo, status de fumante e região geográfica. A análise exploratória revelou correlações importantes:

- O status de fumante é o fator mais impactante no custo do plano de saúde
- Existe uma correlação positiva entre idade e custo, mais pronunciada em fumantes
- O IMC mostra uma correlação positiva moderada com o custo
- O número de filhos e a região geográfica têm impacto menor

Para potencializar o efeito do status de fumante, foram criadas duas features adicionais, que potencializam a força do status de fumante de um cliente em relação com outras features do dataset:

- smoker_bmi: IMC multiplicado pelo status de fumante (1 para fumantes, 0 para não fumantes)
- smoker_age: Idade multiplicada pelo status de fumante (1 para fumantes, 0 para não fumantes)

Seis modelos de regressão foram avaliados para predição de custos:

1. Regressão Linear
2. Regressão Ridge
3. Regressão Lasso
4. Random Forest
5. Gradient Boosting
6. Support Vector Regression (SVR)

O Gradient Boosting apresentou os melhores resultados com um R² de 0,8772. A análise de importância de features confirmou que smoker_bmi foi a característica mais relevante (corroborando para a estratégia de implementação dessas features de correlação), seguida pelo status de fumante e idade, enquanto região e sexo tiveram influência mínima. Esse algoritmo será utilizado para prever o custo de um paciente ao plano de saúde, a depender das características analisadas.

Para a segmentação de clientes, foi utilizado o algoritmo K-means com k=4 (determinado pelo método do cotovelo). As features utilizadas incluíram idade, IMC, número de filhos, custos, smoker_bmi e smoker_age. Os clusters resultantes foram categorizados em níveis de risco:

- Baixo Risco: Clientes mais jovens (até 30 anos), não fumantes, custos mais baixos
- Risco Médio: Clientes de meia-idade (30-50 anos), não fumantes, segundo menor custo
- Alto Risco: Clientes mais velhos, não fumantes, custos moderadamente altos
- Risco Muito Alto: Contém quase todos os fumantes do dataset, custos mais altos

Ambos os modelos foram exportados para uso posterior na API Flask, possibilitando avaliação do custo de um paciente para o plano de saúde, também incluindo cada usuário a um grupo de risco baseado em suas caracterśticas estabelecidas.


## API para integração com outros serviços

Para disponibilizar os modelos de machine learning criados para serviços do projeto, foi criado um microserviço em uma api REST utilizando Flask (pode ser acessado na pasta `/api` na raíz do projeto). 
Ela expõe o endpoint POST `/predict` que é responsável por, utilizando os dados do paciente, retornar seu grupo de risco e o custo previsto de seu plano de saúde. 

### Endpoint `/predict` 
- Exemplo de Request
```bash
curl --location 'ondata-predictor.eduardofuncao.com/predict' \
--header 'Content-Type: application/json' \
--data '{
    "age": 23,
    "sex": "male",
    "bmi": 15,
    "children": 0,
    "smoker": "no",
    "region": "northwest"
}'
```

- Response
```json
{
    "predictedCost": 5009.953130247662,
    "riskCluster": 2,
    "riskLevel": "Low Risk"
}
```

Para testes, o serviço teve seu deploy em uma VPS particular para uso sem autenticação. Em um estágio final do projeto, é desejável que exista controle de acesso à API, e que ela seja gerenciada por algum cloud provider como Microsoft Azure ou AWS.

## Arquitetura de Microserviços

Buscando a melhor alternativa de disponibilizar os modelos treinados para outros serviços do sistema, um microserviço em nuvem, acessível por meio de uma API REST se mostrou como uma ótima solução. Por ser uma API, os dados de saída podem ser controlados
e seguir um padrão que forneça repetibilidade e segurança aos serviços. Sendo um microserviço, essa aplicação não está atrelada à outro projeto monolítico dentro do sistema, mas sim acessível por ele. 
Uma opção considerada a priori foi a de fazer a predição diretamente no Backend Spring Boot. Apesar de funcional, essa solução é menos modular e não se adapta bem a grandes mudanças em outras frentes do projeto. 
Caso o backend migrasse para outra plataforma, o código para acesso aos modelos de Machine Learning seria quase totalmente perdido.
Para a implementação dessa arquitetura, todos os serviços da aplicação foram transformados em contâiners docker, garantindo modularidade, autonomia e confiabilidade aos serviços desenvolvidos.

Apresentação Final
https://youtu.be/vtfjKXHb_9A

Conclusão
Embora classificar clientes de plano de saúde seja uma tarefa desafiadora (uma vez que um erro na classificação inicial pode acarretar na perda de um cliente em potencial), ela se mostra necessária para que a companhia possa garantir uma vantagem em relação aos seus competidores. Nesse projeto, foi usada uma base de dados de teste, que não possui dados em larga escala. Com a expertise e números da Odontoprev, este projeto poderia ser refinado de forma que os modelos desenvolvidos se tornassem ainda mais precisos. É importante ressaltar que estes modelos de machine learning, por envolverem dados sensíveis e decisões complexas, nunca podem ser utilizados para decisões finais, mas sim como um auxílio à análise minuciosa e criteriosa de uma pessoa (neste caso, um funcionário da odontoprev). É certo que, como ferramenta auxiliar, esta aplicação pode fornecer dados e insigths valiosos e de forma muito mais rápida e organizada do que com algum tipo de análise manual.

## Integrantes
- Artur Fiorindo RM553481
- Eduardo Função RM553362
- Jhoe Hashimoto RM553831
