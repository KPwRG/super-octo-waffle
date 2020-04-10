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
    num = int(num)
    print(num)
    print(word)
    return word*num

@app.route('/repeat2/<int:num>/<word>')
def repeat2(num, word):
    print("*"*100)
    print(num)
    print(word)
    return word*num

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)