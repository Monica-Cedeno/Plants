from flask import Flask, render_template, request, flash, session, redirect
import crud
import model 

app = Flask(__name__)

app.secret_key = 'abcdefgz'

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route("/newuser", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")

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
        return redirect ("/favs")
    
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

    if user:
        session['email'] = user.email
        session['password'] = user.password
        return redirect('/favs')

    else:
        flash("--ERROR--", "Log in failed", "Try again")
        return redirect ('/newuser')


@app.route("/favourite_plant", methods=["POST"])
def favourite_plant():
    plant_id = request.form.get("plant_id")
    name = request.form.get("name")
    print ("*"*20)
    print (f'plant_id = {plant_id} plant name = {name}')
    print ("*"*20)
    crud.adding_plant(plant_id, name)
    crud.favourite_a_plant(user_id=1, plant_id=plant_id) # TODO: user id is hardcoded, 
    # when login works, use user_id from session
    flash("Successfully added to your favourites!")
    return "yay"

@app.route("/favs")
def favourite_page():

    # if 'user_id' in session:
    fav_plants = crud.get_plants_by_user('1')
    return render_template('user_favs.html', user='Monica', plants=fav_plants)
    # else:
    #     flash(u'Please log in to view this page', 'error-message')
    #     return redirect('/')

@app.route("/searching")
def search():
    pass
    return render_template("search.html")

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('user_id', None)
    
    return ("hooray, logged out")


if __name__ == '__main__':
    model.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

    