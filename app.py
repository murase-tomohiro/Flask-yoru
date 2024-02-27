from flask import Flask,render_template,request
import sqlite3
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

@app.route("/test")
def test():
    py_name="すなばこ太郎"
    return render_template("base.html",name=py_name)

@app.route("/add")
def add_get():
    return render_template("add.html")

@app.route("/add",methods=["POST"])
def add_post():
    # 1.入力フォームからデータを取得する
    task=request.form.get("task")
    print(task)
    # 2.データベースに接続する
    con=sqlite3.connect("myTask.db")
    # 3.データベースを操作するための準備
    c=con.cursor()
    # 4.SQLを実行してDBにデータを送る
    c.execute("INSERT INTO tasks (id,task) VALUES (null,'{}')".format(task))
    # 5.データベースを更新（保存）する
    con.commit()
    # 6.データベースの接続を終了する
    c.close()
    return render_template("add.html")

@app.route("/list")
def list_get():
    con=sqlite3.connect("myTask.db")
    # 3.データベースを操作するための準備
    c=con.cursor()
    # 4.SQLを実行してDBにデータを送る
    c.execute("SELECT id,task FROM tasks;")
    # データを格納する配列を準備
    task_list=[]
    for row in c.fetchall():
        task_list.append({"id":row[0],"task":row[1]})
    # 5.データベースを更新（保存）する
    con.commit()
    # 6.データベースの接続を終了する
    c.close()
    return render_template("list.html",task_list=task_list)

if __name__=="__main__":
    app.run(debug=True)