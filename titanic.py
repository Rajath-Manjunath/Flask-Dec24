from flask import Flask,request
import pickle

app=Flask(__name__)

with open('classifier.pkl','rb') as f:
    model=pickle.load(f)

# API endpoints

@app.route('/')
def hello_world():
    return "<h1>Hello there !!</h1>"

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return "<h1>I will predict</h1>"
    else:
        inputs=request.get_json()
        print(inputs)
        Pclass=inputs['Pclass']
        if Pclass=="1st":
            Pclass=1
        if Pclass=="2nd":
            Pclass=2
        if Pclass=="3rd":
            Pclass=3
        Sex=inputs['Sex']
        if Sex=="male":
            gender=0
        if Sex=="female":
            gender=1
        Age=inputs['Age']
        SibSp=inputs['SibSp']
        Parch=inputs['Parch']
        Fare=inputs['Fare']
        Embarked=inputs['Embarked']
        if Embarked=="S":
            embarked=0
        if Embarked=="C":
            embarked=1
        if Embarked=="Q":
            embarked=2    
        print(Pclass,gender,Age,SibSp,Parch,Fare,embarked)
        input_data=[Pclass,gender,Age,SibSp,Parch,Fare,embarked]
        prediction=model.predict([input_data])
        print(prediction[0])
        if prediction[0]==0:
            outcome="Oh no You did not survive"
        else:
            outcome="Yeaaaaa You survived"
        return outcome

