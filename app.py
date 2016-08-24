from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
account_config = {
    'OPEN_REGISTRATION': False,
}
app.config.update({
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_ECHO': True,
})

app.config.update(account_config)

db = SQLAlchemy()
db.init_app(app)


@app.route('/')
def hello_world():
    # user_login("hello@email.com", '123456')
    # mvcode_service.generate_mvcode('13000010002')

    # mvcode_service.verify_mvcode('13000010002', '3214', 'message')
    # before_user_login.send(app, email="hello@email.com")
    #
    # print(request.remote_addr)
    # print(request.access_route)
    #
    # # print(request.remote_addr)
    # print(request.remote_user)
    # for h in request.headers:
    #     print(h)

    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
