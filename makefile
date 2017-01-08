all:
	python manage.py flush
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py loadrounds
	python manage.py runserver
