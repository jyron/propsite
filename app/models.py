from app import db


class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(32))
    issue = db.Column(db.String(32), unique=False)
    brief = db.Column(db.String(128))
    solution = db.Column(db.String(1000))

    def __repr__(self):
        return '<Brief: {}>'.format(self.brief)
