from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/googlea82ba51b2fe720e3.html')
def google_verification():
    return send_from_directory(app.root_path, 'googlea82ba51b2fe720e3.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
