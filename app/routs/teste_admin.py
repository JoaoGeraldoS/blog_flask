from datetime import timezone, datetime
from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Post, Coment, Usuarios

rota_admin = Blueprint('admin', __name__)


@rota_admin.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():

    get_posts = Post.query

    if request.method == 'GET':
        posts = [item.retorno() for item in get_posts]

        return render_template('pages/admin/dashboard.html', postagem = posts)

rota_admin.route('/delete_post', methods = ['POST'])
def delete_post():
    ...