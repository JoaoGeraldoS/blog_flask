from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuarios(db.Model):

   


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, default = False)

    def retorno(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'username': self.username
        }

    coment_user = db.relationship('Coment', back_populates = 'user')

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    imagem_url = db.Column(db.String(255), nullable = False)
    autor = db.Column(db.String(100), nullable = False)
    data_post = db.Column(db.DateTime, default = datetime.now(timezone.utc))

    def retorno(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'imagem_url': self.imagem_url,
            'conteudo': self.conteudo,
            'autor': self.autor,
            'data_postagem': self.data_post
        }

    comentarios = db.relationship('Coment', back_populates = 'post', cascade='all, delete')

class Coment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comentario = db.Column(db.Text, nullable=False)
    data_comment = db.Column(db.DateTime, default = datetime.now(timezone.utc))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    

    def retorno(self):
        return {
            'id': self.id,
            'comentario': self.comentario,
            'data_comment': self.data_comment,
            'post_id': self.post_id,
            'user_id': self.user_id
        }

    post = db.relationship('Post', back_populates = 'comentarios')
    user = db.relationship('Usuarios', back_populates = 'coment_user')
    