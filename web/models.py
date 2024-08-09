from web import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# db = SQLAlchemy()
# login_manager = LoginManager()


class Customer(db.Model, UserMixin):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(128))
    desc = db.Column(db.String(200))
    create_timestamp = db.Column(db.DateTime, default=datetime.now)
    update_timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    # products = db.relationship('Product', backref='customer', lazy='dynamic')
    loans = db.relationship('Loan', backref='customer', lazy='dynamic')
    payments = db.relationship('Payment', backref='customer', lazy='dynamic')

    def __repr__(self):
        return "<Customer: {}>".format(self.name)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    desc = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    # customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Product: {}>'.format(self.name)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_type = db.Column(db.String(50), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    roi = db.Column(db.Float, nullable=False)
    emi = db.Column(db.Float, nullable=False)
    installments = db.Column(db.Integer, nullable=False)
    total_payable_amount = db.Column(db.Float, nullable=False)
    total_interest_received = db.Column(db.Float, default=0.0)
    total_amount_out_standing = db.Column(db.Float, default=0.0)
    create_timestamp = db.Column(db.DateTime, default=datetime.now)
    update_timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = db.Column(db.Boolean, default=True)

    # customer_id = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return '<Loan: {}>'.format(self.loan_type)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_type = db.Column(db.String(20), nullable=False)
    loan_number = db.Column(db.Integer, nullable=False)
    installment_number = db.Column(db.Integer)
    installment_amount = db.Column(db.Float)
    installment_interest = db.Column(db.Float)
    create_timestamp = db.Column(db.DateTime, default=datetime.now)
    update_timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Payment: {}>'.format(self.loan_type)
