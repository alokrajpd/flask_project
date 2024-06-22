from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Homepage</h1>"
@app.route("/welcome/steve")
def welcome_steve():
    return "<h1>Hey Steve Welcome to our Page</h1>"
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hey {name.title()} , Welcpme to this page</h1>"
if __name__ == "__main__":
    app.run(debug=True)