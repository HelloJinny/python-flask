from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Fcuser(db.Model):
    __tablename__ = 'fcuser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

    # 실제로 함수로 만들지만 접근할 때 변수처럼 사용할 수 있다
    # 모델이 대해서 직렬화하는 변수나 함수를 만들고 api 결과로 전달
    @property
    def serialize(self):
        return {
            'id': self.id,
            'password': self.password,
            'userid': self.userid,
            'username': self.username
        }
