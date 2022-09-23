from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo_model import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route('/dojos/new_dojo', methods=['POST'])
def new_dojo():
    # print(request.form)
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/show/<int:id>')
def show_dojo(id):
    data = {
        "id":id
    }
    return render_template('show_dojo.html', dojo=Dojo.view_one_with_ninjas(data))