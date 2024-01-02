<p align="center">
    <img src="https://github.com/iamaakashbasnet/basnet-store/assets/136826895/bbc79333-304e-421d-aa0f-70414c51efad" alt="Basnet Store logo" width="200" />
</p>
<h3 align="center">Basnet Store</h3>
<p align="center">Customer credit management web app for Basnet Store</p>

## Project Setup

Install required packages

```
$ pip install -r requirements.txt
```

Create .env file
```
SECRET_KEY=ABC123
PROJECT_ENV=DEV
```

Initialize database:

```
$ python manage.py makemigrations
$ python manage.py migrate
```
