from flask import Flask, render_template, url_for

# appliation instance, used globally
app = Flask(__name__)

# the index view is hosted at both the root URL and /index URL 
@app.route('/')
@app.route('/index')
# generating HTML pages in py is very ugly
# hence render template will look in the templates folder for the file index.html
# flask (via render_template) will look in the folder templates for the file name given as its first argument
# this function below is a view function
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')    

if __name__ == '__main__':
    app.run(debug=True)    