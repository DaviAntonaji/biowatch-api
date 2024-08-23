
#!/bin/bash

docker stop AntiTalaricagemAPI
docker rm AntiTalaricagemAPI

docker build -t antitalaricagemapi .

docker run -d -p 8000:8000 --name AntiTalaricagemAPI --env-file .env antitalaricagemapi