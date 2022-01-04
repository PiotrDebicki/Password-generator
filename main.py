from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField 
from wtforms.validators import DataRequired, NumberRange
import random
import os


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(24)


class FormOpen(FlaskForm):
    password_len = IntegerField(validators=[DataRequired(), NumberRange(min=0, max=100)])
    numbers = BooleanField()
    high_letters = BooleanField()
    special_signs = BooleanField()
    small_letters = BooleanField()
    submit = SubmitField('Generate')


@app.route('/', methods=['GET', 'POST'])
def index():
    small_letters_set = "abcdefghijklmnopqrstuvwxyz"
    high_letters_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_signs_set = "!@#$%^&*"
    numbers_set = "0123456789"

    form = FormOpen()
    answer = "------------"
    if form.validate_on_submit():
        all_signs = ""
        if (form.numbers.data):
            all_signs += numbers_set
        if (form.high_letters.data):
            all_signs += high_letters_set
        if (form.special_signs.data):
            all_signs += special_signs_set
        if (form.small_letters.data):
            all_signs += small_letters_set
        
        answer = ""

        for _ in range(form.password_len.data):
            answer += all_signs[random.randrange(0, len(all_signs)-1, 1)]
    return render_template('index.html', form=form, answer=answer)
