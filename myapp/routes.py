from flask import Blueprint, redirect, url_for, request, jsonify
from .extensions import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    users_list_html = [f"<li>{user.username} [<form method='POST' action='/delete/{user.id}'><input type='hidden' name='_method' value='DELETE'><button type='submit'>Delete</button></form>]</li>" for user in users]
    
    return f"<ul>{''.join(users_list_html)}</ul>"

@main.route('/add/<username>', methods=['POST'])
def add_user(username):
    db.session.add(User(username=username))
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route('/delete/<int:user_id>', methods=['POST', 'DELETE'])
def delete_user(user_id):
    if request.method == 'DELETE' or (request.method == 'POST' and request.form.get('_method') == 'DELETE'):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for("main.index"))

@main.route('/update/<int:user_id>', methods=['POST', 'PUT'])
def update_user(user_id):
    if request.method == 'PUT' or (request.method == 'POST' and request.form.get('_method') == 'PUT'):
        user = User.query.get_or_404(user_id)
        new_username = request.form.get('new_username')
        user.username = new_username
        db.session.commit()
    return redirect(url_for("main.index"))
