from sqlalchemy.sql import func

from database.database import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    french_label = db.Column(db.String, nullable=False)
    english_label = db.Column(db.String, nullable=False)
    competition = db.Column(db.Boolean, nullable=False, default=False)

