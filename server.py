import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index' + '.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# dynamic way of having multiple routes. in future if we add any route, no extra code is required here
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + '.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        write_to_db_file(data)  # if we want to save data in txt file
        write_to_csv(data)  # if we want to save data in an excel(better option bcoz it's formatted and easy to read)
        return render_template("thankyou.html")
    else:
        return "something went wrong. Please try again!!!"


def write_to_db_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# commands while running this proj
# $env:FLASK_APP = "server.py"
# flask run
# $env:FLASK_ENV = "development" # to run in debug mode so that server restart is not required after every change


# NOTE: for html files, we need to put it in templates folder bcoz render template looks for templates
# folder to look out for html files
