from flask import Flask                     
app = Flask(__name__)

@app.route('/')                             
def hello_world():                          
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print("*"*100)
    print(name)
    return f"Hi {name.title()}!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    print("*"*100)
    print(num)
    print(word)
    num = int(num)
    return word*num


if __name__ == "__main__":
    app.run(debug=True)