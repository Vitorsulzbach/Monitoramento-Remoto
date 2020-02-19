SHELL=/bin/bash
up:
	docker-compose up
down:
	docker-compose down
sshc:
	docker exec -it $(shell sudo docker ps -f name=django -a -q) /bin/bash
ssh:
	ssh Sulz@34.95.165.121
