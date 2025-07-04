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

- To install latest pip
```
python -m ensurepip --upgrade
```
# Add tailwindCSS in Django Project

1. Install TailwindCSS
```
uv pip install django-tailwind
```

2. Install Hot Reloading of TailwindCSS
```
uv pip install django-tailwind[reload]
```

3. Add tailwind as an App in settings.py
```
INSTALLED_APPS = [
    # other Django apps
    'tailwind',
]
```

4. Create a theme named TailwindCSS App
```
python manage.py tailwind init
```

5. Add theme app in settings.py
```
INSTALLED_APPS = [
    # other Django apps
    'tailwind',
    'theme'
]
```

6. Set theme as TailwindCSS App in settings.py
```
TAILWIND_APP_NAME = 'theme'
```

7. Set npm bin path
```
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

8. To install TailwindCSS dependencies
```
python manage.py tailwind install
```

9. From theme>templates>base.html copy to the current Project
```
{% load static tailwind_tags %}
    ...
    <head>
    ...
    {% tailwind_css %}
    ...
</head>
```

10. Set hot reloading for TailwindCSS
```
INSTALLED_APPS = [
    # other Django apps
    'tailwind',
    'theme',
    'django_browser_reload'
]
```

11. Set middleware in settings.py
```
MIDDLEWARE = [
    # ...
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    # ...
]
```

12. Set url in urls.py
```
from django.urls import include, path
urlpatterns = [
    ...,
    path("__reload__/", include("django_browser_reload.urls")),
]
```

13. To start the tailwindCSS server in seperate terminal
```
python manage.py tailwind start
```

- for production
```
python manage.py tailwind build
```
- [More Info](https://django-tailwind.readthedocs.io/en/latest/installation.html)

### Migrate the all the errornuous packages and also to access the user
```
python manage.py migrate
```

### Create a Super User
```
python manage.py createsuperuser
```
- Give username and password

- To Change password
```
python manage.py changepassword username
```

### Database Models
- We will create models for database in apps.

- Create a model in any app
```
class Chai(models.Model):

    CHAI_CHOICES=[
        ("ML","MASALA"),
        ("GN","GINGER"),
        ("PL","PLAIN"),
        ("KW","KIWI"),
        ("EL","ELAICHI")
    ]

    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="chais/")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_CHOICES)
```

- In settings.py
```
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
```

- In urls.py
```
from django.conf import settings
from django.conf.urls.static import static

- add this to urlPatterns
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- First create a migration
```
python manage.py makemigrations app_name
```

- Migrate this using
```
python manage.py migrate
```

- Register the model to view the model in admin panel
```
from django.contrib import admin
from .models import Chai
# Register your models here.

admin.site.register(Chai)
```

### Topics
- Templates and Static Files
- jinja - template engine
- django apps
- Adding TailwindCSS
- Admin panel(super user)
- Create Models and Urls for Database