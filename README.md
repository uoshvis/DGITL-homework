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
|Retrieve|api/carplates/<id>/|GET||
|Create|api/carplates/|POST|Data:
		{
	        'plate_number': 'PPP777',
	        'first_name': 'Kaliause',
	        'last_name': 'Bekepuris'
        }|
|Update|api/carplates/<id>/|PUT|Data:
		{
	        'first_name': 'Kaliause',
	        'last_name': 'Bekepuris'
        }|	
|Delete|api/carplates/<id>/|DELETE||


## Tests

	python manage.py test
