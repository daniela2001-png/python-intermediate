from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"Drink(name={self.name}, description={self.description})"

@app.route("/")
def index():
    return "Hello"

@app.route("/drinks")
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return jsonify(output)

@app.route("/drinks/<id>")
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description }


@app.route("/drinks", methods=["POST"])
def create_drink():
    drink = Drink(name=request.json["name"], description=request.json["description"])
    db.session.add(drink) 
    db.session.commit()
    return jsonify({"status_code": 201})


@app.route("/drinks/<id>", methods=["DELETE"])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return jsonify({"status_code": 404})
    db.session.delete(drink) 
    db.session.commit()
    return jsonify({"status_code": 204})


@app.route("/drinks/<id>", methods=["PUT"])
def update_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return jsonify({"status_code": 404})
    drink.description = request.json["description"]
    db.session.commit()
    return jsonify({"status_code": 200})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=5001)