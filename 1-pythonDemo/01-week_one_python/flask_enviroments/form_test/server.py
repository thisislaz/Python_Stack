from flask import Flask, render_template, request, redirect, session #add request and redirect
app = Flask(__name__)
app.secret_key = "keep it serect, keep it safe" #set a secret key for security purposes


@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/users', methods=['POST'])  #this may handle more tahn one request
def create_user():                      #accessing the data follwos this format:
                                            #request.form['name_of_input']
    print("Got Post Info bruh")         #the type of for anything that comes in through request.form will be a "string" no matter what
    #here we add teo properties to session tos tore the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # print(request.form)
    # name = request.form['name']
    # email = request.form['email']                                     #you must type cast if you want a number
    #never redner a template on a POST request.
    #instead we will redirect to our index route
    return redirect('/show')

@app.route('/show')
def show_user():
    print('Showing the User Info From the Form')
    print(request.form)
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])



if __name__ == "__main__":
    app.run(debug=True)