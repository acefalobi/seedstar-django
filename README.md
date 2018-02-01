# Jenkins Script

This simple Django application which stores names and email addresses in an SQLite database.

It includes the following:

* A welcome page with links to the the list and create functions at *('/')*
* A list of all stored names and email addresses at *('/list')*
* A create function that adds a name/email addresses to the database at *('/add')*

## Usage

Install required packages from *requirements.txt* using:

`pip install -r requirements.txt`

Then simply start the python server with *manage.py* like so:

`python manage.py runserver 8000`