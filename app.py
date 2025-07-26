from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"  # or your MongoDB Atlas URI
client = MongoClient(MONGO_URI)
db = client['stromex_database']
collection = db['contact_submissions']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('Blog.html')

@app.route('/products')
def products():
    return render_template('Products.html')

@app.route('/services')
def services():
    return render_template('Services.html')

@app.route('/solution')
def solution():
    return render_template('Solutions.html')

@app.route('/software-saas-applications')
def software_saas_applications():
    return render_template('software-saas-applications.html')

@app.route('/audio-video-solutions')
def audio_video_solutions():
    return render_template('audio-video-solutions.html')

@app.route('/end-user-computing')
def end_user_computing():
    return render_template('end-user-computing.html')

@app.route('/data-center-infrastructure')
def data_center_infrastructure():
    return render_template('data-center-infrastructure.html')

@app.route('/it-consulting-managed-services')
def it_consulting_managed_services():
    return render_template('it-consulting-managed-services.html')

@app.route('/cloud-colocation-services')
def cloud_colocation_services():
    return render_template('cloud-colocation-services.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        contact = request.form.get('contact')
        message = request.form.get('message')

        # Debugging: Print form data
        print(f"Received form data: {name}, {email}, {contact}, {message}")

        try:
            # Store data in MongoDB
            result = collection.insert_one({
                'name': name,
                'email': email,
                'contact': contact,
                'message': message
            })
            print("Data inserted with ID:", result.inserted_id)  # Log inserted ID

        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")  # Log any errors

       
        return redirect('/contact')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')  # Create this HTML page or return a simple message
    # return "<h2>Thank you for contacting us!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
