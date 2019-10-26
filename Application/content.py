import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def add_db():
    db = get_db()

    with current_app.open_resource('add.sql') as f:
        db.executescript(f.read().decode('utf8'))


#### Initializes the Database ##########
# Done manually

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(add_db_command)


@click.command('add-db')
@with_appcontext
def add_db_command():
    """Clear the existing data and create new tables."""
    add_db()
    click.echo('Content Added to the database.')

########################################


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()