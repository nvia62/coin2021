import pymysql
def insert_user(userid, pw, name, phone):
    try: 
        db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='maindb', charset='utf8')
        c = db.cursor() 
        setdata = (userid, pw, name, phone)
        c.execute("INSERT INTO user_tbl (id, pw, name, phone) VALUES (%s, %s, %s, %s)", setdata)
        db.commit() 
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def get_idpw(userid, pw):
    ret = ()
    try: 
        db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='maindb', charset='utf8')
        c = db.cursor() 
        setdata = (userid, pw)
        c.execute("SELECT * FROM user_tbl WHERE id = %s AND pw = %s", setdata)
        ret = c.fetchone
    except Exception as e: 
        print('db error:', e) 
    finally:
        db.close()
    return(ret)
