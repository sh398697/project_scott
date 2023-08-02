from flask import Flask
from datetime import date, datetime, timedelta
from models import db, User
from app import app

if __name__ == '__main__':
    with app.app_context():
        
        print("Starting seed...")

        # Delete existing records
        User.query.delete()

        # Create Users
        scott = User(fname="Scott", lname="Henry", email="scotthenry1@gmail.com", phone="513-227-9750", password="test", image_url="")
        scott.set_password("test")

        db.session.add(scott)
        
        rachel = User(fname="Rachel", lname="Brusky", email="bruskr@d-e.org", phone="917-699-4370", password="test", image_url="")
        scott.set_password("test")

        db.session.add(rachel)

        # Commit the session to the database
        db.session.commit()

        print("Seeding complete!")
