from flask import render_template, request, redirect, url_for, Blueprint
from app import db
from app.models import Service

# Criação do Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    services = Service.query.all()
    return render_template('index.html', services=services)

@main.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

@main.route('/customize')
def customize():
    return render_template('customize.html')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html')

@main.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@main.route('/gerenciamentodeprojetos')
def  gerenciamentodeprojetos():
    return render_template('gerenciamentodeprojetos.html')



@main.route('/boards/<int:board_id>/columns', methods=['POST'])
def add_column(board_id):
    column_name = request.form['name']
    new_column = Column(name=column_name, board_id=board_id, position=0)  # Defina a posição corretamente
    db.session.add(new_column)
    db.session.commit()
    return redirect(url_for('main.board', board_id=board_id))

@main.route('/tasks/move', methods=['POST'])
def move_task():
    task_id = request.form['task_id']
    new_column_id = request.form['column_id']
    new_position = request.form['position']

    task = Task.query.get(task_id)
    task.column_id = new_column_id
    task.position = new_position
    db.session.commit()

    return {'status': 'success'}