from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Home'
    content = 'Welcome to my website!'
    return render_template('index.html', title=title, content=content)

if __name__ == '__main__':
    app.run(debug=True)
