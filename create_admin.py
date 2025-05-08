import os
from app import app, db
from models import User
from werkzeug.security import generate_password_hash

def create_admin_user():
    """
    Cria um usuário administrador padrão se não existir nenhum.
    """
    with app.app_context():
        # Verifica se existe algum usuário com privilégios de admin
        admin = User.query.filter_by(is_admin=True).first()
        
        if admin:
            print(f"Usuário admin já existe: {admin.username} (ID: {admin.id})")
            return admin
        
        # Cria um novo usuário admin
        admin_data = {
            "username": "admin",
            "email": "admin@seucodigo.com.br",
            "name": "Administrador",
            "bio": "Administrador do sistema SeuCodigo",
            "is_admin": True
        }
        admin = User(**admin_data)
        admin.password_hash = generate_password_hash("admin123")
        
        db.session.add(admin)
        db.session.commit()
        
        print(f"Usuário admin criado com sucesso: {admin.username} (ID: {admin.id})")
        return admin

if __name__ == "__main__":
    create_admin_user()