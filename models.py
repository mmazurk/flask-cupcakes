from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """This sets up a connection between a Flask application and a database."""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """This object represents a Pet in our adoption app"""

    __tablename__ = "cupcake_table"

    cupcake_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)
    flavor = db.Column(db.String(20),
                       nullable=False)
    size = db.Column(db.String(20),
                     nullable=False)
    rating = db.Column(db.Float, default = 99)
    image = db.Column(db.String(200), default = "https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg")

    def serialize(self):
        """Serializes the Cupcake model"""

        return {
            'cupcake_id': self.cupcake_id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }