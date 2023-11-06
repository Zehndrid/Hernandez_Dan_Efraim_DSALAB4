from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/toUpperCase')
def to_uppercase():
    return render_template('toUpperCase.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle_area():
    area = None
    radius = None

    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius'))
            area = 3.14 * radius ** 2
        except ValueError:
            area = None

    return render_template('circle.html', area=area, radius=radius)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    base = None
    height = None

    if request.method == 'POST':
        try:
            base = float(request.form.get('base'))
            height = float(request.form.get('height'))
            area = 0.5 * base * height
        except ValueError:
            area = None

    return render_template('triangle.html', area=area, base=base, height=height)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
