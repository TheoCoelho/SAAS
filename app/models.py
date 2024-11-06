from app import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Service {self.name}>"


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    columns = db.relationship('Column', backref='board', lazy=True)

class Column(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.Integer)  # Para ordenar as colunas no front-end
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    tasks = db.relationship('Task', backref='column', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    position = db.Column(db.Integer)  # Para ordenar as tarefas na coluna
    column_id = db.Column(db.Integer, db.ForeignKey('column.id'), nullable=False)
