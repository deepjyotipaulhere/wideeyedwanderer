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
    
@app.route("/getblog/<bid>", methods=['GET'])
def getblog(bid):
    try:
        con=connect()
        blog=con.blog
        from bson.objectid import ObjectId
        x=blog.find_one({"_id":ObjectId(bid)})
        x["_id"]=str(x["_id"])
        return jsonify(x)
    except Exception as ex:
        return make_response(str(ex),500)

@app.route("/updateblog", methods=['POST'])
def updateblog():
    try:
        con=connect()
        blog=con.blog
        p=request.get_json()
        from bson.objectid import ObjectId
        x=blog.update_one({ "_id": ObjectId(p["_id"]) }, { "$set": { "text": str(p['text']), "title": str(p['title']),"coverphoto": str(p['coverphoto']) } })
        return "ok"
    except Exception as ex:
        return make_response(str(ex),500)

@app.route("/createblog", methods=['POST'])
def createblog():
    try:
        con=connect()
        blog=con.blog
        user=con.user
        p=request.get_json()
        from bson import ObjectId
        username=user.find({"_id":ObjectId(p["by"])})
        from datetime import datetime
        p["date"]=datetime.now()
        p["name"]=username[0]["name"]
        x=blog.insert_one(p).inserted_id
        return str(x)
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


@app.route("/getuserposts/<uid>", methods=['GET'])
def getuserposts(uid):
    try:
        con=connect()
        blog=con.blog
        posts=blog.find({"by": uid}).sort("date",-1) if uid!="0" else blog.find().sort("date",-1)
        k=[]
        for x in posts:
            x["_id"]=str(x["_id"])
            x["text"]=" ".join(x["text"].split())[:150]+"..."
            k.append(x)
        return jsonify(k)
    except Exception as ex:
        return make_response(str(ex))

@app.route("/uploadimage", methods=['POST'])
def uploadimage():
    try:
        x=request.files['test']
        fname=str(x.filename)
        ftype=str(x.content_type)
        from gridfs import GridFS
        
        con=connect()
        fs=GridFS(con,"images")
        # with open(x,"r") as f:
        image=fs.put(x.stream, content_type=ftype, filename=fname)
        return str(image)
    except Exception as ex:
        print(ex)
        return make_response(str(ex),500)

@app.route("/getimage/<id>")
def getimage(id):
    from gridfs import GridFS
    con=connect()
    fs=GridFS(con,"images")
    from bson import objectid
    gridout = fs.get(objectid.ObjectId(id)).read()
    import flask
    return flask.Response(gridout, mimetype='image/*')

if __name__=='__main__':
    app.run(debug=True)