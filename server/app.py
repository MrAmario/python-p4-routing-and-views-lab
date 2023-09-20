#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print("hello")
    return "hello"

@app.route('/count/<int:parameter>')
def count(parameter):
    x = range(parameter)
    no = f''
    for n in x:
        no += f'{n}\n'
        print(n)
    return no

@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1,operator,num2):
    # result = num1 {operator} num2
    # return result
    result=0
    if operator == "+":
        result= num1 + num2
    elif operator == "-":
        result=num1 - num2
    elif operator == "*":
        result=num1 * num2
    elif operator == "%":
        result=num2 % num1
    elif operator == "div":
        result=num1/num2

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)