from flask import Flask, render_template                     
app = Flask(__name__)

@app.route('/play')
def play():
    print("*"*100)
    return render_template('playground.html')

@app.route('/play/<number_of_boxes>')
def function(number_of_boxes):
    print("*"*100)
    print(number_of_boxes)
    return render_template('playground_i.html', number_of_boxes=number_of_boxes)

# @app.route('/play/(x)/(color)')
# def function():
#     print("*"*100)
#     return function

if __name__ == "__main__":
    app.run(debug=True)