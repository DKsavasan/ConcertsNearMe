from flask import Flask, render_template

app = Flask(__name__)

# This tells Flask to serve the static files from the 'static' folder
app.static_folder = 'static'

@app.route('/')
def auth():
    return render_template('auth.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
