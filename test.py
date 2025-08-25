import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB URI if necessary

# Choose your database
db = client['hackathon_verification']

# Choose the collection for storing person data
people_collection = db['people']

# Sample data for people (use your full data here)
data = {

    "Mark Johnson": {
      "Aadhar": {
        "aadhar_number": "3234 5678 9012",
        "name": "Mark Johnson",
        "dob": "03/03/1995",
        "address": "789 Pine Road, City, Country"
      },
      "10th Certificate": {
        "roll_number": "3234567890",
        "name": "Mark Johnson",
        "school_name": "LMN High School",
        "passing_year": "2010",
        "board": "CBSE"
      },
      "12th Certificate": {
        "roll_number": "2987654321",
        "name": "Mark Johnson",
        "school_name": "XYZ Senior Secondary School",
        "passing_year": "2012",
        "board": "CBSE"
      }
    },
    "Emma Brown": {
      "Aadhar": {
        "aadhar_number": "4234 5678 9012",
        "name": "Emma Brown",
        "dob": "04/04/1997",
        "address": "101 Maple Lane, City, Country"
      },
      "10th Certificate": {
        "roll_number": "4234567890",
        "name": "Emma Brown",
        "school_name": "OPQ High School",
        "passing_year": "2012",
        "board": "ICSE"
      },
      "12th Certificate": {
        "roll_number": "3987654321",
        "name": "Emma Brown",
        "school_name": "PQR Senior Secondary School",
        "passing_year": "2014",
        "board": "ICSE"
      }
    },
    "Lucas Green": {
      "Aadhar": {
        "aadhar_number": "5234 5678 9012",
        "name": "Lucas Green",
        "dob": "05/05/2000",
        "address": "202 Birch Street, City, Country"
      },
      "10th Certificate": {
        "roll_number": "5234567890",
        "name": "Lucas Green",
        "school_name": "RST High School",
        "passing_year": "2015",
        "board": "CBSE"
      },
      "12th Certificate": {
        "roll_number": "4987654321",
        "name": "Lucas Green",
        "school_name": "STU Senior Secondary School",
        "passing_year": "2017",
        "board": "CBSE"
      }
    }
  }

# Function to insert data for each person into the collection
def insert_user_data(person_data):
    name = person_data["Aadhar"]["name"]  # Using name as identifier

    # Create a combined document with Aadhar, 10th and 12th data
    person_document = {
        "_id": person_data["Aadhar"]["aadhar_number"],  # Use Aadhar number as unique ID
        "name": name,
        "Aadhar": person_data["Aadhar"],
        "10th Certificate": person_data["10th Certificate"],
        "12th Certificate": person_data["12th Certificate"]
    }

    # Insert the document into the 'people' collection
    people_collection.insert_one(person_document)

    print(f"Data inserted for {name}.")

# Insert data for each person in the sample data
for person, person_data in data.items():
    insert_user_data(person_data)

print("All data inserted successfully.")
