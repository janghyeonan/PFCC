#Created by An Janghyun

from flask import Flask, request, jsonify
import json
import pymysql
import datetime

#flask api server

app = Flask(__name__)

#json file read
def talk_book():
    with open('more.json', 'r', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
    return json_data


def db_select(x):
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    with db.cursor(pymysql.cursors.DictCursor) as cursor:        
        curdic = db.cursor(pymysql.cursors.DictCursor)
        curdic.execute(x)
        store_lists = curdic.fetchall()    
    db.close()
    return jsonify(store_lists)

def long_view():
    return db_select('SELECT seq, title, thumbnail, photo, content, isstatus, viewcnt FROM benner where sort = 1 and isstatus = 1 order by seq desc')

def short_view():
    return db_select('SELECT seq, title, thumbnail, photo, content, isstatus, viewcnt FROM benner where sort = 2 and isstatus = 1 order by seq desc')

def review_view():
    return db_select("SELECT seq, name, content, photo, DATE_FORMAT(wdate, '%Y-%m-%d %T') AS wdate, isatatus  from review order by seq DESC")

def rshop_view():
    return db_select('SELECT seq, code, name, content, thumbnail, price, photo, install_photo, mov, ddate, isatatus from shop')

def rshop_search(x):
    return db_select('SELECT seq, code, name, content, thumbnail, price, photo, install_photo, mov, ddate, isatatus from shop where seq = {}'.format(str(x)))    

def review_search(x):
    return db_select('SELECT seq, name, content, photo, wdate, isatatus  from review where seq = {}'.format(str(x)))

def search(x):
    return db_select('SELECT seq, title, thumbnail, photo, content, isstatus, viewcnt FROM benner where seq = {}'.format(str(x)))
  
def get_install():
    return db_select("SELECT o.seq, o.ordernum, o.sort, o.req_cate, o.req_content, date_format(o.ordr_date, '%y-%m-%d %T') as ordr_date, o.work_id, o.item_code, o.work_step, o.isstatus, o.userid, o.res_content, u.addr, u.name, o.memo from order as o inner join user as u on o.userid  = u.seq  where o.sort = 'install'")
    
def get_detail_install(x):
    return db_select("SELECT * from order where sort = 'install' and seq = {}".format(str(x)))

def get_delivery():
    return db_select("SELECT * from order where sort = 'delivery';")

def get_detail_delivery(x):
    return db_select("SELECT * from order where sort = 'delivery' and  seq = {}".format(str(x)))

def get_feed():
    return db_select("SELECT seq, cate, title, oneline, DATE_FORMAT(ddate, '%Y-%m-%d %T') AS ddate, img, source, writer, tag, isatatus, content From feed where isatatus = 1 order by seq desc;")

@app.route('/osear', methods = ['POST'])
def osear():
  if request.method == 'POST':
    data = request.get_json()    
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("SELECT work_step, ordernum, sort, req_cate, req_content, ordr_date, work_id, item_code, isstatus, userid from order where seq = {0}".format(data["seq"]))
    store_lists = curs.fetchall()    
    db.close()
    return jsonify(store_lists)

@app.route('/updatestatus', methods = ['POST'])
def updatestatus():
  if request.method == 'POST':
    data = request.get_json()    
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("UPDATE rorder SET work_step = '{0}' where seq = '{1}'".format(data["work_step"], data["seq"]))
    db.commit()        
    db.close()
    return jsonify(data) # 받아온 데이터를 다시 전송


@app.route('/sorder', methods = ['POST'])
def sorder():
  if request.method == 'POST':
    data = request.get_json()#json 데이터를 받아옴    
    print(data["username"], data["post"], data["addr"], data["hp"], data["email"], data["itemname"],  data["request"])
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("INSERT into sorder (username, post, addr, hp, email, itemname,  request) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(data["username"], data["post"], data["addr"], data["hp"], data["email"], data["itemname"],  data["request"]))
    db.commit()        
    db.close()
    return jsonify(data)# 받아온 데이터를 다시 전송

@app.route('/rjoin', methods = ['POST'])
def rjoin():
  if request.method == 'POST':
    data = request.get_json()#json 데이터를 받아옴    
    print(data["id"], data["pw"], data["name"])
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("INSERT into ruser(userid, pw, name) values('{0}','{1}','{2}')".format(data["id"], data["pw"], data["name"]))
    db.commit()
    curs.execute("select * from ruser where userid = '{0}'".format(data["id"]))    
    store_lists = curs.fetchall()    
    db.close()
    return jsonify(store_lists)

@app.route('/echeck', methods = ['POST'])
def echeck():
  if request.method == 'POST':
    data = request.get_json()#json 데이터를 받아옴    
    print(data["email"])
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("select count(userid) as 'return' from ruser where userid = '{0}'".format(data["email"]))    
    store_lists = curs.fetchall()    
    db.close()
    return jsonify(store_lists)

@app.route('/rlogin', methods = ['POST'])
def rlogin():
  if request.method == 'POST':
    data = request.get_json()#json 데이터를 받아옴    
    print(data["id"], data["pw"])
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("SELECT (HEX(AES_ENCRYPT('pass', now()))) as token from ruser WHERE userid  = '{0}' and pw = '{1}' union all select 'fail' as token from ruser limit 1".format(data["id"],data["pw"]))    
    store_lists = curs.fetchall()    
    db.close()
    return jsonify(store_lists)

@app.route('/responcon', methods = ['POST'])
def responcon():
  if request.method == 'POST':
    data = request.get_json() #json 데이터를 받아옴    
    print(data["res_content"], data["seq"])
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("UPDATE rorder SET res_content = '{0}' where seq = '{1}'".format(data["res_content"], data["seq"]))
    db.commit()        
    db.close()
    return jsonify(data) # 받아온 데이터를 다시 전송

@app.route('/resmemo', methods = ['POST'])
def resmemo():
  if request.method == 'POST':
    data = request.get_json() #json 데이터를 받아옴    
    print(data["memo"], data["seq"])
    db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
    curs = db.cursor()
    curs.execute("UPDATE rorder SET memo = '{0}' where seq = '{1}'".format(data["memo"], data["seq"]))
    db.commit()        
    db.close()
    return jsonify(data) # 받아온 데이터를 다시 전송

@app.route('/infeed', methods = ['POST'])
def infeed():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        try:
            db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
            curs = db.cursor()
            query = "INSERT into feed (cate, title, oneline, ddate, img, source, writer, tag, isatatus, content) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            curs.execute(query, (data["cate"], data["title"], data["oneline"], data["ddate"], data["img"], data["source"], data["writer"], data["tag"], data["isatatus"], data["content"]))
            db.commit()
            return jsonify(data)
        except Exception as e:
            print(e)
            return jsonify({'error': 'An error occurred while inserting data into the database'})
        finally:
            db.close()

@app.route('/upfeed', methods = ['POST'])
def upfeed():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        try:
            db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')
            curs = db.cursor()
            query = '''UPDATE feed  SET cate = %s, title = %s, oneline = %s, ddate = %s, 
            img = %s, source = %s, writer = %s, tag = %s, isatatus = %s, 
            content = %s where seq = %s;'''
            curs.execute(query, (data["cate"], data["title"], data["oneline"], data["ddate"], data["img"], data["source"], data["writer"], data["tag"], data["isatatus"], data["content"], data["seq"]))
            db.commit()
            return jsonify(data)
        except Exception as e:
            print(e)
            return jsonify({'error': 'An error occurred while inserting data into the database'})
        finally:
            db.close()


@app.route("/sb", methods=['GET'])
def sb():
  return short_view()

@app.route("/lb", methods=['GET'])
def lb():
  return long_view()

@app.route("/rshop", methods=['GET'])
def rshop():
  return rshop_view()

@app.route("/rinstall", methods=['GET'])
def rinstall():
  return get_install()

@app.route("/rdelivery", methods=['GET'])
def rdelivery():
  return get_delivery()

@app.route("/rdinstall/<int:id>")
def rdinstall(id):    
  return get_detail_install(id)

@app.route("/rddelivery/<int:id>")
def rddelivery(id):
  return get_detail_delivery(id)

@app.route("/rshop/<int:id>")
def rshopv(id):    
  return rshop_search(id)

@app.route("/benner/<int:id>")
def benner(id):    
  return search(id)

@app.route("/review", methods=['GET'])
def review():
  return review_view()

@app.route("/research/<int:id>")
def research(id):    
  return review_search(id)

@app.route("/feed", methods=['GET'])
def feed():
  return get_feed()

@app.route("/talkbook", methods=['GET'])
def talkbook():
  return talk_book()

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 9999)
