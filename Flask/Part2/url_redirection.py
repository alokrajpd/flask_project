from flask import Flask , redirect , url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> welcome to Homepage</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname ,marks):
    return f"<h1>Hey {sname} Congrats You have passed scoring {marks}</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1> {sname}Sorry You have failed  scoring {marks}</h1>"
@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        return redirect(url_for("failed" ,sname=name , marks=num ))
    else:
        return redirect(url_for("passed",sname=name , marks=num))


if __name__ == "__main__":
    app.run(debug=True)