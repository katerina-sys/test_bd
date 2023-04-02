from app.dao.doc import DocDAO


class DocService:
    def __init__(self, dao: DocDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        doc = self.get_one(uid)

        doc.rubrics = data.get("rubrics")
        doc.text = data.get("text")

        self.dao.update(doc)

    def update_partial(self, data):
        uid = data.get("id")
        doc = self.get_one(uid)

        if "rubrics" in data:
            doc.rubrics = data.get("rubrics")
        if "text" in data:
            doc.text = data.get("text")

        self.dao.update(doc)

    def delete(self, uid):
        self.dao.delete(uid)
