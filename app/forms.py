from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
cat_list = [('Immigration', 'Immigration'),
            ('Racism', 'Racism'), ('Poverty', 'Poverty'), ('College Tuition', 'College Tuition'), ('Prison Reform', 'Prison Reform')]


class PostForm(FlaskForm):
    category = SelectField('Category')
    issue = StringField('Issue', validators=[DataRequired()])
    brief = TextAreaField('Brief')
    detail = TextAreaField('Detail', validators=[DataRequired()])
    factcheck = BooleanField('I have fact-checked my proposal', validators=[DataRequired()])
    submit = SubmitField('Submit Proposal')
