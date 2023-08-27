build:
	docker build --force-rm -t $(options) esscwebsite:latest .

build-prod:
	$(MAKE) build options="--target production"

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down $(options)

compose-manage-py:
	docker-compose run --rm $(options) python manage.py $(cmd)