from datetime import timedelta
from flask import Blueprint, request, render_template, redirect, url_for, make_response, session
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity
from app.models import db, Usuarios

rota_user = Blueprint('users', __name__)


@rota_user.route('/users', methods = ['GET', 'POST'])
def users():

    if request.method == 'GET':
         return render_template('pages/users.html')

    checked = request.form['check']
    nome = request.form['name']
    username = request.form['username']
    senha = request.form['password']

    verify_admin = False
    
    try:
        admin = request.form['admin']

        if admin == 'admin' :
            verify_admin = True
                    
    except KeyError:
        print('Chave inexistente')    

    if checked == 'Cadastro':
        if verify_admin:
            user = Usuarios(nome = nome, username = username, senha = senha, admin = verify_admin)
        else:
            user = Usuarios(nome = nome, username = username, senha = senha)
            
        db.session.add(user)
        db.session.commit()
            
        return redirect(url_for('users.users'))
    
    if checked == 'Login':
        user = Usuarios.query.filter_by(username = username).first_or_404()


        if username == user.username and senha == user.senha:

            session['user_id'] = user.id
            session['nome'] = user.nome

            if user.admin == True:
                accsss_token_admin = create_access_token(identity= user.id, expires_delta=timedelta(days=2))

                response = make_response(redirect(url_for('admin.dashboard')))
                set_access_cookies(response, accsss_token_admin)

                return response

            else:
                accsss_token_user = create_access_token(identity=user.id, expires_delta=timedelta(days=2))

                response = make_response(redirect(url_for('norm_user.initial')))
                set_access_cookies(response, accsss_token_user)

                return response
        else:
            return 'Usuario ou senha invalidos'
            
@rota_user.route('/logout', methods = ['GET'])        
def logout():
    response = make_response(redirect(url_for('rota.index')))
    response.delete_cookie('access_token_cookie')
    return response
    


      

    

    

