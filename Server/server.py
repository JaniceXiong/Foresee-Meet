import bottle
import json,os

os.chdir('../FrontEnd')
user_info={}
music_list = ['like','Jessica\'song','soft music']
user_info['name'] = 'xjw'
user_info['music_list'] = music_list
app = bottle.Bottle()

#返回静态页面
@app.route('/')
def hello():
    return bottle.static_file('hello.html','./')


#返回template
@app.route('/index')
def indexpage():
    return bottle.template('indexpage.html',**user_info)

music_info = {'music_name':'ticket to the moon','music_url':'www.baidu.com'}
@app.route('/vuetest')
def vuetest():
    return bottle.static_file('vuetest.html','./')

@app.route('/vuetestdata')
def vuetestdata():
    return json.dumps(music_info) #python字典转字符串

@app.route('/ref/<filename>')
def ref(filename):
    return bottle.static_file(filename, './ref/')

bottle.run(app,host='localhost',port=8080)

