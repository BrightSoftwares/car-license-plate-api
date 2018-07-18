[![Python 3.7](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-370/)

# Django Rest Car Plates REST Api
This is a sample web application using Django Rest Framework.


## Getting Started

Clone this repo first:
```
git clone https://github.com/nerijus-st/django-rest-car-plates.git
```

Install required dependencies:
```
pip install -r requirements.txt
```

Run the application
```
python manage.py runserver
```

Check the default page, which is http://localhost:8000

## About application

Plates application has two models - **owner** and **plate**. Plate has many-to-one relationship with owner model.

There are some validation rules on both of them. Owner name and surname must be only in alphabetical characters, not nullable, not empty and not exceed 30 characters limit.
License plate number must be assigned to the owner, not nullable, not empty, unique and must come with the format such as ABC123 (three letters followed by three numbers).

## Running tests
Currently application has 7 tests covered. To run a test execute following command:
```
python manage.py test plates
```

## Admin panel
Application has admin panel implemented.
Accessed via browser http://localhost:8000/admin

**Username:** *admin*  
**Password:** *Password123*

## Endpoints

### Owners

| Endpoint      | HTTP Method   | CRUD Method   | Result                  |
| ------------- | ------------- | ------------- | -------------           |
| owners        | GET           | READ          | Get all owners          |
| owners/:id    | GET           | READ          | Get a single owner      |
| owners        | POST          | CREATE        | Add a single owner      |
| owners/:id    | PUT           | UPDATE        | Update a single owner   |
| owners/:id    | DELETE        | DELETE        | Delete a single owner   |

### Plates

| Endpoint      | HTTP Method   | CRUD Method   | Result                  |
| ------------- | ------------- | ------------- | -------------           |
| plates        | GET           | READ          | Get all plates          |
| plates/:id    | GET           | READ          | Get a single plate      |
| plates        | POST          | CREATE        | Add a single plate      |
| plates/:id    | PUT           | UPDATE        | Update a signle plate   |
| plates/:id    | DELETE        | DELETE        | Delete a single plate   |

## TODO

Application must have more tests than now, of course.  
Authentication and authorization is not implemented.  
Frontend part (forms) are django default generated.
