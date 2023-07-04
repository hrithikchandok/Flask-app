from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import smtplib

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///User.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///st.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)

class st(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(200),nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    college = db.Column(db.String(200), nullable=False)
    # date_created=db.Column(db.DateTime,default=datetime.utcnow)

def __repr__(self):
    return f'<User {self.name}'

with app.app_context():
    db.create_all()
subs=[]

@app.route("/")
def hello_world():
    title="HRX Blog"
    return render_template("index.html",titlep=title)

@app.route("/home")
def home():
    name="rishabh"
    return render_template("about.html", name2=name)

@app.route('/about')
def about():
    title='About us'
    names=['kiran','hrithik','rishabh','saly']
    return render_template('about.html',names=names,title=title)

@app.route('/subsribe')
def contact():
    title="Subscribe to my Email News"
    return render_template("subsribe.html",title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    email=request.form.get("Email")
    college=request.form.get("college")

    user=st(first_name=first_name,last_name=last_name,email=email,college=college)
    db.session.add(user)
    try:
        db.session.commit()
        # return "Thanks for Subs"
    except Exception as e:
        db.session.rollback()
        return f"Commit failed,Error:{e}"

    # message="you Have been subsribed to HRX Blogs"
    # server=smtplib.SMTP("smtp.gmail.com",587)
    # server.starttls()
    # server.login("hrithikzubair@gmail.com","hrithikchandok")
    # server.sendmail("hrithikzubair@gmail.com",email,message)

    subs.append(f"{first_name}{last_name} | {email}| {college}")
    title="Subsribed"
    all_users = st.query.all()
    return render_template("users.html",title=title,first_name=first_name,last_name=last_name,email=email,college=college,subs=subs,users=all_users)

@app.route('/users')
def users():
    all_users=st.query.all()
    return render_template('users.html',users=all_users)

app.run(debug=True)
app.debug=True