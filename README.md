# BookListAPI-with-Django
This is a booklist API I made with plain Django.

# To Setup
Open terminal on project folder

Run the command
```
pipenv install
```

Start Django Application by running the command 

```
python manage.py runserver
```

#API ENDPOINTS

View all books by sending a GET request to the endpoint
```
http://127.0.0.1/api/books
```

Create a request by sending a POST request and payload to the endpoint
```
http://127.0.0.1/api/books
```

Payload
```
{
    "title" : "Django Books API",
    "author": "Peter Gambo",
    "price": 200.82,
    "inventory": 600
}
```