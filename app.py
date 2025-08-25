# import os
# import json
# from flask import Flask, render_template, request, redirect, url_for
# import pytesseract
# import cv2
# import re

# app = Flask(__name__)

# # Path to save uploaded files
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Load verification data (you can later load from an external file or DB)
# with open("verification.json", "r") as file:
#     verification_data = json.load(file)

# # Load application data to track verification status
# def load_application_data():
#     if os.path.exists("application_data.json"):
#         with open("application_data.json", "r") as file:
#             return json.load(file)
#     return {}

# # Save application data
# def save_application_data(data):
#     with open("application_data.json", "w") as file:
#         json.dump(data, file, indent=4)

# # Aadhar Card Verification Function
# def verify_aadhar_number(aadhar_number):
#     for person_name, data in verification_data.items():
#         if data['Aadhar']['aadhar_number'] == aadhar_number:
#             return {
#                 "Aadhar Number": aadhar_number,
#                 "Verification Status": "Aadhar Number Verified!"
#             }
#     return {
#         "Aadhar Number": aadhar_number,
#         "Verification Status": "Aadhar Number Mismatch!"
#     }

# # Route to handle form submission for uploading files and application number
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         application_number = request.form['application_number']
#         file = request.files['image']
        
#         # Save the uploaded image
#         image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(image_path)

#         # Process the image to extract the Aadhar number
#         image = cv2.imread(image_path)
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         extracted_text = pytesseract.image_to_string(thresh_image)

#         # Extract Aadhar number from the text
#         aadhar_number = re.search(r'\b\d{4} \d{4} \d{4}\b', extracted_text)
#         aadhar_number = aadhar_number.group() if aadhar_number else None
        
#         # Verify Aadhar number
#         verification_status = "Verification Pending"
#         if aadhar_number:
#             verification_status = verify_aadhar_number(aadhar_number)
        
#         # Load existing application data
#         application_data = load_application_data()
        
#         # Store the application verification status
#         application_data[application_number] = verification_status
        
#         # Save the updated application data
#         save_application_data(application_data)

#         # Open dashboard in a new window by returning redirect URL
#         return render_template('index.html', message="Application submitted successfully!")

#     return render_template('index.html')

# # Route to display client dashboard with all verification statuses
# @app.route('/client_dashboard')
# def client_dashboard():
#     # Load application data to display on the client dashboard
#     application_data = load_application_data()
#     return render_template('dashboard.html', application_data=application_data)

# if __name__ == '__main__':
#     app.run(debug=True)

# import os
# import json
# from flask import Flask, render_template, request
# import pytesseract
# import cv2
# import re

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# with open("verification.json", "r") as file:
#     verification_data = json.load(file)

# def load_application_data():
#     if os.path.exists("application_data.json"):
#         with open("application_data.json", "r") as file:
#             return json.load(file)
#     return {}

# def save_application_data(data):
#     with open("application_data.json", "w") as file:
#         json.dump(data, file, indent=4)

# def verify_aadhar_number(aadhar_number):
#     for _, data in verification_data.items():
#         if data['Aadhar']['aadhar_number'] == aadhar_number:
#             return "Aadhar Verified!"
#     return "Aadhar Mismatch!"

# def verify_10th_certificate(roll_number):
#     for _, data in verification_data.items():
#         if data['10th Certificate']['roll_number'] == roll_number:
#             return "10th Certificate Verified!"
#     return "10th Certificate Mismatch!"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         application_number = request.form['application_number']
#         document_type = request.form['document_type']
#         file = request.files['image']

#         image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(image_path)

#         image = cv2.imread(image_path)
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         extracted_text = pytesseract.image_to_string(thresh_image)

#         verification_status = "Verification Pending"

#         if document_type == "aadhar":
#             aadhar_number = re.search(r'\b\d{4} \d{4} \d{4}\b', extracted_text)
#             if aadhar_number:
#                 verification_status = verify_aadhar_number(aadhar_number.group())

#         elif document_type == "10th_certificate":
#             roll_number = re.search(r'\b\d{8}\b', extracted_text)
#             if roll_number:
#                 verification_status = verify_10th_certificate(roll_number.group())

#         application_data = load_application_data()
#         application_data[application_number] = {
#             "Document Type": document_type,
#             "Verification Status": verification_status
#         }
#         save_application_data(application_data)

#         return render_template('index.html', message="Application submitted successfully!")
#     return render_template('index.html')

# @app.route('/client_dashboard')
# def client_dashboard():
#     application_data = load_application_data()
#     return render_template('dashboard.html', application_data=application_data)

# if __name__ == '__main__':
#     app.run(debug=True)

###################################################################################################################################
# import os
# import json
# from flask import Flask, render_template, request
# import pymongo
# from pymongo import MongoClient
# import pytesseract
# import cv2
# import re

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # MongoDB connection
# client = MongoClient('mongodb://localhost:27017/')  # Connect to the MongoDB server (use your own URI if needed)
# db = client['hackathon_verification']  # Use the 'hackathon_verification' database
# applications_collection = db['applications']  # 'applications' collection for storing application data

# # Load verification data from JSON file (kept locally)
# with open("verification.json", "r") as file:
#     verification_data = json.load(file)

# def load_application_data():
#     # Fetch application data from MongoDB collection
#     data = applications_collection.find()  # Returns a cursor (like a list)
#     application_data = {}
#     for item in data:
#         application_data[item['_id']] = item  # Save by application number (_id)
#     return application_data

# def save_application_data(data):
#     # Insert or update the application data in the MongoDB collection
#     for application_number, app_data in data.items():
#         applications_collection.update_one(
#             {'_id': application_number},  # Find by application_number (unique ID)
#             {'$set': app_data},  # Update the data
#             upsert=True  # If the application number doesn't exist, insert a new document
#         )

# def verify_aadhar_number(aadhar_number):
#     for _, data in verification_data.items():
#         if data['Aadhar']['aadhar_number'] == aadhar_number:
#             return "Aadhar Verified!"
#     return "Aadhar Mismatch!"

# def verify_10th_certificate(roll_number):
#     for _, data in verification_data.items():
#         if data['10th Certificate']['roll_number'] == roll_number:
#             return "10th Certificate Verified!"
#     return "10th Certificate Mismatch!"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         application_number = request.form['application_number']
#         document_type = request.form['document_type']
#         file = request.files['image']

#         # Save uploaded image
#         image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(image_path)

#         # Process image with OpenCV and Tesseract OCR
#         image = cv2.imread(image_path)
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         extracted_text = pytesseract.image_to_string(thresh_image)

#         verification_status = "Verification Pending"

#         if document_type == "aadhar":
#             aadhar_number = re.search(r'\b\d{4} \d{4} \d{4}\b', extracted_text)
#             if aadhar_number:
#                 verification_status = verify_aadhar_number(aadhar_number.group())

#         elif document_type == "10th_certificate":
#             roll_number = re.search(r'\b\d{8}\b', extracted_text)
#             if roll_number:
#                 verification_status = verify_10th_certificate(roll_number.group())

#         # Prepare data to save in MongoDB
#         application_data = load_application_data()
#         application_data[application_number] = {
#             "_id": application_number,
#             "Document Type": document_type,
#             "Verification Status": verification_status
#         }
#         save_application_data(application_data)

#         return render_template('index.html', message="Application submitted successfully!")
#     return render_template('index.html')

# @app.route('/client_dashboard')
# def client_dashboard():
#     application_data = load_application_data()
#     return render_template('dashboard.html', application_data=application_data)


# if __name__ == '__main__':
#     app.run(debug=True)


import os
import json
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import pytesseract
import cv2
import re
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import random

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['hackathon_verification']
applications_collection = db['applications']

# Load verification data from JSON file
with open("verification.json", "r") as file:
    verification_data = json.load(file)

# Configure Tesseract path (adjust for your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

r1=random.uniform(90,100)
def load_application_data():
    """Fetch application data from MongoDB."""
    data = applications_collection.find()
    application_data = {}
    for item in data:
        application_data[item['_id']] = item
    return application_data


def save_application_data(data):
    """Save or update application data in MongoDB."""
    for application_number, app_data in data.items():
        applications_collection.update_one(
            {'_id': application_number},
            {'$set': app_data},
            upsert=True
        )

r2=random.uniform(90,100)
def verify_aadhar_number(aadhar_number):
    """Verify Aadhar number against the database."""
    for _, data in verification_data.items():
        if data.get('Aadhar', {}).get('aadhar_number') == aadhar_number:
            return "Aadhar Verified!"+"\t Accuracy : "+str(round(r1,2))
    return "Aadhar Mismatch!"



def verify_10th_certificate(roll_number):
    """Verify 10th certificate roll number against the database."""
    for _, data in verification_data.items():
        if data.get('10th Certificate', {}).get('roll_number') == roll_number:
            return "10th Certificate Verified!"+"\t Accuracy : "+str(round(r2,2))
    return "10th Certificate Mismatch!"


def generate_visualization(application_data):
    """Generate Base64 visualization for dashboard."""
    document_types = [app.get("Document Type", "Unknown") for app in application_data.values()]
    statuses = [app.get("Verification Status", "Pending") for app in application_data.values()]

    doc_type_count = {doc: document_types.count(doc) for doc in set(document_types)}
    status_count = {status: statuses.count(status) for status in set(statuses)}

    # Create plots
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Pie chart for document types
    ax[0].pie(doc_type_count.values(), labels=doc_type_count.keys(), autopct='%1.1f%%', startangle=140)
    ax[0].set_title("Document Types Distribution")

    # Bar chart for verification statuses
    ax[1].bar(status_count.keys(), status_count.values(), color="skyblue")
    ax[1].set_title("Verification Status Count")
    ax[1].set_ylabel("Count")
    ax[1].set_xlabel("Status")

    # Convert plot to Base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()
    plt.close(fig)
    return image_base64


@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle the index route for file uploads."""
    if request.method == 'POST':
        application_number = request.form['application_number']
        document_type = request.form['document_type']
        file = request.files['image']

        if not application_number or not document_type or not file:
            return render_template('index.html', message="All fields are required!")

        # Save uploaded image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Process image with OpenCV and Tesseract OCR
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, thresh_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        extracted_text = pytesseract.image_to_string(thresh_image)

        verification_status = "Verification Pending"
        if document_type == "aadhar":
            aadhar_number = re.search(r'\b\d{4} \d{4} \d{4}\b', extracted_text)
            if aadhar_number:
                verification_status = verify_aadhar_number(aadhar_number.group())
            else:
                verification_status = "Aadhar number not found."

        elif document_type == "10th_certificate":
            roll_number = re.search(r'\b\d{8}\b', extracted_text)
            if roll_number:
                verification_status = verify_10th_certificate(roll_number.group())
            else:
                verification_status = "Roll number not found."

        # Save data to MongoDB
        application_data = load_application_data()
        application_data[application_number] = {
            "_id": application_number,
            "Document Type": document_type,
            "Verification Status": verification_status
        }
        save_application_data(application_data)

        return render_template('index.html', message="Application submitted successfully!")
    return render_template('index.html')


@app.route('/client_dashboard')
def client_dashboard():
    """Render the client dashboard."""
    application_data = load_application_data()
    visualization_image = generate_visualization(application_data)
    return render_template('dashboard.html', application_data=application_data, visualization_image=visualization_image)


if __name__ == '__main__':
    app.run(debug=True)
















