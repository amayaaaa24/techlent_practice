from src.calculator import Calculator
from flask import Flask, render_template, request

cal = Calculator()
app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    result = ""
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operator = request.form["operator"]
        if operator == "+":
            result = cal.add(float(num1), float(num2))
        elif operator == "-":
            result = cal.subtract(float(num1), float(num2))
        elif operator == "*":
            result = cal.multiply(float(num1), float(num2))
        else:
            result = cal.divide(float(num1), float(num2))

    return render_template("index.html", result=result)

@app.route("/health")
def health():
    return "I am health"

if __name__ == "__main__":
    # 比較安全的預設, debug=True一邊調一邊運行(但會要比較多資源)
    #app.run(debug=True, host='127.0.0.1', port=5000)
    # 4個0外面用戶才能連線
    app.run(debug=True, host='0.0.0.0', port=5000)
