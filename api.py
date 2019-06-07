import flask
from flask import request, jsonify
from flask_cors import CORS
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/',methods=['GET'])
def default():
	return ''' <h1> Hi.. 27-APR-19 Batch of Data Scientists
        </h1>'''

@app.route('/sunday',methods=['GET'])
def sunday():
	return ''' <h1> Hi.. IT is very Late
        </h1>'''        

@app.route('/predictIt',methods=['GET'])
def predictIt():
	from sklearn.externals import joblib
	model =joblib.load('hp-2jun.ml')
	return str(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]]))#str(model.predict([[1500,5,10,5,3]]))  

@app.route('/hello',methods=['GET'])
def hello():
    return ''' <h1> Helloo.. just checking..</h1>'''

@app.route('/predict',methods=['GET'])
def predict():
    from sklearn.externals import joblib
    model = joblib.load('hp-2jun.ml')
    return str(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]]))


@app.route('/mayhp',methods=['GET'])
def mayhp():
    from sklearn.externals import joblib
    model = joblib.load('../hp-3May.ml')
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))


@app.route('/testing',methods=['GET'])
def testing():
    return ''' <h1> Hi.. My testing successful.</h1>'''

@app.route('/predicthp',methods=['GET'])
def predicthp():
    from sklearn.externals import joblib
    model = joblib.load('hp-21apr.ml')
    
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))




@app.route('/test',methods=['GET'])
def test():
	return ''' <h1> Testing.. </h1>'''


@app.route('/hp-predict',methods=['GET'])
def hp():
    from sklearn.externals import joblib
    model = joblib.load('hp-18feb.ml')
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))




@app.route('/sales_returns', methods=['GET'])
def returns():
    from sklearn.externals import joblib
    model = joblib.load('sales_returns_trained_model.ml')
    return str(model.predict([[int(request.args['age']),int(request.args['gender']),int(request.args['city']),int(request.args['cat'])]]))

@app.route('/hp', methods=['GET'])
def home1():
    from sklearn.externals import joblib
    model = joblib.load('hp_team_train.ml')
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))


app.run()
