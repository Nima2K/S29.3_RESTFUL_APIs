from flask import Flask, jsonify, request
from models import connect_db, db, Cupcake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.app_context().push()
connect_db(app)
db.create_all()






@app.route("/")
def home():
    return "Hello"


# API
@app.route("/api/cupcakes")
def get_all_cupcakes():

    return jsonify(cupcakes=[c.serialize() for c in Cupcake.query.all()])

@app.route("/api/cupcakes/<cupcake_id>")
def get_cupcake(cupcake_id):

    return jsonify(cupcake=Cupcake.query.get_or_404(cupcake_id).serialize())

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]
    id = Cupcake.create_cupcake(flavor,size,rating,image)
    return (jsonify(cupcake=Cupcake.query.get_or_404(id).serialize()), 201)

@app.route("/api/cupcakes/<cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    flavor = request.json.get('flavor', cupcake.flavor)
    size = request.json.get('size', cupcake.size)
    rating = request.json.get('rating', cupcake.rating)
    image = request.json.get('image', cupcake.image)
    id = cupcake.update_cupcake(flavor,size,rating,image)
    return jsonify(cupcake=Cupcake.query.get_or_404(id).serialize())

@app.route("/api/cupcakes/<cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    id = cupcake.delete_cupcake()

    return jsonify(message="Deleted")