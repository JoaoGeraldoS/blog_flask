import os
from datetime import timezone, datetime
from flask import Blueprint, request, render_template, redirect, url_for, session, flash, current_app
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Post, Coment, Usuarios
from app.utils import get_coments, get_posts,allowed_file


rota_admin = Blueprint('admin', __name__)


#Rota para mostrar, deletar posts e comentarios
@rota_admin.route('/dashboard', methods = ['GET', 'POST'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()

    get_nome = session.get('nome')

    if request.method == 'GET':

        result_posts = get_posts()
        result_coments = get_coments()
        
        return render_template('pages/admin/dashboard_admin.html', postagem = result_posts, coments = result_coments, nome = get_nome)
    
    atualizar = request.form['update'].lower()
    
    if atualizar == 'atualizar':        
        post_id = request.form.get('post_id')

        return redirect(url_for('admin.update', id= post_id))
    
    return redirect(url_for('admin.dashboard'))


@rota_admin.route('/delete_post', methods = ['POST'])
@jwt_required()
def delete_post():
    current_user = get_jwt_identity()

    post_id = request.form.get('post_id')
    post = Post.query.get(post_id)

    if post:
        db.session.delete(post)
        db.session.commit()
        flash('Post apagado com sucesso') 
    return redirect(url_for('admin.dashboard'))


#Rota para criar posts
@rota_admin.route('/admin', methods = ['GET', 'POST'])
@jwt_required()
def create():
    current_user = get_jwt_identity()

    if request.method == 'POST':

        title = request.form['title']
        conteudo = request.form['conteudo']
        auth = request.form['auth']
        file = request.files['file']


        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            post = Post(titulo = title, conteudo = conteudo, autor = auth)
            post.imagem_url = os.path.join('static', 'uploads', filename)
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('admin.dashboard'))
    
    return render_template('pages/admin/add.html')



#Rota para editar posts
@rota_admin.route('/update/<int:id>', methods = ['GET', 'POST'])
@jwt_required()
def update(id):
    current_user = get_jwt_identity()

    if request.method == 'GET':
        return render_template('pages/admin/update.html')
    
    file = request.files['file']
    post = Post.query.filter_by(id = id).first()

    if file and allowed_file(file.filename):      
        if post.imagem_url:
            filename = os.path.basename(post.imagem_url)
            old_image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

            if os.path.exists(old_image_path):
                os.remove(old_image_path)
        
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
    
        post.imagem_url = os.path.join('static', 'uploads', filename)
    

    post.titulo = request.form['title']
    post.conteudo = request.form['conteudo']
    post.auth = request.form['auth']
    post.data_post = datetime.now(timezone.utc)

    db.session.commit()

    flash('Post atualizado com sucesso')

    
    return redirect(url_for('admin.dashboard'))


@rota_admin.route('/delete_coment', methods = ['POST'])
@jwt_required()
def delete_coment():
    current_user = get_jwt_identity()
    coment_id = request.form.get('coment_id')
    coment = Coment.query.get(coment_id)

    if coment:
        db.session.delete(coment)
        db.session.commit()

        flash('Comentario apagado com sucesso!')
    return redirect(url_for('admin.dashboard'))


@rota_admin.route('/add_coment', methods = ['POST'])
@jwt_required()
def add_coment():
    current_user = get_jwt_identity()

    post_id = request.form.get('post_id')
    comentario = request.form.get('coment_entrada')
    user_id = session.get('user_id')

    if comentario and post_id:
        coment = Coment(comentario = comentario, user_id = user_id, post_id = post_id)
        db.session.add(coment)
        db.session.commit()
        flash('Comentario adicionado com sucesso')
    else:
        flash('Erro: O comentario não pode esta vazio')
    
    return redirect(url_for('admin.dashboard'))

