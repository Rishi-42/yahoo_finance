from models import db, Subscription
import yfinance as yf
import smtplib, os
from twilio.rest import Client
from datetime import date
from dotenv import load_dotenv



def check_prices(app):
  with app.app_context():  
    subscriptions = Subscription.query.all()
    for sub in subscriptions:
        ticker = yf.Ticker(sub.stock_ticker)
        # print(ticker)
        data = ticker.history(period='1d')
        # print(data)
        price = data['Close'][0]
        freq = sub.freq
        T_date = date.today()
        print(T_date)
        L_resp = sub.last_response_sendday
        print(L_resp)
        if L_resp != T_date and freq=="ED":
          print("inside daily")
          if price >= sub.price_threshold:
              if sub.ntype == 'mail':
                  print("Email send")
                  send_email(sub.email, f"The stock price of {sub.stock_ticker} has reached the threshold of {sub.price_threshold}")
                  sub.last_response_sendday=T_date
                  db.session.commit()
              elif sub.ntype == 'sms':
                  print("message send")
                  sub.last_response_sendday=T_date
                  db.session.commit()
                  send_text(sub.phonenumber, f"Reached the threshold of {sub.price_threshold}")
        if freq =="EH":
           print("inside hourly")
           if price >= sub.price_threshold:
              if sub.ntype == 'mail':
                  print("Email send")
                  sub.last_response_sendday=T_date
                  db.session.commit()
                  send_email(sub.email, f"The stock price of {sub.stock_ticker} has reached the threshold of {sub.price_threshold}")
                  
              elif sub.ntype == 'sms':
                  print("sms send")
                  sub.last_response_sendday=T_date
                  db.session.commit()
                  send_text(sub.phonenumber, f"Reached the threshold of {sub.price_threshold}")
           
# define the functions to send email and text notifications
def send_email(to, message):
    from_email = os.environ.get('mail_address')
    password = os.environ.get('password')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(from_email, password)
        subject = "Stock price threshold reached"
        body = message
        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(from_email, to, msg)

def send_text(to, message):
    ''' The two arguments has the receiver phone number
        and the message need to be send. 
        The from is the trial phone number provided by the Twilio api.
    '''
    account_sid = os.environ.get('account_sid')  # Sid Provided by API
    auth_token  = os.environ.get('auth_token')  #provided by api
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=f"+977{to}",
        from_="+15076903775", # virtual number provided by api.
        body=message)
