from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=False)
    password = db.Column(db.String())
    proposals = db.relationship('Proposal', backref='user', lazy=True)


class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(32))
    issue = db.Column(db.String(32), unique=False)
    brief = db.Column(db.String(128))
    detail = db.Column(db.String(1000))
    writer = db.Column(db.String(), db.ForeignKey('user.email'), nullable=False)

    def __repr__(self):
        return '<Brief: {}>'.format(self.brief)
