import json
import datetime
import pymysql

db = pymysql.connect(host='9.9.9.9', port=3306, db='db', user='sa', passwd='pass', charset='utf8')

def json_default(value):
  if isinstance(value, datetime.date):
    return value.strftime('%Y-%m-%d')
  raise TypeError('not JSON serializable')

def lambda_handler(event, context):
  global db
  with db.cursor(pymysql.cursors.DictCursor) as cursor:        
    curdic = db.cursor(pymysql.cursors.DictCursor)
    curdic.execute('SELECT seq, sort, title, thumbnail, photo, content, isstatus, viewcnt FROM benner')
    store_lists = curdic.fetchall()
    return store_lists
  db.close()