from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        print("DB barebone created..", self.id)

@app.route('/')
def default():
    return "Hello!"




if __name__ == "__main__":
    app.run(debug=True)