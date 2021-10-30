from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registration.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "random string"
db = SQLAlchemy(app)


class User(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):

        self.username = username
        self.password = password


db.create_all()


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "GET":

        return render_template("login.html")
    else:
        name = request.form["name"]
        password = request.form["password"].encode("utf-8")
        user = User.query.filter_by(username=f"{login}").first()
        if user == None:
            return "Non-Existing User"
        else:
            if bcrypt.checkpw(password, user.password.encode("utf-8")):
                login_user(user)
                return "Success"
            else:
                return "Bad creds."
