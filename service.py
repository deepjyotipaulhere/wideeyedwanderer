from flask import Flask,request,jsonify, make_response
from flask_cors import CORS
from connection import connect, image_fetch_path, image_save_path

app=Flask(__name__)
CORS(app)



@app.route("/videos", methods=['GET'])
def videos():
    con=connect()
    video=con.wew.videos
    x=video.find({},{"_id":0})
    k=[]
    for i in x:
        k.append(i)
    con.close()
    return jsonify(k)

@app.route("/insertcomment", methods=['POST'])
def insertcomment():
    con=connect()
    try:
        x=request.get_json()
        blog=con.wew.blog
        from bson.objectid import ObjectId
        blog.update({'_id': ObjectId(x['id'])}, {'$push': {'comments': {
            "name": x['name'],
            "comment": x['comment']
        }}})
        con.close()
        return jsonify('ok')
    except Exception as ex:
        con.close()
        return make_response(str(ex),500)
    finally:
        con.close()


@app.route("/hit", methods=['GET'])
def hit():
    con=connect()
    hit=con.wew.hit
    import datetime
    j=hit.insert_one({'date':datetime.datetime.now()}).inserted_id
    con.close()
    return jsonify({'hit':str(j)})

@app.route("/registernewsletter",methods=['POST'])
def registernewsletter():
    con=connect()
    try:
        
        news=con.wew.newsletter_user
        x=request.get_json()
        assert (x['regemail']!=''), 'blank'
        news.insert_one({'email':x['regemail']}).inserted_id
        con.close()
        return jsonify('ok')
    except Exception as ex:
        con.close()
        return make_response(str(ex),500)
    finally:
        con.close()
    
@app.route("/getblog/<bid>", methods=['GET'])
def getblog(bid):
    con=connect()
    try:
        
        blog=con.wew.blog
        from bson.objectid import ObjectId
        x=blog.find_one({"_id":ObjectId(bid)})
        x["_id"]=str(x["_id"])
        con.close()
        return jsonify(x)
    except Exception as ex:
        con.close()
        return make_response(str(ex),500)
    finally:
        con.close()

@app.route("/updateblog", methods=['POST'])
def updateblog():
    con=connect()
    try:
        
        blog=con.wew.blog
        p=request.get_json()
        from bson.objectid import ObjectId
        x=blog.update_one({ "_id": ObjectId(p["_id"]) }, { "$set": { "text": str(p['text']), "title": str(p['title']),"coverphoto": str(p['coverphoto']),"visibility": p['visibility'] } })
        con.close()
        return "ok"
    except Exception as ex:
        con.close()
        return make_response(str(ex),500)
    finally:
        con.close()

@app.route("/createblog", methods=['POST'])
def createblog():
    con=connect()
    try:
        
        blog=con.wew.blog
        user=con.wew.user
        p=request.get_json()
        from bson import ObjectId
        username=user.find({"_id":ObjectId(p["by"])})
        from datetime import datetime
        p["date"]=datetime.now()
        p["name"]=username[0]["name"]
        x=blog.insert_one(p).inserted_id
        con.close()
        return str(x)
    except Exception as ex:
        con.close()
        return make_response(str(ex),500)
    finally:
        con.close()


@app.route("/login", methods=['POST'])
def login():
    con=connect()
    try:
        
        user=con.wew.user
        x=request.get_json()
        assert (x['username']!='' and x['password']!=''), 'blank'
        userid=user.find_one({'username':x['username'],'password':x['password']})
        assert (userid!=None), 'nf'                                                             # user not found
        con.close()
        return str(userid['_id'])+","+str(userid['name'])
    except Exception as ex:
        con.close()
        return make_response(str(ex), 500)
    finally:
        con.close()


@app.route("/register", methods=['POST'])
def register():
    con=connect()
    try:
        
        user=con.wew.user
        x=request.get_json()
        assert (x['username']!='' and x['password']!=''), 'blank'
        userid=user.insert_one(x).inserted_id
        assert (userid!=None), 'error'                                                             # user not found
        con.close()
        return str(userid)
    except Exception as ex:
        con.close()
        return make_response(str(ex), 500)
    finally:
        con.close()


@app.route("/getuserposts/<uid>", methods=['GET'])
def getuserposts(uid):
    con=connect()
    try:
        
        blog=con.wew.blog
        posts=blog.find({"by": uid}).sort("date",-1) if uid!="0" else blog.find({"visibility": True}).sort("date",-1)
        k=[]
        for x in posts:
            x["_id"]=str(x["_id"])
            x["text"]=" ".join(x["text"].split())[:150]+"..."
            k.append(x)
        con.close()
        return jsonify(k)
    except Exception as ex:
        con.close()
        return make_response(str(ex))
    finally:
        con.close()

@app.route("/uploadimage", methods=['POST'])
def uploadimage():
    from werkzeug.utils import secure_filename
    con=connect()
    try:
        import random
        import os
        x=request.files['test']
        filename = secure_filename(str(random.randint(1,10000))+str(hash(x.filename))+x.filename)
        x.save(os.path.join(image_save_path, filename))
        from PIL import Image
        image=Image.open(os.path.join(image_save_path, filename))
        image.save(os.path.join(image_save_path, filename),quality=20,optimize=True)
        photo=con.wew.photos
        photoid=photo.insert_one({'path':filename})
        con.close()
        return getimage(str(photoid.inserted_id))
    except Exception as ex:
        print(ex)
        con.close()
        return make_response(str(ex),500)
    finally:
        con.close()

@app.route("/getimage/<id>")
def getimage(id):
    con=connect()
    try:
        photo=con.wew.photos
        from bson.objectid import ObjectId
        x=photo.find_one({"_id":ObjectId(id)})
        return image_fetch_path+x["path"]
    except Exception as ex:
        con.close()
        print(ex)
    finally:
        con.close()


@app.route("/view/<id>", methods=['GET'])
def view(id):
    con=connect()
    blog=con.wew.blog
    from bson.objectid import ObjectId
    blog.update_one({ "_id": ObjectId(str(id)) }, { "$inc": { "view": 1 } })
    con.close()
    return jsonify("ok")

if __name__=='__main__':
    app.run(debug=True)