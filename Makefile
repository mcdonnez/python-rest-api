### Edit these variables ###
IMG_NAME=python-rest-api-template
PORT=8080
TAG=latest
### End of edit ###

IMG=$(IMG_NAME)
CONTAINER=$(IMG_NAME)
RUNOPTS=-p $(PORT):8080
APPDIR=/var/www/app

dev: rm build rundev open_swagger dlogs

open_swagger:
	sleep 3
	open http://localhost:8080/python-rest-api-template/ui

rundev:
	docker run $(RUNOPTS) --name $(CONTAINER) -d --volume $(PWD):/var/www $(IMG):$(TAG) gunicorn --reload 'app.server:app' -c config/gunicorn.conf.py

lint:
	docker run --name $(CONTAINER)-lint --rm --volume $(PWD):/var/www $(IMG):$(TAG) pylint app tests

test:
	docker run --name $(CONTAINER)-test --rm --volume $(PWD):/var/www $(IMG):$(TAG) sh -c "cd /var/www && coverage run -m unittest && coverage report --fail-under 90"

rmi:
	docker rmi -f $(IMG):$(TAG)
	docker rm $$(docker ps -a -q) || true
	docker rmi $$(docker images | grep "^<none>" awk "{print $$3}") || true

push:
	docker push $(IMG):$(TAG)

build:
	docker build --pull -t $(IMG):$(TAG) .

pull:
	docker pull $(IMG):$(TAG)

run: rm
	docker run -d $(RUNOPTS) --name $(CONTAINER) $(IMG):$(TAG)

rm:
	docker rm -f $(CONTAINER) || true

deploy:
	echo "TBD"

enter:
	docker exec -it $(CONTAINER) bash

app_log:
	docker exec -it $(CONTAINER) tail -f /var/logs/application.log

access_log:
	docker exec -it $(CONTAINER) tail -f /var/logs/access.log

dlogs:
	docker logs -f $(CONTAINER)
