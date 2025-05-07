import os
from app import app, db
from werkzeug.security import generate_password_hash
from models import User

# Executar dentro do contexto da aplicação
with app.app_context():
    # Verificar se existe o usuário admin
    admin = User.query.filter_by(username="admin").first()
    
    if not admin:
        # Criar usuário admin
        admin = User(
            username="admin",
            email="admin@seucodigo.com.br",
            password_hash=generate_password_hash("admin123"),
            name="Administrador",
            bio="Administrador do sistema SeuCodigo.",
            is_admin=True
        )
        
        db.session.add(admin)
        db.session.commit()
        print("Usuário admin criado com sucesso!")
    else:
        # Garantir que o usuário admin tenha is_admin=True
        if not admin.is_admin:
            admin.is_admin = True
            db.session.commit()
            print("Flag de admin atualizada para o usuário admin.")
        
        print("Usuário admin já existe.")
        print(f"Username: {admin.username}")
        print(f"Email: {admin.email}")
        print(f"Is Admin: {admin.is_admin}")