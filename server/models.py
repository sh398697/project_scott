from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta

db = SQLAlchemy()
    
class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(100), nullable=False)
  lname = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)
  phone = db.Column(db.String(100))
  image_url = db.Column(db.String(300))
  password_hash = db.Column(db.String(128))


  def __init__(self, fname, lname, email, phone, password, image_url):
      self.fname = fname
      self.lname = lname
      self.email = email
      self.phone = phone
      self.image_url = image_url
      self.password_hash = generate_password_hash(password)
      
  def set_password(self, password):
      self.password_hash = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password_hash, password)

class Post(db.Model):
  __tablename__ = 'posts'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  title = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  