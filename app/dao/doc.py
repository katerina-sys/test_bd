
# CRUD
from app.dao.model.doc import Document


class DocDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Document).get(uid)

    def get_all(self):
        return self.session.query(Document).all()

    def create(self, data):
        doc = Document(**data)

        self.session.add(doc)
        self.session.commit()

        return doc

    def update(self, doc):
        self.session.add(doc)
        self.session.commit()

        return doc

    def delete(self, uid):
        doc = self.get_one(uid)

        self.session.delete(doc)
        self.session.commit()
