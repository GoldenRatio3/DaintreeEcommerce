# Daintree shopping site.

This is a Django project for a shopping site organised into three sections: Login, Shopping and Checkout. 

## Getting Started

### Prerequistes

Python which can be downloaded [here](https://www.python.org/downloads/)

Download Django - instructions can be found here [here](https://www.djangoproject.com/download/)

### Installing
```
Download this repo to your local computer and load up using a Python IDE/Text Editor
```

## Running

1. ```cd Daintree```
2. ```python manage.py runserver ``` - this will run the development server here ``` http://127.0.0.1:8000/ ``` 

## Contributing
Feel free to contribute by submitting pull requests.

## Project Outline

The Login page is where a user can login using their credentials or sign up with a new account. Login has the following fields:

First Name
Last Name
Username
Email
Phone number
Address (first line, Town and Post Code)

The user model uses django's built in user model with a one-to-one relationship. Figure 1 dispays the model with it's relationship and extra fields. 

The shopping section is for browsing the items in Daintree. The user can add an item to their shopping basket. The page uses ajax requests for updating the users basket.


The checkout page is for viewing the users basket. There the user can remove an item, or ammed the quantity for each item. The page uses ajax requests to remove and amend items. 


A user pays on the checkout page. The user receives an email from Daintree with the cost of their purchase and  their delivery address. The users basket is saved if the user logs in and out. The email uses django's built in library for sending emails. (The email is currently set up to a temp email address with a temp password so feel free to use the given email and password)


Daintree uses a MySQL database with the openshift cartridge. Daintree connects to the database using three model files. The login contains the Info model for the user. The Shopping sections contains the Item model for the items Daintree stocks. The Checkout holds the Basket Model users to an item with the quantity of each item as an attribute. 

Ajax Requests are used throughout daintree to submit and retrieve information from the databse.

Bootstrap is used to style the webstite. It is used in the checkout section to style the text, tables and buttons.

Daintree's REST API can be reached from /api/ path. User details (not the password) and item details can be browsed. The API uses django's restframwork library with serializers and ViewSets. 

## License
This project is licensed under the MIT License - Read the LICENSE.md file
