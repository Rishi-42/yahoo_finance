from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from models import db, Subscription
from notification import check_prices

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Finance.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# database initilaization
db.init_app(app)
app.app_context().push()

scheduler = BackgroundScheduler(daemon=True)
scheduler.start()
scheduler.add_job(func=check_prices, args=[app], trigger='interval', minutes=60) # job scheduled

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phonenumber = request.form['phonenumber']
        email = request.form['email']
        stock_ticker = request.form['stock_ticker']
        price_threshold = request.form['price_threshold']
        freq = request.form['freq']
        ntype = request.form['ntype']
        print(phonenumber, email, stock_ticker, price_threshold, ntype, freq)
        if not phonenumber and not email:
          error = 'Please fill out all the fields'
          return render_template('index.html', error=error)
        check_phonenumber = Subscription.query.filter_by(phonenumber=phonenumber)
        check_email = Subscription.query.filter_by(email=email).first()
        if (check_phonenumber is not None) and (check_email is not None):
           error = "Already exists"
           return render_template('index.html', error=error)
        subscription = Subscription(phonenumber=phonenumber, email=email, stock_ticker=stock_ticker, 
                                    price_threshold=price_threshold, ntype=ntype, freq=freq)
        db.session.add(subscription)
        db.session.commit()
        return 'Thanks for submitting the form!' 
    else:
        return render_template('index.html')

if __name__ == "__main__":
  db.create_all()
  app.run(debug=True, host='0:0:0:0')