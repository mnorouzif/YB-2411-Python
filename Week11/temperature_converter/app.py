from flask import Flask, render_template, request

app = Flask(__name__)

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
        else:
            return value
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            temperature = float(request.form['temperature'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_temperature(temperature, from_unit, to_unit)
            result = f"{temperature:.2f}°{from_unit} = {converted:.2f}°{to_unit}"
        except ValueError:
            result = "Please enter a valid number."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
