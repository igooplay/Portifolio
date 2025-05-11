import datetime
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# User loader function for flask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(120))
    bio = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    # Relationships
    messages_sent = db.relationship('ChatMessage', foreign_keys='ChatMessage.sender_id', backref='sender', lazy='dynamic')
    messages_received = db.relationship('ChatMessage', foreign_keys='ChatMessage.recipient_id', backref='recipient', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    link = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(64))  # For storing icon class names
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(120))
    position = db.Column(db.String(120))
    rating = db.Column(db.Integer, default=5)  # Out of 5
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    read = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'recipient_id': self.recipient_id,
            'content': self.content,
            'timestamp': self.timestamp.isoformat(),
            'read': self.read,
            'sender_name': self.sender.username
        }

class SiteConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False, default="SeuCodigo")
    email = db.Column(db.String(120), nullable=False, default="contato@seucodigo.com.br")
    phone = db.Column(db.String(20), default="+55 11 99999-9999")
    country = db.Column(db.String(50), default="Brasil")
    address = db.Column(db.Text, default="Av. Paulista, 1000 - São Paulo, SP")
    latitude = db.Column(db.String(20), default="-23.5505")
    longitude = db.Column(db.String(20), default="-46.6333")
    logo_url = db.Column(db.String(255), default="/static/img/logo.png")
    favicon_url = db.Column(db.String(255), default="/static/img/favicon.ico")
    whatsapp = db.Column(db.String(20))
    instagram = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    linkedin = db.Column(db.String(120))
    twitter = db.Column(db.String(120))
    youtube = db.Column(db.String(120))
    github = db.Column(db.String(120))
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    @classmethod
    def get_settings(cls):
        # Retorna as configurações existentes ou cria uma nova com valores padrão
        config = cls.query.first()
        if not config:
            config = cls()
            db.session.add(config)
            db.session.commit()
        return config
