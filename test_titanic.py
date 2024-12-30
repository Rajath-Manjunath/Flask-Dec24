import pytest
from titanic import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp=client.get("/")
    assert resp.status_code==200
    assert resp.text=="<h1>Hello there !!</h1>"
    
def test_predict_get(client):
    resp=client.get("/predict")
    assert resp.status_code==200
    assert resp.text=="<h1>I will predict</h1>"
    
def test_predict_post1(client):
    test_data={ 
    "Pclass":"3rd",
    "Sex":"male",
    "Age":22,
    "SibSp":1,
    "Parch":0,
    "Fare":10,
    "Embarked":"S"}
    resp=client.post("/predict",json=test_data)
    assert resp.status_code==200
    assert resp.text=="Oh no You did not survive"

def test_predict_post2(client):
    test_data={ 
    "Pclass":"3rd",
    "Sex":"female",
    "Age":22,
    "SibSp":1,
    "Parch":0,
    "Fare":10,
    "Embarked":"S"}
    resp=client.post("/predict",json=test_data)
    assert resp.status_code==200
    assert resp.text=="Yeaaaaa You survived"