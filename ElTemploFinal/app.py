from flask import Flask, render_template, redirect, url_for, request
from wtforms.fields.simple import StringField, SubmitField, EmailField, TextAreaField
from wtforms.form import Form
from wtforms.validators import DataRequired

app = Flask(__name__)


class LoginForm(Form):
    name = StringField('Nombre', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.route('/',  methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")


@app.route('/precios')
def precios():
    return render_template("precios.html")


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = LoginForm()
    if request.method == 'POST':
        return 'Okay'
    return render_template("contacto.html", form=form)


@app.route('/novedades')
def novedades():
    return render_template("novedades.html")


if __name__ == '__main__':
    app.run()
