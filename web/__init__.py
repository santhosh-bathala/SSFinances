from flask import Flask, render_template, url_for, abort
# import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import app_config
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    # from web.models import db, login_manager
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10
    app.config['SQLALCHEMY_POOL_PRE_PING'] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # with app.app_context():
    #    db.init_app(app)
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    csrf.init_app(app)
    # print(db.engine.pool.status())
    Bootstrap(app)
    # app.app_context().push()
    # db.create_all()
    # db.session.close()
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)
    from web import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title="Forbidden"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title="Page Not Found"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    @app.route('/500')
    def error():
        abort(500)
    
    @app.errorhandler(OperationalError)
    def handle_operational_error(error):
        db.session.rollback()
        db.session.close_all()
    return app
