from os.path import dirname, join
from flask import Flask,json, request, jsonify
from dao.userDao import db_insert, db_select, db_update, db_delete, db_selectAll
from model.user import User
from model.encoder import AlchemyEncoder
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def select_user():    
    result = db_selectAll()
    return json_response(db_selectAll())   

@app.route('/select',methods = ['GET']) #this is when user submits an insert
def select_user_filter():
    email = request.args.get('email', default = None, type = str)
    if request.method == 'GET' and email!=None:
        results = db_select(email, 'email')
        return json_response(results)
    return json_response({}, status=204)

@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        db_insert(name, phone, email)        
    results = db_select(phone, 'phone')
    return json_response(results)

@app.route('/update',methods = ['POST', 'GET']) #this is when user submits an update
def update_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        db_update(name, email)
    results = db_select(email, 'email')
    return json_response(results)

@app.route('/delete',methods = ['POST', 'GET']) #this is when user submits an update
def remove_user():
    if request.method == 'POST':
        email = request.form['email']
        db_delete(email)
    return json_response('Removido com sucesso')

def json_response(payload, status=200):
    if payload == None:
        return ('', 204, {'content-type': 'application/json'})       
    return (json.dumps(payload, cls=AlchemyEncoder), status, {'content-type': 'application/json'})

if __name__ == '__main__':
    app.run()

