#importing the necessary modules that you need 
from flask import Flask,render_template,redirect,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from database import adding_users_to_the_db,get_user_by_email
from flask_wtf.csrf import CSRFProtect

#creating a new flask application instance 
app = Flask(__name__)



app.config['SECRET_KEY'] = 'Gratia_Premium' # Set your secret key here
csrf = CSRFProtect(app)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    Form = form
    adding_users_to_the_db(Form)
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for("new"))
      
    return render_template('register.html', title='Register', form=form)
    

@app.route("/", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        entered_password = form.password.data

        # Retrieve the stored password from the database
        stored_password = get_user_by_email(email)

        if stored_password == entered_password:
            # Passwords match
            #session['user_id'] = user.id
            flash('You have been logged in!', 'success')
            return redirect(url_for('new'))
        else:
            # Passwords don't match
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title="Login", form=form)


@app.route('/')
def home():
  return render_template("login.html")

"""@app.route('/login')
def login():
  return render_template("login.html")"""

@app.route('/home')
def new():
  return render_template("home.html")

"""@app.route('/register')
def register():
  return render_template("register.html")"""

#this is just to run the program basically
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
  