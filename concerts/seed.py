from models import Base, Band, Venue, Concert

import os
from sqlalchemy.orm import sessionmaker, relationship, backref
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
sys.path.append(os.getcwd)

# Create an SQLite database engine and initialize the database schema
engine = create_engine('sqlite:///concerts.db', echo=True)
# Create a session factory bound to the engine
Session = sessionmaker(bind=engine)
session = Session()
# Initialize the Base for the models
Base = declarative_base()

# creating instances of classes to test code

# Creating band instances
band1 = Band(name="AJR", hometown="USA")
band2 = Band(name="Sauti Sol", hometown="Nakuru")
band3 = Band(name="UB40", hometown="Jamaica")

# Creating venue instances
venue1 = Venue(title="Sports club", city="Eldoret")
venue2 = Venue(title="Green Stadium", city="Kericho")
venue3 = Venue(title="Tottenham Stadium", city="London")

# Creating concert instances linking bands and venues
concert1 = Concert(name="AJR Live", date="2024-10-01", band=band1, venue=venue1)
concert2 = Concert(name="Sol Fest", date="2024-10-15", band=band2, venue=venue2)
concert3 = Concert(name="Reggae Experience", date="2024-10-20", band=band3, venue=venue3)

# Adding all instances to the session
session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3])

# Committing the session
session.commit()
session.close()

print("Seeding Successful...")