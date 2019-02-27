# Configuration #
database_file = 'python-sqlite-base-project.db'

# Database Seeding #
import sqlite3
conn = sqlite3.connect(database_file)
conn.execute("""CREATE TABLE IF NOT EXISTS project (
                    id INTEGER PRIMARY KEY, 
                    name char(100) NOT NULL, 
                    completed bool NOT NULL
                    );""")
conn.execute("""CREATE TABLE IF NOT EXISTS task (
                    id INTEGER PRIMARY KEY, 
                    name char(100) NOT NULL, 
                    project_id INTEGER NOT NULL,
                    FOREIGN KEY(project_id) REFERENCES project(id)
                    );""")
conn.commit()

# Backend #
## Setup
from bottle import get, post, run, debug, install, request, response, redirect, static_file, template
from bottle_utils.flash import message_plugin
from bottle_sqlite import SQLitePlugin
install(message_plugin)
install(SQLitePlugin(dbfile=database_file))

## Routes
@get('/project')
def project_index(db):
    project_result = db.execute('select * from project').fetchall()
    projects = [{'name': p['name'], 'link': f"/project/{p['id']}/tasks"} 
                for p in project_result]
    return template('project_index', projects=projects, message=request.message)

@get('/project/add')
def add_project():
    return template('project_add')

@post('/project/add')
def add_project_post(db):
    project_name = request.forms.get('project_name')
    db.execute("insert into project (name, completed) values (?,?)", (project_name, False))
    response.flash(f'Added project: <b>{project_name}</b>')
    redirect('/project')

@get('/project/<project_id>/tasks')
def task_index(db, project_id):
    task_result = db.execute("""
        select * from task 
        where project_id = ?
        """, project_id).fetchall()
    project_name = db.execute('select name from project where id = ?', project_id).fetchone()['name']
    tasks = [p['name'] for p in task_result]
    return template('task_index', project_id=project_id, project_name=project_name, tasks=tasks, message=request.message)

@get('/project/<project_id>/tasks/add')
def add_task(db, project_id):
    project_name = db.execute('select name from project where id = ?', project_id).fetchone()['name']
    return template('task_add', project_id=project_id, project_name=project_name)

@post('/project/<project_id>/tasks/add')
def add_task_post(db, project_id):
    task_name = request.forms.get('task_name')
    db.execute("insert into task (name, project_id) values (?,?)", (task_name, project_id))
    project_name = db.execute('select name from project where id = ?', project_id).fetchone()['name']
    response.flash(f'Added task: <b>{task_name}</b> for project: {project_name}')
    redirect(f'/project/{project_id}/tasks')

@get('/static/<file>')
def serve_static(file):
    return static_file(file, root='./static')

## Initialisation
debug(True)
run(host='localhost', port=8080, reloader=True)