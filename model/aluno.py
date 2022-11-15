from model.pessoa import Pessoa
from helpers.database import db


class Aluno(Pessoa, db.Model):

    __tablename__ = "tb_aluno"
    __mapper_args__ = {'polymorphic_identity': 'aluno', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    instituicaoDeEnsino = db.Column(db.String, nullable=False)
    curso = db.Column(db.String, nullable=False)
    matricula = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula, endereco):
        super().__init__(nome, nascimento, email, telefone)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula

    def __repr__(self):
        return '<Nome: {}\n Nascimento: {}\n Email: {}\n Telefone: {}\n Instituição de ensino: {}\n Curso: {}\n Matrícula: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula)
