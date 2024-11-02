from flask import Flask, render_template, request, jsonify
import csv
import json

app = Flask(__name__)

# Halaman utama
@app.route('/')
def home():
    return render_template('home.html')

# Halaman CV
@app.route('/cv')
def cv():
    return render_template('cv.html')

# Halaman Portofolio
@app.route('/portofolio')
def portfolio():
    return render_template('portofolio.html')

# Halaman Biodata
@app.route('/biodataabel')
def biodata():
    return render_template('biodataabel.html')
# Halaman my cat 
@app.route('/cat')
def cat_page():
    return render_template('cat.html')
#Halaman book
@app.route('/book')
def book():
    return render_template('book.html')
#Halaman fibonaci
# Route Fibonacci
@app.route('/fibonaci', methods=['GET', 'POST'])
def fibonacci():
    deret = []
    if request.method == 'POST':
        panjang = int(request.form['number'])
        pertama, kedua = 0, 1
        for _ in range(panjang):
            deret.append(kedua)
            pertama, kedua = kedua, pertama + kedua
    return render_template('fibonaci.html', result=deret)
#halaman convert csv to json
@app.route('/csv', methods=['GET', 'POST'])
def convert_csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "Tidak ada file yang diunggah"}), 400
        file = request.files['file']
        if file.filename == '' or not file.filename.endswith('.csv'):
            return jsonify({"error": "File tidak valid atau bukan file CSV"}), 400
        file_data = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(file_data)
        json_data = [row for row in reader]
        return jsonify(json_data)
    return render_template('csv.html')
#Halaman submit form
@app.route('/form', methods=['GET', 'POST'])
def post_form():
    if request.method == 'POST':
        name = request.form.get('name')
        nim = request.form.get('nim')
        email = request.form.get('email')
        prodi = request.form.get('prodi')
        return render_template('form.html', name=name, nim=nim, email=email, prodi=prodi)
    return render_template('form.html')

