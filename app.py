from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/equipment')
def equipment():
    items = [
        {'name': 'Treadmill', 'img': 'assets/treadmill.jpg'},
        {'name': 'Weight Set', 'img': 'assets/weights.jpg'},
        {'name': 'Elliptical', 'img': 'assets/elliptical.jpg'},
        # Add more equipment...
    ]
    return render_template('equipment.html', items=items)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    sent = False
    name = ''
    if request.method == 'POST':
        name = request.form['name']
        sent = True
        # Add email or data saving logic here
    return render_template('contact.html', sent=sent, name=name)

# if __name__ == '__main__':
#     app.run(debug=True)

# ✅ THIS IS IMPORTANT FOR RENDER
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)