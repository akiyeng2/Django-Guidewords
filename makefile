all:
	python manage.py flush
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	./manage.py shell < makerounds.py
	python manage.py runserver
