init:
	pip install -r ./requirements.txt
local_run:
	flask run
container_run:
	docker compose up --build -d