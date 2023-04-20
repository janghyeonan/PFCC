import json
import logging
import pymysql

conn = pymysql.connect(host='9.9.9.9', port=3306, db='name', user='sa', passwd='pass', charset='utf8')

def get_all():
	global conn
	curdic = conn.cursor(pymysql.cursors.DictCursor)
	sql = "SELECT * FROM item where status = '1' order by seq desc"
	curdic.execute(sql)
	store_lists = curdic.fetchall()
	return store_lists

def benner_all():
	global conn	
	curdic = conn.cursor(pymysql.cursors.DictCursor)
	sql = "SELECT * FROM benner"
	curdic.execute(sql)
	store_lists = curdic.fetchall()
	return store_lists
    

def get_page(x):
	global conn	
	curdic = conn.cursor(pymysql.cursors.DictCursor)
	sql = "SELECT * FROM item where status = '1' order by seq desc limit {}, 5".format((int(x)-1)*5)
	curdic.execute(sql)
	store_lists = curdic.fetchall()
	return store_lists


def get_select(x):
	global conn	
	curdic = conn.cursor(pymysql.cursors.DictCursor)
	sql = "SELECT * FROM item where seq = {}".format(x)
	curdic.execute(sql)
	store_lists = curdic.fetchall()
	return store_lists

def insItem(sn, cate, name, content, photo, cnt, status):
	global conn 
	db = conn
	curs = db.cursor()	
	sql = '''insert into item (sn, cate, name, content, photo, cnt, status) values(%s,%s,%s,%s,%s,%s,%s)'''
	curs.execute(sql,(sn, cate, name, content, photo, cnt, status))
	db.commit()
	db.close()

def del_update(x):
	print(x)
	global conn 	
	curdic = conn.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE item set status='0' WHERE seq = {}".format(x)
	curdic.execute(sql)
	conn.commit()
	conn.close()


app = Flask(__name__)

@app.route('/')
def main():
	return '<b>error</b>'

@app.route('/benner', methods=['GET'])
def benner():
	data = benner_all()
	return jsonify(data)

@app.route('/info/get', methods=['GET'])
def getTest():
	data = get_all()
	return jsonify(data)

@app.route('/info/get_page/<page>', methods=['GET'])
def getPate(page):
	data = get_page(page)
	return jsonify(data)

@app.route('/info/get/<id>', methods=['GET'])
def target_user(id):
	data = get_select(id)
	return jsonify(data)

@app.route('/info/post', methods=['POST'])
def postTest():		
	print(request.json)
	sn = request.json['sn']
	cate = request.json['cate']
	name = request.json['name']
	content = request.json['content']
	photo = request.json['photo']
	cnt = request.json['cnt']
	status = request.json['status']
	# insItem(sn, cate, name, content, photo, cnt, status)
	return {'status':'success'}

@app.route('/request', methods=['POST'])
def requestPostTest():
	headers = {'Content-Type':'application/json'}
	datas = request.get_json()
	res = requests.post("http://localhost:5000/info/post", headers=headers, json=datas, verify=False)
	return res.json()

@app.route('/delete/', methods=['DELETE'])
def delete_emp(id):	
	try:
		print(id)
		del_update(id)
		respone = jsonify('item deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == '__main__':
	app.run('0.0.0.0', port=9)