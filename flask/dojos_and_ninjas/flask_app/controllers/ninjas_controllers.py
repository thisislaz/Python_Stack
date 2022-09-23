from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninja/new')
def new_ninjas():
    dojos=Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect('/')

