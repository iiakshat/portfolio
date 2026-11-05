from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/googlea82ba51b2fe720e3.html')
def google_verification():
    return Response('google-site-verification: googlea82ba51b2fe720e3.html', mimetype='text/html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
