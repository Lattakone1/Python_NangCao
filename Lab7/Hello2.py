from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Role Model (bảng vai trò)
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f'<Role {self.name}>'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref='users')

    def __repr__(self):
        return f'<User {self.username}>'

with app.app_context():
    db.create_all()
    admin_role = Role(name='Admin')
    user_role = Role(name='User')
    db.session.add(admin_role)
    db.session.add(user_role)
    db.session.commit()

    user1 = User(username='root', password='1234', role=admin_role)
    user2 = User(username='jane_smith', password='password456', role=user_role)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    print("Roles:", Role.query.all())
    print("Users:", User.query.all())

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)

