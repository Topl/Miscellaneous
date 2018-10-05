from flask import Flask, render_template
from testModelDB import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def hello():
    db.drop_all()
    db.create_all()
    db.session.add(User("John Doe", "john.doe@example.com"))
    db.session.add(User("Bill Smith", "smith.bill@example.com"))
    db.session.commit()
    all_users = User.query.all()
    return render_template('index.html', all_users=all_users)

if __name__ == "__main__":
    app.run(debug=True)