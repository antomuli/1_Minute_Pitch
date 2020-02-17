from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())


    # pitches = db.relationship('Pitch', backref='user', lazy=True)
    # comments = db.relationship('Comment', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    # def __repr__(self):
    #     return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String(500))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches
    
    @classmethod
    def get_all_pitches():
        pitches = Pitch.query.all()

        return pitches

    @classmethod
    def get_pitch(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch
    
    @classmethod
    def get_pitches_by_user_id(cls, user_id):
        pitches = Pitch.query.filter_by(user_id=user_id).first()
        user = User.query.filter_by(user_id = user_id)

        return pitches

    @classmethod
    def count_pitches(cls, uname):
        user = User.query.filter_by(username=uname).first()
        pitches = Pitch.query.filter_by(user_id=user.id).all()

        pitches_count = 0
        for pitch in pitches:
            pitches_count += 1

        return pitches_count


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1000))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch):
        comments = Comment.query.filter_by(pitch_id=pitch).all()
        return comments

# class Upvote(db.Model):

#     __tablename__ = 'upvotes'
#     id = db.Column(db.Integer, primary_key = True)
#     upvote = db.Column(db.Integer, default = 1)
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     def save_upvotes(self):
#         db.session.add(self)
#         db.session.commit()

#     def add_upvotes(cls,id):
#         upvote_pitch = Upvote(user = current_user, pitch_id=id)
#         upvote_pitch.save_upvotes()

#     @classmethod
#     def get_upvotes(cls, id):
#         upvote = Upvote.query.filter_by(pitch_id=id).all()
#         return upvote

#     @classmethod
#     def get_all_upvotes(cls, pitch_id):
#         upvotes = Upvote.query.order_by('id').all()
#         return upvotes

#     def __repr__(self):
#         return f'{self.user_id}: {self.pitch_id}'


# class Downvote(db.Model):
#     __tablename__ = 'downvotes'
#     id = db.Column(db.Integer, primary_key = True)
#     downvote = db.Column(db.Integer, default=1)
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     def save_downvotes(self):
#         db.session.add(self)
#         db.session.commit()

#     def add_downvotes(cls, id):
#         downvote_pitch = Downvote(user = current_user, pitch_id = id)
#         downvote_pitch.save_downvotes()

#     @classmethod
#     def get_downvotes(cls, id):
#         downvote = Downvote.query.filter_by(pitch_id = id).all()
#         return downvote

#     @classmethod
#     def get_all_downvotes(cls, pitch_id):
#         downvote = Downvote.query.order_by('id').all()
#         return downvote

#     def __repr__(self):
#         return f'{self.user_id}: {self.pitch_id}'
