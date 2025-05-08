from app import app, db
from models import User

def check_admin_status():
    with app.app_context():
        # Verificar se existe o usuário admin
        admin = User.query.filter_by(username="admin").first()
        
        if admin:
            print(f"Usuário admin encontrado:")
            print(f"  ID: {admin.id}")
            print(f"  Username: {admin.username}")
            print(f"  Email: {admin.email}")
            print(f"  Is Admin: {admin.is_admin}")
            print(f"  Password Hash: {admin.password_hash[:20]}...")
        else:
            print("Usuário admin não encontrado.")

if __name__ == "__main__":
    check_admin_status()