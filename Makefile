SHELL=/bin/bash
up:
	sudo docker-compose up
down:
	sudo docker-compose up
sshc:
	sudo docker exec -it $(shell sudo docker ps -f name=django -a -q) /bin/bash
