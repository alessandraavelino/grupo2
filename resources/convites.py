
from flask_restful import (Resource, current_app, marshal, marshal_with,
                           reqparse)
from sqlalchemy import exc

from helpers.database import db
from model.convites import Convites
from model.error import Error, error_campos

from .serializer import response_serializer

parser = reqparse.RequestParser()
parser.add_argument('email', required=True)
parser.add_argument('mensagem', required=True)

class ConvitesResource(Resource):
    def get(self):
        current_app.logger.info("Get - Convites")
        convites = Convites.query.all()
        response = response_serializer(convites)
        return response, 200

    def post(self):
        current_app.logger.info("Post - Convites")
        try:
            # JSON
            args = parser.parse_args()
            email = args['email']
            mensagem = args['mensagem']
            # Endereco
            convite = Convites(email, mensagem)
            # Criação do Endereco.
            db.session.add(convite)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204

    def put(self, id):
        current_app.logger.info("Put - Convites")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Convites: %s:" % args)
            # Evento
            email = args['email']
            mensagem = args['mensagem']

            Convites.query \
                .filter_by(id=id) \
                .update(dict(email=email, mensagem=mensagem))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204

    def delete(self, id):
        current_app.logger.info("Delete - Convite: %s:" % id)
        try:
            Convites.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204
