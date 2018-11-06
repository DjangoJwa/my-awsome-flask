from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# 현재 모듈에 대해 Flask 객체 생성

CORS(app)

@app.route('/')
# 데코레이터를 통해서 '/'에 라우팅
def index():
    return 'Index'

@app.route('/get')
def get():
    return 'It\'s get'

# 위처럼 한 URL Rule에 대해 할당되어 로직을 처리하는 함수를 view function이라고 부른다
# URL rule - Endpoint에서 HTTP 메소드를 제외한 부분('GET /'에서 'GET'을 뺀 '/')
# 별도의 HTTP 메소드 명시가 없으면 GET에 라우팅하며, 따라서 아래의 view function은 'GET /'의 요청 처리를 담당

@app.route('/path/<string:subpath>')
#path 파라미터 정의 - <type:name>, 타입은 생략할 수 있고, 생략하면 타입은 string으로 처리된다.
#아래 view function은 'GET /path/{subpath}'에 대한 요청 처리를 담당한다.
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath: %s' % subpath

@app.route('/post-text', methods=['POST'])
def index_post():
    #이 함수는 'POST' http 메서드에 대한 view function
    return 'POST /'

app.add_url_rule('/2', 'something', lambda: 'Hi!')
