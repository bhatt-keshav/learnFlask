from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, url_for, flash
# redirect library is used to redirect user to another page

# from logging import DEBUG ## Commented out since using flash()

# just creates an appliation instance, used globally
app = Flask(__name__)
## app.logger.setLevel(DEBUG) # commented out since app is no longer in debug mode

## Generating a secret key for flash()
# import os
# os.urandom(24) # key = '\xb5\x1e#\x15\x07\x9a\xc8XB\xa8\x95\x10B\xbf\x9auuh0\x81ML\xe2 '

bookmarks = []
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'


def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = 'keshav',
        datetime = datetime.utcnow()
    ))

# the index view is hosted at both the root URL and /index URL 
@app.route('/')
@app.route('/index')
# generating HTML pages in py is very ugly
# hence render template will look in the templates folder for the file index.html
# flask (via render_template) will look in the folder templates for the file name given as its first argument
# this function below is a view function
def index():
    return render_template('index.html')

# this will look in the templates folder for the file add.html
@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == "POST":
        # this url variable is present in the add.html file at: <input type="text" name="url">
        url = request.form['url']
        store_bookmark(url)
        # Logger Commented out since using flash()
        # app.logger.debug('stored url: ' + url) 
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    # render temp will look in the templates folder for the file add.html    
    return render_template('add.html')  

@app.errorhandler(404)
def page_not_found(e):
# the numeric argument to the tuple  400, sets the status code correctly to 400
    return render_template('404.html'), 404      

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500      

# this does nothing much, just boiler plate to start the flask service
if __name__ == '__main__':
    app.run(debug=True)    