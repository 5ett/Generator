from recapp import db, daimyou
from datetime import datetime
from flask_login import UserMixin


@daimyou.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    profile_photo = db.Column(db.String, nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.username})"


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudo_id = db.Column(db.String, unique=True, nullable=False)
    belongs_to = db.Column(db.String, nullable=False)
    form_type = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    subtotal = db.Column(db.Float, nullable=False, default=0.00)
    vat = db.Column(db.Float, nullable=False, default=0.00)
    total_sum = db.Column(db.Float, nullable=False, default=0.00)
    no_items = db.Column(db.Integer, nullable=False, default=0)
    issuance_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow())

    items = db.relationship('Storage', backref='pocket', lazy=True)

    def __repr__(self):
        return f"Ticket({self.id}, {self.pseudo_id}, {self.form_type}, {self.status})"


class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, nullable=False)
    item_quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    ticket_link = db.Column(
        db.Integer, db.ForeignKey('ticket.id'), nullable=False)

    def __repr__(self):
        return f"Storage({self.id}, {self.item_name}, {self.unit_price}, {self.total_price})"
