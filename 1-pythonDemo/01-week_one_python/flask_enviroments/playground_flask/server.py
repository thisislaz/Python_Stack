from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def nothing_yet():
    return render_template("play.html")

# @app.route('/play/<int:num>')
# def multiply_box(num):
#     return render_template("play.html", num=num)

@app.route('/play/<int:num2>/<color>')
def box_color(num2,color):
    return render_template("play.html", num2=num2, color=color)
    


if __name__== "__main__":
    app.run(debug=True)