from flask import Flask, render_template

app = Flask(__name__)


listado_nombres =['Miguel Ángel',
'Juan Carlos',
'Carlos Alberto',
'José Luis',
'Juan Manuel']


@app.route("/")
def index():
    return render_template("index.html", title="Listado de Nombres", nombres= listado_nombres)
