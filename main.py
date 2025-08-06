from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)


# Configura tu correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cashamaquinola@gmail.com'  # Reemplaza con tu correo
app.config['MAIL_PASSWORD'] = 'frxz bkrb dfws oaix'  # Reemplaza con tu contraseña de aplicación

mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/productos')
def productos():
    return render_template("productos.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    mensaje = request.form.get('mensaje')

    if not (nombre and email and mensaje):
        flash("Por favor, completa todos los campos.", "danger")
        return redirect(request.referrer or '/')

    # Aquí se intentaría enviar el correo
    try:
        msg = Message("Nueva solicitud de cotización",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['cashamaquinola@gmail.com'])
        msg.body = f"Nombre: {nombre}\nCorreo: {email}\nMensaje: {mensaje}"
        mail.send(msg)
        flash("Tu mensaje fue enviado correctamente.", "success")
    except Exception as e:
        print("Error al enviar correo:", e)
        flash("Hubo un problema al enviar el mensaje. Inténtalo más tarde.", "danger")

    return redirect(request.referrer or '/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
