from flask import Flask, render_template
#import Flask to allow us to create our app
#must also add render_terplates for the html part
app = Flask(__name__)   #create a new instance of the Flask class called "app"


@app.route('/1')         #the "@" decorator associatres this route with the function immediately following
def hello_world():      #the '/' is the homepage really
    return "hello world!"   #return the string "hello world" as a response

@app.route('/<word>/<int:num>')
def index_page(word,num):
    return render_template('index.html', phrase="hello", times=5, word=word,num=num)

@app.route('/check_this_shit_out_bitch')
def fuck_python():
    return "i fucking hate coding in python bruh"

@app.route('/making_more_pages/<any_word>')
def more_pages(any_word):
    return f"This is {any_word}, but still not easy"

@app.route('/trying/<word><int:some_number>')
def trying_things(word,some_number):
    return f"Hello, I am {word} and im practicing the flask env in the program, this is my {some_number} time adding an @app.route method"

@app.route("/more_tries/<another_word><int:another_num>/<int:multipler>")
def keep_testing(another_word,another_num,multipler):
    return f"hi i am {another_word} and now i have created {multipler} of these flask env things and ive added a multipler, but i dont know what will happned. ive added it to the end {another_num * multipler}  "

@app.route('/trying/1/<word2>/<int:somenum>/<fucking>')
def fuck_python2(word2,somenum,fucking):
    return f"i {word2} { fucking  *  somenum } hate coding in python bruh"

@app.route('/check/hi/nope/yeah/<var><int:another_var>/<float:float_num>')
def more_prac(var,another_var,float_num):
    # print(var)
    # print(another_var)
    # print(float_num)
    return f"Just doing more testing by {var*another_var} the space between lazaro(var) was added in the webpage bar. Turning 9 into {float_num}. The space between the number 9 (which is a float requirement from the url bar) was in the code itself "

if __name__ == "__main__":   #ensure this file is being rundirectly and not from a adifferent module
    app.run(debug=True)     #run the app in debug mode