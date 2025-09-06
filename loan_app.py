from flask import Flask, request
import pickle
app = Flask(__name__)

with open('classifier.pkl','rb') as f:
    model = pickle.load(f)

#Api endpoints
@app.route('/')
def home():
    return "<h1>Welcome to Loan Approval Application</h1>"
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return "I will make the prediction"
    else:
        loan_request = request.get_json()
        #print(loan_request)
        if loan_request['Gender'] == 'Male':
            Gender = 0
        else:
            Gender = 1

        if loan_request['Married'] == 'No':
            Married = 0
        else:
            Married = 1
        ApplicantIncome = loan_request['ApplicantIncome']
        LoanAmount = loan_request['LoanAmount']
        Credit_History = loan_request['Credit_History']

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        pred = model.predict([input_data])

        if pred == 1:
            return "<h1>Your loan application is approved</h1>"
        else:
            return "<h1>Your loan application is not approved</h1>"


        #return "you have sent a post request"
