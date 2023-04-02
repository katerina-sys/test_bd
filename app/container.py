from app.dao.doc import DocDAO
from app.database import db
from app.services.doc import DocService

doc_dao = DocDAO(db.session)
doc_service = DocService(doc_dao)

