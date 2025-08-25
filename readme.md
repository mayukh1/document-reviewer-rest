# document-reviewer-rest

## Cmd

### Create Virtal Env
python -m venv {venv}
### To activate virtual env
{venv}\Scripts\activate.bat
### Install Required Packages
pip install -r requirements.txt
### Check Installed Packages
pip freeze 
### MakeMigrations
python manage.py makemigrations
### Migrate
python manage.py migrate

python manage.py createsuperuser

### Run
python manage.py runserver

### Swagger:
http://localhost:8000/swagger/