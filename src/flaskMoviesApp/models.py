from flaskMoviesApp import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from email.policy import default


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    profile_image = db.Column(db.String(30), nullable=False, default='default_profile_image.png')
    password = db.Column(db.String(15), nullable=False)
    movies = db.relationship('Movie', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.username}:{self.email}"



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    plot = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(30), nullable=False, default='default_movie_image.png')
    rating = db.Column(db.Integer, default=0, nullable=False)## Integer, δήλωση πεδίου βαθμολογίας ταινίας, με προεπιλεγμένη τιμή το μηδέν: default=1, υποχρεωτικό πεδίο
    release_year = db.Column(db.Integer, default=2000, nullable=False)## Integer, δήλωση πεδίου χρονιάς πρώτης προβολής της ταινίας με προεπιλεγμένη τιμή default=2000, υποχρεωτικό πεδίο
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.date_created}:{self.title}:{self.rating}"
