from flask import Flask,request,jsonify, make_response
from flask_cors import CORS
from connection import connect

app=Flask(__name__)
CORS(app)



@app.route("/hit", methods=['GET'])
def hit():
    con=connect()
    hit=con.hit
    import datetime
    j=hit.insert_one({'date':datetime.datetime.now()}).inserted_id
    return jsonify({'hit':str(j)})

@app.route("/registernewsletter",methods=['POST'])
def registernewsletter():
    try:
        con=connect()
        news=con.newsletter_user
        x=request.get_json()
        assert (x['regemail']!=''), 'blank'
        news.insert_one({'email':x['regemail']}).inserted_id
        return jsonify('ok')
    except Exception as ex:
        return make_response(str(ex),500)
    
@app.route("/chatakpur", methods=['GET'])
def chatakpur():
    try:
        con=connect()
        blog=con.blog
        x=blog.find_one()
        return jsonify({'text':x['text']})
    except Exception as ex:
        return make_response(str(ex),500)

@app.route("/updatechatakpur", methods=['POST'])
def updatechatakpur():
    try:
        con=connect()
        blog=con.blog
        p=request.get_json()
        from bson.objectid import ObjectId
        x=blog.update_one({ "_id": ObjectId("5ccdae4ff1726f2e00a3ca17") }, { "$set": { "text": str(p['text']) } })
        return "ok"
    except Exception as ex:
        return make_response(str(ex),500)

@app.route("/login", methods=['POST'])
def login():
    try:
        con=connect()
        user=con.user
        x=request.get_json()
        assert (x['username']!='' and x['password']!=''), 'blank'
        userid=user.find_one({'username':x['username'],'password':x['password']})
        assert (userid!=None), 'nf'                                                             # user not found
        return str(userid['_id'])
    except Exception as ex:
        return make_response(str(ex), 500)


@app.route("/register", methods=['POST'])
def register():
    try:
        con=connect()
        user=con.user
        x=request.get_json()
        assert (x['username']!='' and x['password']!=''), 'blank'
        userid=user.insert_one({'username':x['username'],'password':x['password']}).inserted_id
        assert (userid!=None), 'error'                                                             # user not found
        return str(str(userid))
    except Exception as ex:
        return make_response(str(ex), 500)

if __name__=='__main__':
    app.run(debug=True)