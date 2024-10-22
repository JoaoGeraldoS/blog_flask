from flask import Blueprint, redirect, url_for, render_template, request, session, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Usuarios, Coment, Post
from app.utils import get_coments, get_posts

rota_user = Blueprint('norm_user', __name__)



@rota_user.route('/pag_init', methods = ['GET', 'POST'])
@jwt_required()
def initial():
    current_user = get_jwt_identity()
    get_nome = session.get('nome')

    

    # if coment:
    #     if coment.user_id != current_user:
    #         print(current_user)

    if request.method == 'GET':
        result_posts = get_posts()
        result_coments = get_coments()
        
        return render_template('pages/user/pag_init.html', postagem = result_posts, coments = result_coments, nome = get_nome)
    
    return redirect(url_for('norm_user.initial'))


@rota_user.route('/delete_comentario', methods = ['POST'])
@jwt_required()
def delete_comentario():
    current_user = get_jwt_identity()

    coment_id = request.form.get('coment_id')
    coment = Coment.query.get(coment_id)


    if coment:
        if coment.user_id != current_user:
            flash('Voce nao tem permissão para apagar esste comentario')
            return redirect(url_for('norm_user.initial'))

        db.session.delete(coment)
        db.session.commit()

    return redirect(url_for('norm_user.initial'))


@rota_user.route('/add_comentario', methods = ['POST'])
@jwt_required()
def add_comentario():
    current_user = get_jwt_identity()
    print(current_user)

    post_id = request.form.get('post_id')
    comentario = request.form.get('coment_entrada')


    if comentario and post_id:
        coment = Coment(comentario = comentario, user_id = current_user, post_id = post_id)
        db.session.add(coment)
        db.session.commit()

    
    return redirect(url_for('norm_user.initial'))




    