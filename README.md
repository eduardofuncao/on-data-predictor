


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
