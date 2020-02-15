# from flask_wtf import FlaskForm
# from wtforms import StringField,TextAreaField,SubmitField,SelectField
# from wtforms.validators import Required

# class PitchForm(FlaskForm):

#     title = StringField('Pitch title',validators=[Required()])
#     text = TextAreaField('Text',validators=[Required()])
#     category = SelectField('Type',choices=[('',''),('',''),('','')],validators=[Required()])
#     submit = SubmitField('Submit')

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Bio.',validators = [Required()])
#     submit = SubmitField('Submit')

# class CommentForm(FlaskForm):
#     text = TextAreaField('Leave a comment:',validators=[Required()])
#     submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
    pitch_title = StringField('Title', validators = [Required()])
    pitch_content = TextAreaField("What would you like to pitch?", validators = [Required()])
    category = RadioField('Label', choices = [('promotionpitch', 'Promotion Pitch'), ('interviewpitch', 'Interview Pitch'), ('pickuplines', 'Pick-Up Lines'), ('productpitch', 'Product Pitch')], validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comments', validators = [Required()])
    submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class Downvote(FlaskForm):
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators = [Required()])
    submit = SubmitField('Submit')