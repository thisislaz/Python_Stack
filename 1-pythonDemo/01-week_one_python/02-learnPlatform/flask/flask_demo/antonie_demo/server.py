from flask import Flask, render_template,request, redirect, session

app = Flask(__name__)
app.secrey_key = "THIS DEMO IS GOING GREAT"

@app.route('/index')
def index():
    print('i am printing something into the terminal, this might be useful.')
    return render_template('index.html')

@app.route('/fill_out_form')
def fill_out_form():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process_form():
    print('name: ',request.form['name'])
    print('fav pokemon',request.form['fav_pokemon'])
    session['name']=request.form['name']
    session['fav_pokemon']=request.form['fav_pokemon']
    return redirect('/')

@app.route('/variables/<word>/<int:number>')
def var_word_num(word,number):
    print("our word and number is...", word,number)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)