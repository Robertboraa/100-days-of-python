from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random




app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafee():

    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe= random_cafe.to_dict())

@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search_cafes():
    location = request.args.get('loc')
    cafe = db.session.execute(db.select(Cafe).where(Cafe.location == location.capitalize())).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafe])

# HTTP POST - Create Record
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

# HTTP PUT/PATCH - Update Record (http://127.0.0.1:5000/update-price/1?new_price=£4.50)
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    cafe.coffee_price = request.form.get("coffee_price")
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."})


# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key== "TopSecretAPIKey":
        try:
            cafe = db.session.get(Cafe, cafe_id)
        except  AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})
    else :
        return jsonify(response={"Forbidden": "You are not authorized to perform this action."}), 403
if __name__ == '__main__':
    app.run(debug=True)
