# Resumen  News API
Resume News API using web scraping and the full set of Django REST Framework features.
The API have users, permissions, and allow for full CRUD (Create-Read-Update-Delete)
functionality. I also explore documentation.

| Image 1                                                                                       | Image 2                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| ![](https://github.com/alcibiadesBustillo/resumen-news-api/blob/master/images_app/image0.png) | ![](https://github.com/alcibiadesBustillo/resumen-news-api/blob/master/images_app/image1.png) |

| Image 3                                                                                       | Image 4                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| ![](https://github.com/alcibiadesBustillo/resumen-news-api/blob/master/images_app/image2.png) | ![](https://github.com/alcibiadesBustillo/resumen-news-api/blob/master/images_app/image3.png) |


## Dependencies
Python 3
Django

## Usage
```shell
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
## Migrate and runserver on port 8000

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Create superuser

```python
    python manage.py createsuperuser
```

## Feed the API

To feed the News API put the db.sqlite3 database in the root folder of [scrapping_resumen_news]() and run 
```python
python pipeline.py
```

## Url's

1. admin/
2. api/v1/
3. api-auth/
4. api/v1/rest-auth/
5. api/v1/rest-auth/registration/
6. ^doc(?P<format>\.json|\.yaml)$ [name='schema-json']
7. doc/ [name='schema-swagger-ui']
8. redoc/ [name='schema-redoc']

## License
[This project is under MIT License](https://opensource.org/licenses/MIT)
