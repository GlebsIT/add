from app import db

class Logic(db.Model):
    __tablename__ = 'products'
    id_logic = db.Column(db.Integer, primary_key=True)
    id_parents = db.Column(db.String(64))
    response = db.Column(db.String(120))
    template = db.Column(db.String(128))

    def __repr__(self):
        return '<Response {}>'.format(self.response)