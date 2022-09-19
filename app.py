from flask import *
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from valid_email import *
from send_mail import *

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload_csv", methods= ["GET", "POST"])
def verify_csv():

    if request.method == 'POST':

        file = request.files['file']
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_file = os.path.join('csv_files', new_filename)
            file.save(save_file)

            output_file = check_mail(save_file)

        # return 'uploaded'

        # return invalid_email


    return render_template('single.html', invalidmail = invalid_email)

@app.route("/send-mail")
def send_mail():

    return render_template('single.html')

if __name__ == "__main__":

    app.run(host='0.0.0.0', port='5000', debug=True)    