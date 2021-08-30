# testbonos

To run the example do the following steps:

```console
$ mkdir bonos
$ cd bonos/
```

Tested with:
```console
$ python -V
Python 3.5.3
$ python -V
Python 3.8.11
```
Should work with any python version > 3.5.3

Create the virtual environment
```console
$ python3 -m venv venv
```

Activate the virtual environment
```console
$ . venv/bin/activate
```

Upgrade pip and install wheel
```console
$ pip install --upgrade pip
$ pip install wheel
```

Clone the git repository
```console
$ git clone https://github.com/jboadas/testbonos
```

Install libraries of the example
```console
$ cd testbonos/
$ pip install -r requirements.txt 
```

Create the database
```console
$ python manage.py migrate
```

Run tests
```console
$ python manage.py test
```

Create admin user
```console
python manage.py createsuperuser --email admin@example.com --username admin
```

Run the development server
```console
$ python manage.py runserver
```

Server will be available at:
http://127.0.0.1:8000/

We can access the api using the Django interactive API explorer

Or using curl commands on the terminal:

View users
```console
curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/
```

View bonds
```console
curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/bonos/
```

Bond view detail
```console
curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/bonos/4/
```

Publish bond to sell
```console
curl -H 'Accept: application/json; indent=4' -u admin:password123 -F 'bono_name=ADMDOS' -F 'bono_number=5000' -F 'bono_price=9999.99' http://127.0.0.1:8000/bonos/
```

Buy bond (sell user/buy user need to be differents)
```console
curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/bonos/4/comprabono/
```

Get bond USD price
```console
curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/bonos/4/preciousd/
```
