from flask import Flask, jsonify, request, redirect, render_template
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push() 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all() 

@app.route("/api/cupcakes")
def show_cupcakes():
    """Get data about all cupcakes"""

    cupcakes = Cupcake.query.all()
    all_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes = all_cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def show_cupcake(cupcake_id):
    """show data on a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.serialize())

@app.route("/api/cupcakes", methods = ["POST"])
def create_cupcake():
    """create a cupcake via POST method"""

    new_cupcake = Cupcake(flavor = request.json['flavor'], rating = request.json['rating'], 
                          size = request.json['size'], image = request.json["image"])

    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake = new_cupcake.serialize()), 201)

@app.route("/api/cupcakes/<int:cupcake_id>", methods = ["PATCH"])
def edit_cupcake(cupcake_id):
    """edit a cupcake in the system"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.add(cupcake)
    db.session.commit()
    return(jsonify(cupcake = cupcake.serialize()))

@app.route("/api/cupcakes/<int:cupcake_id>", methods = ["DELETE"])
def remove_cupcake(cupcake_id):
    """delete a cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()
    return(jsonify(message = "Deleted"))

@app.route("/")
def show_homepage():
    """show homepage"""

    return render_template("index.html")