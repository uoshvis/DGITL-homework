DGITL coding homework
=====================

### Installation
	
Create a virtual environment for a project

	$ cd my_project_folder
	$ virtualenv -p python3 ENVname


Activate a virtual environment

	$ source ENVname/bin/activate


Install packages

    $ pip install -r requirements.txt

### Usage

    python manage.py runserver

## Documentation

List
	Endpoint: api/carplates/
	Method: GET
	
Retrieve
	Endpoint: api/carplates/<id>/
	Method: GET
	
Create
	Endpoint: api/carplates/
	Method: POST
	Data:
		{
	        'plate_number': 'PPP777',
	        'first_name': 'Kaliause',
	        'last_name': 'Bekepuris'
        }
Update
	Endpoint: api/carplates/<id>/
	Method: PUT
	Data:
		{
	        'first_name': 'Kaliause',
	        'last_name': 'Bekepuris'
        }
Delete
	Endpoint: api/carplates/<id>/
	Method: DELETE

## Tests

	python manage.py test
