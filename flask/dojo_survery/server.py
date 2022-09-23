from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "lazaro"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submitted_info():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def results():

    return render_template('results.html')




if __name__ == "__main__":
    app.run(debug=True)