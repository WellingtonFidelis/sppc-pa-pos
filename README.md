## Commands
```bash
conda create python=3.10 --prefix ./venv
```
```bash
conda activate ./venv
```
```bash
pip install --upgrade
```

```bash
pip install Django
```

```bash
pip freeze >> requirements.txt
```

```bash
mkdir djangoapp
```

```bash
django-admin startproject api ./djangoapp
```


```bash
python djangoapp/manage.py runserver
```

First run.
```bash
docker-compose up --build
```

To other run builds, remove all containers and theis volumes, after run follow command
Indicated alwayes when the Dockerfiles, docker-compose.yml and .env file was changed
```bash
docker-compose up --build --force-recreate
```

To run commands insed containers
```bash
docker-compose run djangoapp python manage.py startapp api_sppc
```

Super user Django
login: admin_user
psw: admin_user$#@!