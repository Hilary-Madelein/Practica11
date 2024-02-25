from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        mensaje = request.form.get('mensaje')

        # Aquí puedes procesar los datos como desees, por ejemplo, imprimirlos
        print(f'Nombre: {nombre}, Email: {email}, Teléfono: {telefono}, Mensaje: {mensaje}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
