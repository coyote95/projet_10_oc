
# Projet 10 OpenClassrooms: Create a secure RESTful API using Django REST


Creation of the API 'SoftDesk' using the Django Rest and Postman request.  This website aims to manage users, projects, issues and comments with OWASP rules. Setting up different permissions, notably through the use of access tokens.





## Installation with pip

Install project with powershell windows:

```bash
    git clone https://github.com/coyote95/projet_10_oc.git
    cd projet_10_oc
    python -m venv ENV
    source ENV/Scripts/activate
    python  manage.py migrate
    pip install -r requirements.txt
    python manage.py runserver
```
## Installation with poetry

```bash
    git clone https://github.com/coyote95/projet_10_oc.git
    cd projet_10_oc
    poetry install
    poetry shell
    python  manage.py migrate
    python manage.py runserver
```


    
## Postman request
![user](https://github.com/coyote95/projet_10_oc/assets/141831464/b1ecb965-0ebd-4788-a8ff-735231bfe79a)
![token](https://github.com/coyote95/projet_10_oc/assets/141831464/ccf018ee-baeb-4137-bb1e-2bac51145180)
![projetc](https://github.com/coyote95/projet_10_oc/assets/141831464/29895883-856b-4252-a9d2-04a6c69620a5)
![authorization](https://github.com/coyote95/projet_10_oc/assets/141831464/10893d3e-034d-41e0-835d-16cfdcf87dc1)


