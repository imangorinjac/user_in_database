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
    username = db.Column(db.String(80), unique=True, nullable=False, autoincrement=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):

        self.username = username
        self.password = password



@app.route("/", methods=["GET", "POST"])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    
    if username or password :
        user = User.query.filter_by(username=username,password=password).first()
        print('already taken')
        return render_template('login.html')

    if username is None or password is None :
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        return render_template('login.html')