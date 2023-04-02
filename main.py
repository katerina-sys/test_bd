from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.model.doc import Document
from app.database import db
from app.views.docs import doc_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(doc_ns)  # docs


def load_data():
    d1 = Document(id=1, rubrics="test1", text="test1.5", created_date="date")
    d2 = Document(id=2, rubrics="test2", text="test2.5", created_date="date")

    db.create_all()

    with db.session.begin():
        db.session.add_all([d1, d2])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)

    app.run()
