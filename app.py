from flask import Flask, request, render_template, redirect, url_for, session
from func  import ck_idpw
import db
app = Flask(__name__)
app.secret_key = b'aaa!111/'



@app.route('/') 
def index():
    return render_template('main.html')   

@app.route('/coin') 
def coin():
    if 'user' in session:
        return '코인 거래소'
    else:
        return redirect('login')  

@app.route('/join') 
def join():
    return render_template('join.html')   

@app.route('/join_action', methods=['GET','POST']) 
def join_action():
    if request.method == 'GET':
        return "액션페이지"  
    else:
        id = request.form["id"]
        pw = request.form["pw"]
        name = request.form["name"]
        phone = request.form["phone"]
        print(id, pw, name, phone)
        db.insert_user(id, pw, name, phone) #데이터넣기
        return ck_idpw(id, pw)


@app.route('/login', methods=['GET','POST']) 
def login():
    if request.method == 'GET':
        return render_template('login.html')   
    else:
        userid = request.form["userid"]
        pwd = request.form["pwd"]
        print(userid, pwd)
        ret = db.get_idpw(userid, pwd)
        if ret !=None:
            session['user'] = ret[3] #로그인처리
        return ck_idpw(ret)



@app.route('/action_page', methods=['GET','POST']) 
def action_page():
    if request.method == 'GET':
        return '나는 액션페이지야'
    else:
        search = request.form["search"]
        return "당신은 '{}'로 검색을 했습니다".format(search)


@app.route('/image') 
def image():
    return render_template('image.html')

@app.route('/logout') 
def logout(): 
    session.pop('user', None) 
    return redirect(url_for('form'))


@app.route('/urltest') 
def url_test():
    return redirect(url_for('naver'))

@app.route('/move/<site>')      
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else:
        return '없는 페이지 입니다'

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다 url를 확인하세요", 404

@app.route('/daum') 
def daum():
    return redirect("http://www.daum.net/")


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)
