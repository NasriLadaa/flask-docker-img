from flask import Flask, render_template, request, redirect, session

#magic functions 

app = Flask(__name__)
app.secret_key = "Hello World!"


#http://localhost:5000/

#methods

#decoertor
#http://localhost:5000/
@app.route("/")
def landing_page():
    return render_template("index.html")

# http://localhost:8000/login
@app.route("/login")
def login():
    return render_template("login.html" , count = 10, name="Nasri" )

# http://localhost:8000/view
@app.route("/view/<int:mynumber>")
def view_users(mynumber):
    return render_template("login.html" , count = mynumber, name="Nasri" )

# http://localhost:8000/user
@app.route("/user" , methods = ['POST'])
def login_user():
    
    username = request.form['username']
    password = request.form['password']
    fomr_type = request.form['fomr_type']

    print(f"My username is {username} and my password is {password} , {fomr_type}")
    
    session['myname'] = username

    return redirect("/home")

@app.route("/home")
def home_page():
    return render_template("home.html")

#Stateless webpages


#Your Entry point for the framework 
if __name__ == "__main__":
    app.run(debug = True)