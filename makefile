SCR=./manage.py shell < makerounds.py


all:
	python manage.py flush
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	$(SCR)
	python manage.py runserver
