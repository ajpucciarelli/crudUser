from os.path import dirname, join
from flask import Flask,json, request, jsonify
#from dao.engine import engine
from dao.userDao import db_insert, db_select, db_update, db_delete, db_selectAll
from model.user import User
from model.encoder import AlchemyEncoder
from pprint import pprint

app = Flask(__name__)

#db_insert('Ricardo', '98989898', 'ricardo_@gmail.com')
#pprint(db_select('98989898', 'phone'))

@app.route('/')
def select_user():    
    #pprint(request.form['email'])
    #email = request.form.get('email',None)
    #if email is not None:
    #    return json_response(db_select(email, 'email'))    
    result = db_selectAll()
    return json_response(db_selectAll())   
    #return json_response(db_select('98989898', 'phone'))

#@app.route('/<name>')
#def hello_name(name):
#    return "Hello {}!".format(name)

@app.route('/select',methods = ['GET']) #this is when user submits an insert
def select_user_filter():
    #pprint("request =",json.dumps(request))
    email = request.args.get('email', default = None, type = str)
    if request.method == 'GET' and email!=None:
        results = db_select(email, 'email')
        #results = db_selectAll()
        return json_response(results)
    return json_response({}, status=204)

@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def new_user():
    #pprint("request =",json.dumps(request))
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        db_insert(name, phone, email)        
    results = db_select(phone, 'phone')
    #results = db_selectAll()
    return json_response(results)

@app.route('/update',methods = ['POST', 'GET']) #this is when user submits an update
def update_user():
    pprint('Entrou em update_user')
    #pprint("request =",json.dumps(request))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        db_update(name, email)
    results = db_select(email, 'email')
    return json_response(results)

@app.route('/delete',methods = ['POST', 'GET']) #this is when user submits an update
def remove_user():
    #pprint("request =",json.dumps(request))
    if request.method == 'POST':
        email = request.form['email']
        db_delete(email)
    #results = db_select(email, 'email')
    return json_response('Removido com sucesso')

def json_response(payload, status=200):
    if payload == None:
        return ('', 204, {'content-type': 'application/json'})       
    return (json.dumps(payload, cls=AlchemyEncoder), status, {'content-type': 'application/json'})

if __name__ == '__main__':
    app.run()

