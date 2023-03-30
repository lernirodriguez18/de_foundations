#! / Bin / bash

docker build -t python3 .

docker-compose up -d

docker run -d --name upload_data -v "$PWD"/data:/usr/src/myapp -w /usr/src/myapp python3 sleep 1000

docker network connect tpf-foundations-lernirodriguez18_foundations_net upload_data

docker exec -it upload_data bash -c "python3 upload_data.py"

docker exec -it upload_data bash -c "python3 consultas_negocio.py"