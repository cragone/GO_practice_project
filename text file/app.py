from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("home.html")

@app.route('/compare', methods=['POST'])
def compare():
    # Your file comparison logic here
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
