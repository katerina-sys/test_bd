from flask import request
from flask_restx import Resource, Namespace

from app.container import doc_service
from app.dao.model.doc import DocumentSchema

doc_ns = Namespace('docs')

doc_schema = DocumentSchema()
docs_schema = DocumentSchema(many=True)


@doc_ns.route('/docs')
class DocsView(Resource):
    def get(self):
        all_docs = doc_service.get_all()
        return docs_schema.dump(all_docs), 200

    def post(self):
        req_json = request.json
        doc_service.create(req_json)

        return "", 201


@doc_ns.route('/doc/<int:uid>')
class DocView(Resource):
    def get(self, uid: int):
        doc = doc_service.get_one(uid)
        return doc_schema.dump(doc), 200

    def put(self, uid):
        req_json = request.json
        req_json['id'] = uid

        doc_service.update(req_json)

        return "", 204

    def patch(self, uid):
        req_json = request.json
        req_json['id'] = uid

        doc_service.update_partial(req_json)

        return "", 204

    def delete(self, uid: int):
        doc_service.delete(uid)

        return "", 204



