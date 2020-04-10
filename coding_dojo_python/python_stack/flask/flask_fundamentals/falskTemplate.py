from flask import Flask                     
app = Flask(__name__)

@app.route()
def function():
    print("*"*100)
    return function

if __name__ == "__main__":
    app.run(debug=True)