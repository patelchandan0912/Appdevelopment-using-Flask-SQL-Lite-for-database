from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app= Flask(__name__) ## we telling that this is the app. That is global

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/enternewData")
def new_student():
    return render_template('form.html')

@app.route('/userdata', methods = ['POST','GET'])
def userdata():
    if request.method == 'POST':
        try: 
            nm= request.form['nm']
            add=request.form['add']
            city=request.form['city']
            zip=request.form['zip']
            
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, addr, city, zip)VALUES(?,?,?,?)",(nm, add,city,zip))  ## question marks are placeholders. So this is the insert statement
                
                con.commit()
                msg="Inserted data successfully"
        except:
            con.rollback()
            msg= "There was an INSERT errors!"
        finally:
            con.close()
            return render_template("results.html")
@app.route('/list')
def list():
    con= sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    cur.execute("SELECT * FROM students ")
    
    rows= cur.fetchall()
    return render_template("results.html", rows=rows)

            
