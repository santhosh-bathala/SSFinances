# from web import app, db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,FloatField, SelectField
from wtforms.validators import Email, DataRequired, Length, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
# from wtforms.ext.sqlalchemy.fields import QuerySelectField

from web.models import Product, Customer


class AddCustomer(FlaskForm):
    username = StringField('name', validators=[DataRequired(), Length(min=2, max=50)])
    phone = StringField('phone', validators=[DataRequired(), Length(min=10, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    desc = StringField('desc', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField("Add Customer")


class AddProduct(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField("description", validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField("Add Product")


class AssignLoan(FlaskForm):
    # customers = QuerySelectField(query_factory=lambda: Customer.query.all(), get_label="name")
    # products = QuerySelectField(query_factory=lambda: Product.query.all(), get_label="name")
    loan_type = SelectField('loan_type', choices=[(product.name, product.name) for product in Product.query.all()])
    # loan_type = StringField('loan_type', validators=[DataRequired()])
    loan_amount = FloatField('loan_amount', validators=[DataRequired()])
    roi = FloatField('roi', validators=[DataRequired()])
    emi = FloatField('emi', validators=[DataRequired()])
    installments = IntegerField('installments', validators=[DataRequired()])
    total_payable_amount = FloatField('total_payable_amount', validators=[DataRequired()])
    total_interest_received = FloatField('total_interest_received', default=0)
    submit = SubmitField('Submit Loan')


class AddPayment(FlaskForm):
    # products = QuerySelectField(query_factory=lambda: Product.query.all(), get_label="name")
    # loan_type = db.Column(db.String(20), nullable=False)
    loan_type = StringField('loan_type', validators=[DataRequired()])
    loan_number = IntegerField('loan_number', validators=[DataRequired()])
    installment_number = IntegerField('installment_number', validators=[DataRequired()])
    installment_amount = FloatField('installment_amount', validators=[DataRequired()])
    installment_interest = IntegerField('installment_interest', validators=[DataRequired()])
    submit = SubmitField('Submit Payment')
