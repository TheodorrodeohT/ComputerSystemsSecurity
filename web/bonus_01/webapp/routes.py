import sqlite3
from webapp import app
from webapp.forms import SearchForm
from flask import g, render_template, url_for, redirect, request, flash

# to initialize database:
# $ sqlite3 accounts.db < init-db.sql
DATABASE = './accounts.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resourse('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def form_handler(form):
    choice = form.choice.data
    if choice == '1':
        login_to_search = form.field.data
        url_redirect = f'/by-login?login={login_to_search}'
        return redirect(url_redirect)
    elif choice == '2':
        id_to_search = form.field.data
        url_redirect = f'/by-id?id={id_to_search}'
        return redirect(url_redirect)


@app.route('/', methods=['GET', 'POST'])
@app.route('/users', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return form_handler(form)

    query = 'select * from Users filter where status="active"'
    users = query_db(query)
    return render_template('home.html', users=users, form=form)


# обработать нулевые случаи
@app.route('/by-login', methods=['GET', 'POST'])
def by_login():
    form = SearchForm()
    if form.validate_on_submit():
        return form_handler(form)

    login = request.args.get('login')
    if login:
        query = f'select * from Users where login = "{login}"'
        users = query_db(query)
        if users:
            return render_template('home.html', users=users, form=form)
        else:
            return redirect(url_for('home'))


@app.route('/by-id', methods=['GET', 'POST'])
def by_id():
    form = SearchForm()
    if form.validate_on_submit():
        return form_handler(form)

    id = request.args.get('id')
    if id:
        query = f'select * from Users where id = {id}'
        users = query_db(query)
        if users:
            return render_template('home.html', users=users, form=form)
        else:
            return redirect(url_for('home'))


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
