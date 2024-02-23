from flask import Flask,render_template
app=Flask(__name__)

# @app.route("/")
# def hello():
#     return "FlaskでHellow World!"

# @app.route("/<name>")
# def name(name):
#     return name+"さんこんにちは"

@app.route("/template")
def template():
    py_name="むらせ　ともひろ"
    return render_template("index.html",name=py_name)

if __name__=="__main__":
    app.run(debug=True)
