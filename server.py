from flask import Flask, render_template, request, flash, session, redirect
import crud
import model 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'abcdefgz'
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html", logged_in=False)

@app.route("/newuser", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html", logged_in=False)

@app.route("/newuser", methods=["POST"])
def create_account():
    """Form on loging page to create a new account"""

    first_name = request.form.get("first_name")
    username = request.form.get("username")
    email = request.form.get("new_email")
    password = request.form.get("new_password")
    user = None

    try:
        user = crud.create_user(first_name, username, email, password)
    
    except: 
        pass
    
    if user:
        flash("Your account was created successfully! You can now log in")
        
        session['user_id'] = user.user_id
        session['username'] = user.username
        return redirect ("/favourite_plant")
    
    else:
        flash("--ERROR--", "Email already exists!. Make an account with a different email")

    return redirect ("/newuser")

@app.route('/login', methods=["POST"])
def previous_user():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user=crud.verify_user(email, password)

    if password == '' or email =='':
        flash('--ERROR--', 'log in failed, Try again')
        return redirect ('/newuser')
    
    elif not user or user.password != password:
        flash("--ERROR--", "Log in failed", "The email or password is incorrect. Try again")
        return redirect ('/newuser')

    elif user:
        session['email'] = user.email
        session['username']=user.username
        session['user_id']=user.user_id
        flash(u'Welcome back!')
        return redirect("/users/favourite_plants")


@app.route("/favourite_plant", methods=["POST"])
def favourite_plant():
    """This allows users to favourite a plant and add it to the db"""

    plant_id = request.form.get("plant_id")
    name = request.form.get("name")
    print ("*"*20)
    print (f'plant_id = {plant_id} plant name = {name}')
    print ("*"*20)
    crud.adding_plant(plant_id, name)
    crud.favourite_a_plant(user_id=session['user_id'], plant_id=plant_id)
    flash("Successfully added to your favourites!")
    return ('/searching')

@app.route("/users/favourite_plants")
def favourite_page():
    """this route displays the user's favourited plants"""
    user_id=session['user_id']
    # if 'user_id' in session:
    fav_plants = crud.get_plants_by_user(user_id)
    
    return render_template('user_favs.html', user=session['username'], plants=fav_plants, logged_in=True)
    # else:
    #     flash(u'Please log in to view this page', 'error-message')
    #     return redirect('/')

@app.route("/searching")
def search():
    
    return render_template("search.html", logged_in=True)

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('user_id', None)
    
    return ("hooray, logged out")


if __name__ == '__main__':
    model.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

    