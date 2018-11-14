# fullthrottle-assignment
Search assignment for screening

#### Steps to run the project.

1. Clone the repository
2. `python3 manage.py migrate`
3. `python3 manage.py runserver`

### Endpoints:

**1. Search endpoint**

**_Request_:**

GET `localhost:8000/api/v1/search/{query}`


**_Response_:**
```
[
    "then",
    "them",
    "than",
    "those",
    "think",
    "three",
    "they",
    "things",
    "thread",
    "these",
    "there",
    "their",
    "through",
    "both",
    "month",
    "north",
    "others",
    "other",
    "south",
    "author",
    "something",
    "within",
    "another",
    "health",
    "without"
]
```

### Live APIs

The application is deployed on a Heroku server.

[https://fullthrottle-test.herokuapp.com/api/v1/search/th](https://fullthrottle-test.herokuapp.com/api/v1/search/th)

### Populate the database with test data
If you wish to populate your local database with test data, you can simple run the following command.

`python3 manage.py add_words`

This is a management command that would populate the database with the test data.
