from flask import Flask, render_template, request, redirect 
import csv
import os

print("Templates path:", os.path.abspath("templates"))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    print("Contact route hit")
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

# 🔽 New routes for each solution page
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
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'contact': request.form['contact'],
            'message': request.form['message']
        }
        file_exists = os.path.isfile('submissions.csv')

        with open('submissions.csv', 'a', newline='') as csvfile:
            fieldnames = ['name', 'email', 'contact', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()

            writer.writerow(data)

        return redirect('/thankyou')

@app.route('/thankyou')
def thank_you():
    return "<h2>Thank you! Your message has been received.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
