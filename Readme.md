- First installed uv - An extremely fast Python package and project manager, written in Rust.
```
pip install uv
```

- Create a Virtual Environment
```
uv venv
```

- Activate using this command
```
.venv\Scripts\activate
```

- Install Django
```
uv pip install Django
```

- Then to create the Django Project
```
django-admin startproject project_name
```
- Change the directory using ```cd``` command

- To start the project app
```
python manage.py runserver port_number
```

- To create an Django App
```
python manage.py startapp app_name
```

- To add TailwindCSS
```
uv pip install django-tailwind
```
then run
```
uv pip install 'django-tailwind[reload]'
```

- To install latest pip
```
python -m ensurepip --upgrade
```
- Add tailwindCSS 'tailwind' as an app in settings

- To create an app with tailwindCSS
```
python manage.py tailwind init
```

- To install that folder
```
python manage.py tailwind install
```

- To start the tailwindCSS server
```
python manage.py tailwind start
```

```
python manage.py tailwind build
```

### Topics
- Templates and Static Files
- jinja - template engine
- django apps
- Adding TailwindCSS