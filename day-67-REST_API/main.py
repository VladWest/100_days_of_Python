from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
# View documentation on https://documenter.getpostman.com/view/8522449/2s8YmRNM4j
# #Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# #Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

# # HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def choice_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })


@app.route("/all", methods=["GET"])
def show_all_cafes():
    cafes = db.session.query(Cafe).all()
    cafes_list = []
    for cafe in cafes:
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        cafes_list.append(cafe_dict)
    return jsonify(cafes_list)


@app.route("/search", methods=["GET"])
def search_by_location():
    query_location = request.args.get("location")
    cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    if cafes:
        cafes_list = []
        for cafe in cafes:
            cafe_dict = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
            }
            cafes_list.append(cafe_dict)
        return jsonify(cafes_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# # HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# # HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def coffee_price_update(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(responce={
            "success": "Successfully updated the prise."
        })
    else:
        return jsonify(responce={
            "Not found": "Sorry a cafe with that id was not found in the database."
        })


# # HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    users_api_key = request.args.get("api_key")
    api_key = "TopSecretAPIKey"
    cafe_to_delete = Cafe.query.get(cafe_id)
    if cafe_to_delete:
        if users_api_key == api_key:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(responce={
                "success": "The Cafe was successfully deleted from DB."
            })
        else:
            return jsonify(responce={
                "error": "Sorry, that is not allowed. Make sure you have the correct api_key."
            })
    else:
        return jsonify(responce={
            "Not found": "Sorry a cafe with that id was not found in the database."
        })


if __name__ == '__main__':
    app.run(debug=True)
