from flask import Flask, render_template, request, flash, session
import crud
import model 

app = Flask(__name__)

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("search.html")

@app.route("/newuser", methods=["POST"])
def create_account():
    """Form on loging page to create a new account"""

    first_name = request.form.get("first_name")
    username = request.form.get("username")
    email = request.form.get("new_email")
    password = request.form.get("new_password")
    user = crud.create_user(first_name, username, email, password)

    if user:
        flash("Email already exists!. Make an account with a different email")
    
    else:
        user = crud.create_user(first_name, username, email, password)
        flash("Your account was created successfully! You can now log in")
        session['user_id'] = user.user_id
        session['username'] = user.username
    return render_template("login.html")

# @app.route("/response", methods=["POST"])
# def response():
#     username= request.form.get("username")
#     email = request.form.get("email")
#     return render_template("login.html", username=username, email=email)

# @app.route("/login", methods=["POST"])

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
    return "yay"

@app.route("/users/<user_id>")
def favourite_page():
    
    return "stuff"

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('user_id', None)
    
    return ("hooray, logged out")




if __name__ == '__main__':
    model.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

    