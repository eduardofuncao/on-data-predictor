# On Data Predictor
Ferramenta para predição de custo de plano de saúde e categorização de risco de clientes utilizando técnicas de machine learning, oferecida para Odontoprev por meio do Challange Fiap.

## Estratégia do projeto
O projeto principal do qual esta ferramente faz parte é um sistema de gerenciamento de sinistros para pacientes de planos odontológicos. Devido a isso, é de extrema importância que os pacientes possam ser categorizados em grupos de risco bem determinados. Uma estratégia para garantir que isso funcione é utlizando um modelo de clusterização.
Além disso, também é desejável que o sistema possa prever uma estimativa para os custos do plano de saúde odontológico de um determinado paciente com base em algumas informações básicas sobre sua saúde que fazem parte de sua ficha cadastral (como por exemplo BMI, idade, se fuma, etc.). Algumas técnicas de machine learning podem ser utilizadas para alcançar este objetivo, como por exemplo o uso de um modelo de Regressão.

## Escolha e Treinamento dos modelos
Para este projeto, como não foram fornecidos datasets específicos para o treinamento do modelo, foi selecionado um dataset público que relaciona informações de pacientes ao preço de seu plano de saúde.
Os detalhes do treinamento dos modelos pode ser visualizado no notebook em `/ml-training' (na raíz do diretório), ou através do link de visualização para o Google Collab [Notebook Google Collab](https://colab.research.google.com/drive/19hOUn-8Pp8iPUhMlxhvgsPjVJAvgxmjX?usp=sharing). Ao final das análises, os modelos mais eficientes foram exportados para utilização dentro de uma API REST


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

## Integrantes
- Artur Fiorindo RM553481
- Eduardo Função RM553362
- Jhoe Hashimoto RM553831
