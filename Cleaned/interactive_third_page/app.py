# import necessary libraries
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///babies.sqlite"

db = SQLAlchemy(app)


class Baby (db.Model):
    __tablename__ = 'babies'

    id = db.Column(db.Integer, primary_key=True)
    Decade = db.Column(db.Integer)
    Males = db.Column(db.Text)
    num_boys=db.Column(db.Integer)
    Females = db.Column(db.Text)
    num_girls=db.Column(db.Integer)

    def __repr__(self):
        return f"id={self.id}, name={self.name}"


#@app.before_first_request
#def setup():
    # Recreate database each time for demo
    #db.drop_all()
    #db.create_all()


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")




# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["findName"]
        #lower_name=name.lower()
        #pet = Pet(name=name, type=pet_type, age=age)
        #db.session.add(pet)
        #db.session.commit()
        years={"girls":[],"boys":[]}
        years["boys"] = db.session.query(Baby.Decade).filter(Baby.Males==name).all()
        years["girls"] = db.session.query(Baby.Decade).filter(Baby.Females==name).all()
        #if years["boys"]
        responses=[]
        responses.append("Never. Now is the time to start advocating for this name!")
        responses.append("Never. Are you sure this is a good name for a baby?")
        responses.append("Never. If this is your name, then you truly are a unique fish in a sea of commonality.")
        responses.append("Never. 130 years of people avoiding this name.")
        responses.append("Never. A rose by any other name would smell as sweet, but this name kind of stinks.")
        responses.append("Never. Wear your individuality as a badge of honor.")
        responses.append("Never. I can't believe it. It is such a good name. No, I'm not being sarcastic at all.")
        responses.append("Never. I had a cousin with this name, so there's that.")
        responses.append("Never. Just . . . never.")

        gender = ""
        answer = []
        if (len(years["boys"])==0 and len(years["girls"])==0):
            which_resp = np.random.randint(len(responses))
            answer=responses[which_resp]
            gender="boy or girl"
        else:
            if len(years["boys"])==0:
                which_resp = np.random.randint(len(responses))
                for i in years["girls"]:
                    answer.append(i[0])
                gender = "girl"
            if len(years["girls"])==0:
                which_resp = np.random.randint(len(responses))
                for i in years["boys"]:
                    answer.append(i[0])
                #answer=years["boys"]
                gender = "boy"
        
        
        #return render_template('index.html', {'boys': years["boys"],'girls': years["girls"]})
        #return render_template("http://localhost:5000/", {'boys': years["boys"],'girls': years["girls"]})
        #return redirect("http://localhost:5000/", code=302)
        #return redirect("index.html", code=302)
        #return redirect("http://localhost:5000/", {'boys': years["boys"],'girls': years["girls"]})
        
        #return render_template('index.html', name=name, boys=years["boys"], girls=years["girls"])
        return render_template('index.html', name=name, answer=answer, gender = gender)

#This part said render form.html in the pet pals thing
    return render_template("index.html")
    #return render_template('index.html', {'boys': years["boys"],'girls': years["girls"]})


# @app.route("/api/pals")
# def pals():
#     results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()

#     pet_type = [result[0] for result in results]
#     age = [result[1] for result in results]

#     pet_data = {
#         "x": pet_type,
#         "y": age,
#         "type": "bar"
#     }

#     return jsonify(pet_data)


# @app.route("/api/names")
# def pets():
#     results = db.session.query(Pet.name).all()
#     print(results)
#     all_pets = list(np.ravel(results))
#     return jsonify(all_pets)

if __name__ == "__main__":
    app.run()