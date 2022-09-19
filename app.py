from flask import *
import mysql.connector
import re

app = Flask(__name__)
# Enter your database connection details below
def connection(a):
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '8881',
        database = 'user')
    mycursor = mydb.cursor()
    mycursor.execute(a)
    result = mycursor.fetchone()
    mydb.close()
    return result

@app.route("/")
@app.route("/first_page")
def first_page():
    return render_template("first_page.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login", methods= ['POST','GET'])
def login():
    session = []
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # getting input with name = username in HTML form
        username = request.form.get("username")
        # getting input with name = password in HTML form
        password = request.form.get("password")
        query = "select * from person where username = '{}' and pwd = '{}'".format(username,password)
        rus = connection(query)
        if rus:
            # Redirect to Home Page
            return 'Logged in successfully!'
        else:
            #Account doesn't Exist or uname / pass incorrect
            return 'Incorrect username / Password'
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)