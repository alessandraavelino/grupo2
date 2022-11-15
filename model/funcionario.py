from model.pessoa import Pessoa
from helpers.database import db


class Funcionario (Pessoa, db.Model):

    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario'}

    cargo = db.Column(db.String, nullable=False)

    def __init__(self, nome, nascimento, email, telefone, prefeitura, cargo):
        super().__init__(nome, nascimento, email, telefone)
        # TODO: É necessário adicionar o relacionamento com a entidade Prefeitura
        self.prefeitura = prefeitura
        self.cargo = cargo

    def __repr__(self):
        return ""
