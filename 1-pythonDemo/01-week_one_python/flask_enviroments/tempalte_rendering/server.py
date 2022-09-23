from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def nothing():
    
    return render_template("index.html")

@app.route('/lists')
def render_some_lists():
    #this is a list of dictionaries
    student_info = [
        #each row is a dictionary, this is  helpful to know for when are looping thru the list then the dictionary.
            #for the dictionaries, we have the use the:
                #student_info['name] to get the "value" of the "key"
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", students = student_info)





if __name__=="__main__":
    app.run(debug=True)