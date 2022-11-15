from helpers.database import db
from sqlalchemy.types import String


class Pessoa(db.Model):

    __tablename__ = "tb_pessoa"

    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True, nullable=False)
    nascimento = db.Column(db.Date)
    email = db.Column(db.String, unique=True)
    telefone = db.Column(db.String(11))    

    # Relacionamento com Endereço
    endereco = db.relationship("Endereco", uselist=False)

    # Herança: Superclasse
    tipo_pessoa = db.Column('tipo_pessoa', String(50))
    __mapper_args__ = {'polymorphic_on': tipo_pessoa}

    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Nome: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
