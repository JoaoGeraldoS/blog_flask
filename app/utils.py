from .models import Post, Coment, Usuarios
from flask import session

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_posts():
    postes = Post.query

    result = []
    for post in postes:
        data_post = post.data_post.strftime('%Y-%m-%d %H:%M:%S') if post.data_post else 'Data indisponivel'
        
        result.append({
            'id': post.id,
            'titulo': post.titulo,
            'imagem_url': post.imagem_url,
            'conteudo': post.conteudo,
            'autor': post.autor,
            'data_postagem': data_post
        })

    return result


def get_coments():
    get_coments = Coment.query.all()

    result = []
    for coment in get_coments:
        usuario = Usuarios.query.filter_by(id = coment.user_id).first()

        if not usuario:
            continue

        data_comment = coment.data_comment.strftime('%Y-%m-%d %H:%M:%S') if coment.data_comment else 'Data indisponivel.'
       
        result.append({
            'id': coment.id,
            'comentario': coment.comentario,
            'data_comment': data_comment,
            'post_id': coment.post_id,
            'user_id': coment.user_id,
            'nome': usuario.nome,
        })

    return result
