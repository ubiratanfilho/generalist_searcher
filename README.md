# Generalist Searcher

Esse repositório contém um chatbot que responde sobre qualquer tema não relacionado a Engenharia Civil, e se necessário realiza pesquisas na Web.

## Requisitos

- Docker Desktop
- OpenAI API Key
- Tavily API Key

## Como executar o projeto
1. Exporte a sua chave de API da OpenAI e da Tavily

    ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export TAVILY_API_KEY="your-tavily-api-key"
    ```

2. Rode o comando abaixo para subir os serviços

   ```bash
   docker compose up -d
   ```

3. Faça a requisição para gerar a resposta (é possível também utilizar a coleção Postman disponível na pasta `postman`):

   ```bash
   curl --location 'http://localhost:5002/generate_answer' \
      --header 'Content-Type: application/json' \
      --data '{
         "question": "Quando é o próximo jogo do Palmeiras?",
         "thread_id": 2
      }'
   ```