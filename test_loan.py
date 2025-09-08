import pytest
from loan_app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.text == "<h1>Welcome to Loan Approval Application</h1>"

def test_predict(client):
    test_input = {
    "ApplicantIncome" : 100,
    "Credit_History" : 1.0,
    "Gender" : "Male",
    "LoanAmount" : 12000,
    "Married" : "No"
    }
    resp = client.post('/predict',json=test_input)
    assert resp.status_code == 200
    assert resp.text == "<h1>Your loan application is not approved</h1>"
