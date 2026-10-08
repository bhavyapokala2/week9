from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('myForm.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    return render_template('greeting.html', username=username, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)