#importing the necessary modules that you need 
from flask import Flask,render_template 


#connection = mysql.connector.connect(host=)


#creating a new flask application instance 
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("login.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/home')
def new():
  return render_template("home.html")

@app.route('/register')
def register():
  return render_template("register.html")

#this is just to run the program basically
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
  