# Kletos-Backend
Kletos Backend API
=====================

Overview
--------

This is the backend API for the Kletos application, built using Flask and utilizing various extensions for database management, authentication, and file storage.

Dependencies
------------

* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* Flask-Mail
* Flask-WTF
* Flask-Login
* Firebase Admin SDK

Setup
-----

### Firebase Configuration

* Create a Firebase project and enable the Firebase Admin SDK.
* Download the `firebase-adminsdk-wpe3s-7c4898beb9.json` file and place it in the `app` directory.
* Update the `storageBucket` name in the `firebase_app` initialization to match your Firebase project's storage bucket name.

### Environment Variables

* Set the following environment variables:
	+ `FLASK_APP`: the name of the Flask app
	+ `FLASK_ENV`: the environment (e.g. development, production)

Running the App
---------------

* Run `flask run` to start the development server.
* Use a tool like Postman or cURL to test the API endpoints.

API Endpoints
-------------

### Authentication

* **POST /login**: Authenticate a user and return a JSON Web Token (JWT)
	+ Request Body: `username` and `password`
	+ Response: `access_token` (JWT)
* **POST /register**: Register a new user
	+ Request Body: `username`, `email`, and `password`
	+ Response: `user_id` and `access_token` (JWT)

### Users

* **GET /users**: Retrieve a list of all users
	+ Response: `users` (array of user objects)
* **GET /users/:id**: Retrieve a single user by ID
	+ Response: `user` (user object)
* **PUT /users/:id**: Update a single user
	+ Request Body: `username`, `email`, and/or `password`
	+ Response: `user` (updated user object)

### Files

* **POST /files**: Upload a new file to Firebase Storage
	+ Request Body: `file` (multipart/form-data)
	+ Response: `file_url` (URL of the uploaded file)
* **GET /files/:id**: Retrieve a single file by ID
	+ Response: `file_url` (URL of the file)
* **DELETE /files/:id**: Delete a single file by ID
	+ Response: `success` (boolean)

### Miscellaneous

* **GET /healthcheck**: Healthcheck endpoint for the API
	+ Response: `success` (boolean)

Contributing
------------

* Fork the repository and create a new branch for your changes.
* Submit a pull request with a clear description of your changes.

License