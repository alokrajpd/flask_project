from flask import Flask , render_template , url_for , redirect

app=Flask(__name__)

from forms import SignupForm , LoginForm

app.config["SECRET_KEY"] ="this_is_a_secret_key"
@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html" , title="Home")
@app.route("/signup",methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        print("Hi")
        return redirect(url_for("home"))
    return render_template("signup.html" , title="Signup" , form=form)
@app.route("/login")
def login():
    form =LoginForm()
    return render_template("login.html" ,title="Login",form=form)
if __name__ == "__main__":
    app.run(debug=True)