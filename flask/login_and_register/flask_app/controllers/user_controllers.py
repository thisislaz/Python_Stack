from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models import user_model


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('/dashboard.html')

@app.route('/logout')
def logout():
    del session['user_id']
    return redirect('/')    

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/user/new')
def user_new():
    return render_template('user_new.html')

@app.route('/user/process_login', methods=['POST'])
def user_process_login():
    #validate form
    if not user_model.User.validate_login(request.form):
        return redirect('/')

    return redirect('/dashboard')

@app.route('/user/create', methods=['POST'])
def user_create():
    if not user_model.User.validate_registration(request.form):
        return redirect('/')

    #hash the password
    hash_password = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hash_password
    } 
    id = user_model.User.create(data)
   
    session['user_id'] = id
    return redirect('/')

@app.route('/user/<int:id>')
def user_show(id):
    return redirect('/show_user.html')

@app.route('/user/<int:id>/edit')
def user_edit(id):
    return render_template('user_edit.html')

@app.route('/user/<int:id>/update', methods=['POST'])
def user_update(id):
    return redirect('/')

@app.route('/user/<int:id>/delete')
def user_delete(id):
    return redirect('/')