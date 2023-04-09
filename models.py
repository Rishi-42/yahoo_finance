from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phonenumber = db.Column(db.Integer())
    email = db.Column(db.String(50))
    stock_ticker = db.Column(db.String(10), nullable=False)
    price_threshold = db.Column(db.Integer, nullable=False)
    freq = db.Column(db.String(10), nullable=False)
    ntype = db.Column(db.String(10), nullable=False)
    last_response_sendday = db.Column(db.Date)