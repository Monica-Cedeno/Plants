from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("search.html")

@app.route("/response", methods=["POST"])
def response():
    username= request.form.get("username")
    email = request.form.get("email")
    return render_template("login.html", username=username, email=email)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    