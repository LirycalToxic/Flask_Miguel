from app import mail
from flask_mail import Message
from app import app
with app.app_context():
    msg = Message('test subject', sender=app.config['ADMINS'][0], recipients=['xaccaope@gmail.com'])
    msg.body = 'text body'
    msg.html = '<h1>HTML text</h1>'
    mail.send(msg)
