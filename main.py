# created by Vincent Munyalo

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/rankings')
def rankings():
    return render_template('rankings.html')

@app.route('/universities')
def universities():
    return render_template('universities.html')

@app.route('/collections')
def collections():
    return render_template('collections.html')

@app.route('/subjects')
def subjects():
    return render_template('subjects.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)