### MVP
## Login
    - [x] route to render login.html
        - this form will have `<form action="/submit-login" method="POST">` (the opening tag)
        - each input should have `name="password"` 
    - [x] route to handle post request from form submit (in server.py)
        - [x] get the user's input (name/email, password)
            - use `request.form.get("password")`
        - [x] query db for user with that name/email (user crud function)
        - [x] compare db user and input user's passwords
        - [x] redirect back to login (with flash?) if fail
        - [x] if user exists and has correct pw, redirect to main app
        - [x] if user exists, add user_id to session
        <!-- session is a magical dictionary that you can access from any view function in your server 
        session['user_id] = user.user_id
        -->
## Register

## Search bar that pulls from api 
- [x] most of this feature
- api call
- add data to page.....

## Favorite a plant ***UP NEXT***
In order to do this before login/reg/session, all favoriting will be done by one test user for now (use a user id that you know exists in your db, hard code `user_id = 1`)
    - [X] use SQLAlchemy to make a relationship between a user and a test plant 
        <!--test_user.favourite_plants.append(test_plant)-->
        <!--db.session.add(test.user)-->
        <!--The secondary reference in the User table pretend that Favourites table does not exist -->
    - [X] package that in to a crud function
    - [X] make a plant object from data similar from the API
    <!-- if you enter plant information using SQLAlchemy, you created an object and a row in the db once committed  -->
    - [ ] figure out what happens when a plant already exists in the db (unique constraint) TODO: until i tackle this, just use dif plants each time
    - [x] get plant information from the frontend to the server 
        - [x] every plant is a form with a submit button 
            - [x] if button is clicked, use html form to send information to server
            - [x] Favourite is added to server and redirect

## see user's fav plants
- [x] route to render a template "/users/<user_id>" --> "localhost://5000/users/1" if user_id is 1
- [x] get all fav plants for current user 
    - make a sqlalchmey user_obj using the user_id from the url (query your db for user, by id)
    - `user_obj.favourite_plants` --assuming user_obj is a sqlalcmey user object, you can use the relationship you made in the model 
- [x] use jinja to add all plants to the template (display the plants w/ jinja loop)
