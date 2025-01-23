from flask import Blueprint, render_template, request, redirect
from app import db
from app.models import Todo

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

@main.route('/delete/<int:sno>')
def delete(sno):
    dtodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(dtodo)
    db.session.commit()
    return redirect("/")
