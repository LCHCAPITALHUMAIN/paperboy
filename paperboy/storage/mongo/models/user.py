from mongoengine import ListField, IntField, StringField, ReferenceField
from .base import Base


class UserMongo(Base):
    __tablename__ = 'users'
    id = IntField(required=True)
    name = StringField()
    password = StringField()

    notebooks = ListField(ReferenceField('NotebookMongo'))
    jobs = ListField(ReferenceField('JobMongo'))
    reports = ListField(ReferenceField('ReportMongo'))

    def __repr__(self):
        return "<User(name='%s')>" % self.name