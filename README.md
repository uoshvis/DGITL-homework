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

|Action|Endpoint|Method|Data|
|---|---|---|---|
|List|api/carplates/|GET||
|Retrieve|api/carplates/<id\>/|GET||
|Create|api/carplates/|POST|{'plate_number': 'PPP777',<br />'first_name': 'Kaliause',<br />'last_name': 'Bekepuris'}|
|Update|api/carplates/<id\>/|PUT|{'first_name': 'Kaliause',<br />'last_name': 'Bekepuris'}|	
|Delete|api/carplates/<id\>/|DELETE||

##### AngularJS part is available at root link.

## Tests

	python manage.py test
