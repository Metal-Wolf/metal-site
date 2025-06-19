from flask import Flask, render_template, request,redirect
import csv

app = Flask(__name__)

def write_to_csv(data):
    with open('database.csv', mode='a+', newline='') as database2:
        fname = data.get('fname', '')
        lname = data.get('lname', '')
        email = data.get('email', '')
        subject = data.get('subject', '')
        message = data.get('message', '')
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fname,lname,email, subject, message])

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        # Optionally, you can render a thank you message or the same page with a success message
        return render_template('index.html', success=True)
    return render_template('index.html', success=False)