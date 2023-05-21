from flask import Flask, render_template,request
import sqlite3 
app =Flask(__name__)
#con=sqlite3.connect("submit.db")
#con.execute("create table event(firstname TEXT, lastname TEXT, email TEXT, ph INTEGER)")
#print("table create successfully")
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/', methods=["POST","GET"])
def submit():
    if request.method == "POST":
        try:
            firstname=request.form['firstname']
            lastname=request.form['lastname']
            email=request.form['email']
            ph=request.form['ph']
            with sqlite3.connect("submit.db") as con:
                cur= con.cursor()
                cur.execute("INSERT into event (firstname, lastname, email, ph) values(?,?,?,?)",(firstname, lastname, email, ph))
        except:
            print("we cant find")
    return render_template("form.html")
@app.route('/page')
def page():
    con=sqlite3.connect("submit.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select*from event")
    rows=cur.fetchall()
    return render_template("page.html",rows=rows)
if __name__ =="__main__":
    app.run(debug=True)