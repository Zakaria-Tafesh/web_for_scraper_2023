from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return redirect(url_for('success'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)