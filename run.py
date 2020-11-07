import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

from app.main.model import balance
from app.main.model import branch, cancelled_invoice, cash, expense, payment


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
