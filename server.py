from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
# read flask documentation to get started Installation and Quickstart
# pip install Flask


####### how to get environment started so we can look at it on the server#######
# $env:FLASK_APP="server.py"
# $env:FLASK_ENV="development"
# flask run
################################################

# @app.route('/')  # decorator
# def hello_world():
#     return 'Hello, Traniel!'


@app.route('/index.html')  # decorator
def my_home():
    # render_template is also looking for a templates folder, so we need to create a templates folder and move the index.html
    return render_template('index.html')


# @app.route('/<username>')  # decorator
# def hello_world(username=None):
#     return render_template('index.html', name=username)


@app.route('/<string:page_name>')  # decorator
def html_page(page_name):
    # render_template is also looking for a templates folder, so we need to create a templates folder and move the index.html
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['subject']
#         file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['subject']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did NOT save to database'
    else:
        return 'Something went wrong, try again.'

    # the code below is executed if the request method
    # was GET or the credentials were invalid


###################### creating routes one by one #####################################

# @app.route('/components.html')  # decorator
# def components():
#     return render_template('components.html')


# @app.route('/work.html')  # decorator
# def work():
#     return render_template('work.html')


# @app.route('/works.html')  # decorator
# def works():
#     return render_template('works.html')


# @app.route('/contact.html')  # decorator
# def contact():
#     return render_template('contact.html')
