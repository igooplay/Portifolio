from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, NumberRange, URL, Optional
from models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nome de usuário já está em uso. Por favor, escolha outro.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email já está registrado. Por favor, use outro.')

class ProfileForm(FlaskForm):
    name = StringField('Nome completo', validators=[Length(max=120)])
    bio = TextAreaField('Biografia', validators=[Length(max=1000)])
    submit = SubmitField('Atualizar perfil')

class ProjectForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Descrição', validators=[DataRequired()])
    image_url = StringField('URL da imagem', validators=[Optional(), URL()])
    link = StringField('Link do projeto', validators=[Optional(), URL()])
    submit = SubmitField('Salvar projeto')

class ServiceForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Descrição', validators=[DataRequired()])
    icon = StringField('Classe do ícone', validators=[Length(max=64)])
    price = FloatField('Preço', validators=[Optional(), NumberRange(min=0)])
    submit = SubmitField('Salvar serviço')

class TestimonialForm(FlaskForm):
    client_name = StringField('Nome do cliente', validators=[DataRequired(), Length(max=120)])
    content = TextAreaField('Depoimento', validators=[DataRequired()])
    company = StringField('Empresa', validators=[Length(max=120)])
    position = StringField('Cargo', validators=[Length(max=120)])
    rating = IntegerField('Avaliação (1-5)', validators=[NumberRange(min=1, max=5)])
    submit = SubmitField('Salvar depoimento')

class ChatMessageForm(FlaskForm):
    content = TextAreaField('Mensagem', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class SiteConfigForm(FlaskForm):
    company_name = StringField('Nome da Empresa', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Telefone', validators=[DataRequired(), Length(max=20)])
    country = SelectField('País', choices=[
        ('Brasil', 'Brasil'),
        ('Portugal', 'Portugal'),
        ('Estados Unidos', 'Estados Unidos'),
        ('Canadá', 'Canadá'),
        ('Espanha', 'Espanha'),
        ('França', 'França'),
        ('Reino Unido', 'Reino Unido'),
        ('Alemanha', 'Alemanha'),
        ('Itália', 'Itália'),
        ('Japão', 'Japão'),
        ('China', 'China'),
        ('Austrália', 'Austrália')
    ])
    address = TextAreaField('Endereço', validators=[DataRequired(), Length(max=255)])
    latitude = StringField('Latitude', validators=[Optional(), Length(max=20)])
    longitude = StringField('Longitude', validators=[Optional(), Length(max=20)])
    logo_url = StringField('URL do Logo', validators=[Optional(), Length(max=255)])
    favicon_url = StringField('URL do Favicon', validators=[Optional(), Length(max=255)])
    
    # Redes sociais
    whatsapp = StringField('WhatsApp', validators=[Optional(), Length(max=20)])
    instagram = StringField('Instagram', validators=[Optional(), Length(max=120)])
    facebook = StringField('Facebook', validators=[Optional(), Length(max=120)])
    linkedin = StringField('LinkedIn', validators=[Optional(), Length(max=120)])
    twitter = StringField('Twitter', validators=[Optional(), Length(max=120)])
    youtube = StringField('YouTube', validators=[Optional(), Length(max=120)])
    github = StringField('GitHub', validators=[Optional(), Length(max=120)])
    
    submit = SubmitField('Salvar Configurações')
