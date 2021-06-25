from flask import Flask, render_template, url_for, redirect, request
import csv
# from flask.wrappers import Request
# from werkzeug.utils import redirect         #########pip install virtualenv ####virtualenv env
#db = SQLAlchemy(app)                      ##########.\env\Scripts\activate.ps1
app = Flask(__name__) 

@app.route('/')
@app.route('/index.html')
def index():
    print((url_for('static', filename='fav.ico')))
    return render_template('index.html')

@app.route('/submit_form', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            message = 'Thanks for filling out our form, We will look over your message and get back to you shortly.'
            return render_template('thankyou.html', message=message)
        except:
            message = 'Sorry something went wrong !! Please submit again!'
            return render_template('thankyou.html', message=message)
    else:
        message = "Form not submitted!! Please try again!"
        return render_template('thankyou.html',message=message)

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

def write_data_csv(data):
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('db.csv', 'a', newline='')as csvfile:
        db_writer = csv.writer(csvfile, delimiter='|', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([name,email,subject,message])

if __name__ == "__main__":
    app.run(debug=False)
