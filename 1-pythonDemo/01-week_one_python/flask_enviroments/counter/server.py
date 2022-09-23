from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = "lazaro"

@app.route('/')
def homepage():
    if 'visit' not in session:
        session['visit']=0
    else:
        session['visit']+=1    
    return render_template("index.html")

@app.route('/destroy_session')
def destory_sess():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)