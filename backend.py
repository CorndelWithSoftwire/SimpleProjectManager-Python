# Database Seed
import sqlite3
conn = sqlite3.connect('qq-test-altran-2.db')
conn.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
conn.commit()

# Backend
from bottle import get, route, run, debug, install, template
from bottle_sqlite import SQLitePlugin
install(SQLitePlugin(dbfile='qq-test-altran-2.db'))

@get('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get('/todo')
def seeProjects(db):
    projects = db.execute('select * from todo').fetchall()
    return template('index', projects=[p['task'] for p in projects])

@get('/todo/add/<something>')
def add(db, something):
    db.execute("insert into todo (task, status) values (?,?)", (something, False))
    return template('Added <b>{{thing}}</b>', thing=something)

debug(True)
run(host='localhost', port=8080, reloader=True)