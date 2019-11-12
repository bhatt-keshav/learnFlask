from flask import Flask, render_template, url_for

app = Flask(__name__)

# the index view is hosted at both the root URL and /index URL 
@app.route('/')
@app.route('/index')
# generating HTML pages in py is very ugly, hence render template will look in the templates folder for the file index.html
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)    