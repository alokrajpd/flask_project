from flask import Flask , render_template,url_for
from data import employee_data
# create the flask app
app = Flask(__name__)

# home page
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html" , title ="Homepage")


# about page
@app.route("/about")
def about():
	return render_template("about.html" , title ="About")

@app.route("/evaluate/<int:num>")
def evaluate(num):
	return render_template("evaluate.html" , title ="Evaluate" , number =num)

@app.route("/employee")
def employee():
	return render_template("employee.html" , title ="Employee" , emps = employee_data)
# start the app
if __name__ == "__main__":
	app.run(debug=True)