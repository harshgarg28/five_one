# Flask CRUD APIs

## Description
This project provides a set of CRUD (Create, Read, Update, Delete) APIs implemented in Python using the Flask framework. These APIs allow users to perform CRUD operations on a resource, such as users in this case.

## Accessing the APIs
The APIs can be accessed using the following base URL:
[https://five-one-flask.onrender.com/](https://five-one-flask.onrender.com/)

## Endpoints
- **GET `/users`**: Retrieve all users.
- **GET `/users/<user_id>`**: Retrieve a specific user by ID.
- **POST `/users`**: Create a new user.
- **PUT `/users/<user_id>`**: Update a user's information by ID.
- **DELETE `/users/<user_id>`**: Delete a user by ID.

## Usage
- To retrieve all users: `GET /users`
- To retrieve a specific user: `GET /users/<user_id>`
- To create a new user: `POST /users` with JSON data containing the user's information.
- To update a user: `PUT /users/<user_id>` with JSON data containing the updated user's information.
- To delete a user: `DELETE /users/<user_id>`

## Response Format
- Successful requests will return a JSON response with the appropriate status code.
- Error responses will include a JSON object with an error message and an appropriate status code.

## Sample Request (using cURL)
- Create a new user:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "example_user", "email": "example@example.com"}' https://five-one-flask.onrender.com/users
```

## Technologies Used
- Python
- Flask

## Deployment
The project is deployed on Render at [https://five-one-flask.onrender.com/](https://five-one-flask.onrender.com/)
