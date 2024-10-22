from flask import Blueprint, request, render_template
from .models import db, Usuarios, Post, Coment
from app.utils import get_coments, get_posts

rota = Blueprint('rota', __name__)


@rota.route('/')
def index():
    postagem = get_posts()
    coments = get_coments()
    return render_template('index.html', postagem = postagem, coments = coments)



    
