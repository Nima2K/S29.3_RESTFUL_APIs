
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
 
def connect_db(app):
    db.app=app
    db.init_app(app)


class Cupcake(db.Model):
    """ Cupcakes Model """

    def serialize(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

    @classmethod
    def create_cupcake(cls,f,s,r,i):
        new = cls(flavor=f,size=s,rating=r,image=i)
        db.session.add(new)
        db.session.commit()
        return new.id


    ___tablename___="cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default="https://tinyurl.com/demo-cupcake")