from sqlalchemy.sql import func

from infrastructure.database.database import db


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    french_label = db.Column(db.String, nullable=False)
    english_label = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer,  db.ForeignKey('categories.id'), nullable=False)
    revers = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict_for_front(self):
        return {
            "id": self.id,
            "frenchLabel": self.french_label,
            "englishLabel": self.english_label,
        }