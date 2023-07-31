import os
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime, timedelta
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User

# Instantiate app, set attributes
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.config['JWT_SECRET_KEY'] = '2b5faaf05ca77b1e23aa9f3e1c05d840'

db.init_app(app)

# Use this to create your tables
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

CORS(app)

jwt = JWTManager(app)

####################################################################################################

@app.route("/")
def hello():
  return "Scott's API is running!"

@app.route("/users", methods=['GET'])
def get_users():
  users = []
  for user in User.query.all():
    user_dict = {
                  "id": user.id,
                  "fname": user.fname,
                  "lname": user.lname,
                  "email": user.email,
                  "phone": user.phone,
                  "image_url": user.image_url
                  }
    users.append(user_dict)
  
  response = make_response(
        users,
        200,
        {"Content-Type": "application/json"}
    )
  return response

@app.route("/users", methods=['POST'])
def create_user():
  data = request.get_json()
  user = User(fname=data['fname'], lname=data['lname'], email=data['email'], phone=data['phone'], image_url=data['image_url'], password=data['password'])
  user_dict = {
                  "fname": user.fname,
                  "lname": user.lname,
                  "email": user.email,
                  "phone": user.phone,
                  "password": user.password_hash,
                  "image_url": user.image_url
                  }
  db.session.add(user)
  db.session.commit()
  response = make_response(
        user_dict,
        201,
        {"Content-Type": "application/json"}
    )
  return response
    



@app.route('/login', methods=['POST'])
def login():
  email = request.json.get('email')
  password = request.json.get('password')
  user = User.query.filter_by(email=email).first()
  if not user or not user.check_password(password):
    return make_response(
      {"error": "Invalid email or password"},
      401,
      {"Content-Type": "application/json"}
    )
  token = create_access_token(identity=user.id)
  response = make_response(
  {"token": token},
  200,
  {"Content-Type": "application/json"}
  )
  # Set the cookie with an expiration time of 24 hours
  expires = datetime.now() + timedelta(days=1)
  response.set_cookie("token", token, expires=datetime.utcnow() + timedelta(days=1))
  return response




@app.route('/get-user-data', methods=['GET'])
@jwt_required()
def get_user_data():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user:
        user_dict = {
            "id": user.id,
            "fname": user.fname,
            "lname": user.lname,
            "email": user.email,
            "phone": user.phone,
            "image_url": user.image_url
        }
        response = make_response(
            user_dict,
            200,
            {"Content-Type": "application/json"}
        )
    else:
        response = make_response(
            {"error": "User not found"},
            404,
            {"Content-Type": "application/json"}
        )

    return response
  



@app.route('/logout', methods=['POST'])
def logout():
  
  response = make_response(
    {"message": "Successfully logged out"},
    200,
    {"Content-Type": "application/json"}
  )
  # Set the cookie with an expiration time of 24 hours
  expires = datetime.now() - timedelta(days=1)
  response.set_cookie("token", "", expires=expires)
  return response


####################################################################################################

if __name__ == "__main__":
  app.run()
