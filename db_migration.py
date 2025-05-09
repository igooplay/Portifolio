import os
import json
import datetime
from app import app, db
from models import User, Project, Service, Testimonial, ChatMessage

def json_serial(obj):
    """Função para serializar objetos que não são naturalmente serializáveis por JSON."""
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError(f"Tipo não serializável: {type(obj)}")

def export_data():
    """Exporta todos os dados do banco de dados para arquivos JSON."""
    with app.app_context():
        # Exportar usuários
        users = User.query.all()
        users_data = []
        for user in users:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'password_hash': user.password_hash,
                'name': user.name,
                'bio': user.bio,
                'is_admin': user.is_admin,
                'created_at': user.created_at
            }
            users_data.append(user_dict)
        
        with open('export_users.json', 'w') as f:
            json.dump(users_data, f, default=json_serial, indent=2)
        
        # Exportar projetos
        projects = Project.query.all()
        projects_data = []
        for project in projects:
            project_dict = {
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'image_url': project.image_url,
                'link': project.link,
                'created_at': project.created_at
            }
            projects_data.append(project_dict)
        
        with open('export_projects.json', 'w') as f:
            json.dump(projects_data, f, default=json_serial, indent=2)
        
        # Exportar serviços
        services = Service.query.all()
        services_data = []
        for service in services:
            service_dict = {
                'id': service.id,
                'title': service.title,
                'description': service.description,
                'icon': service.icon,
                'price': service.price,
                'created_at': service.created_at
            }
            services_data.append(service_dict)
        
        with open('export_services.json', 'w') as f:
            json.dump(services_data, f, default=json_serial, indent=2)
        
        # Exportar depoimentos
        testimonials = Testimonial.query.all()
        testimonials_data = []
        for testimonial in testimonials:
            testimonial_dict = {
                'id': testimonial.id,
                'client_name': testimonial.client_name,
                'content': testimonial.content,
                'company': testimonial.company,
                'position': testimonial.position,
                'rating': testimonial.rating,
                'created_at': testimonial.created_at
            }
            testimonials_data.append(testimonial_dict)
        
        with open('export_testimonials.json', 'w') as f:
            json.dump(testimonials_data, f, default=json_serial, indent=2)
        
        # Exportar mensagens de chat
        messages = ChatMessage.query.all()
        messages_data = []
        for message in messages:
            message_dict = {
                'id': message.id,
                'sender_id': message.sender_id,
                'recipient_id': message.recipient_id,
                'content': message.content,
                'timestamp': message.timestamp,
                'read': message.read
            }
            messages_data.append(message_dict)
        
        with open('export_messages.json', 'w') as f:
            json.dump(messages_data, f, default=json_serial, indent=2)
        
        print("Exportação concluída com sucesso!")

def import_data():
    """Importa todos os dados dos arquivos JSON para o banco de dados."""
    with app.app_context():
        # Limpar todas as tabelas
        db.session.query(ChatMessage).delete()
        db.session.query(Testimonial).delete()
        db.session.query(Service).delete()
        db.session.query(Project).delete()
        db.session.query(User).delete()
        db.session.commit()
        
        # Importar usuários
        if os.path.exists('export_users.json'):
            with open('export_users.json', 'r') as f:
                users_data = json.load(f)
            
            for user_data in users_data:
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password_hash=user_data['password_hash'],
                    name=user_data['name'],
                    bio=user_data['bio'],
                    is_admin=user_data['is_admin'],
                    created_at=datetime.datetime.fromisoformat(user_data['created_at'])
                )
                db.session.add(user)
            
            db.session.commit()
        
        # Importar projetos
        if os.path.exists('export_projects.json'):
            with open('export_projects.json', 'r') as f:
                projects_data = json.load(f)
            
            for project_data in projects_data:
                project = Project(
                    title=project_data['title'],
                    description=project_data['description'],
                    image_url=project_data['image_url'],
                    link=project_data['link'],
                    created_at=datetime.datetime.fromisoformat(project_data['created_at'])
                )
                db.session.add(project)
            
            db.session.commit()
        
        # Importar serviços
        if os.path.exists('export_services.json'):
            with open('export_services.json', 'r') as f:
                services_data = json.load(f)
            
            for service_data in services_data:
                service = Service(
                    title=service_data['title'],
                    description=service_data['description'],
                    icon=service_data['icon'],
                    price=service_data['price'],
                    created_at=datetime.datetime.fromisoformat(service_data['created_at'])
                )
                db.session.add(service)
            
            db.session.commit()
        
        # Importar depoimentos
        if os.path.exists('export_testimonials.json'):
            with open('export_testimonials.json', 'r') as f:
                testimonials_data = json.load(f)
            
            for testimonial_data in testimonials_data:
                testimonial = Testimonial(
                    client_name=testimonial_data['client_name'],
                    content=testimonial_data['content'],
                    company=testimonial_data['company'],
                    position=testimonial_data['position'],
                    rating=testimonial_data['rating'],
                    created_at=datetime.datetime.fromisoformat(testimonial_data['created_at'])
                )
                db.session.add(testimonial)
            
            db.session.commit()
        
        # Importar mensagens de chat
        if os.path.exists('export_messages.json'):
            with open('export_messages.json', 'r') as f:
                messages_data = json.load(f)
            
            for message_data in messages_data:
                message = ChatMessage(
                    sender_id=message_data['sender_id'],
                    recipient_id=message_data['recipient_id'],
                    content=message_data['content'],
                    timestamp=datetime.datetime.fromisoformat(message_data['timestamp']),
                    read=message_data['read']
                )
                db.session.add(message)
            
            db.session.commit()
        
        print("Importação concluída com sucesso!")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python db_migration.py [export|import]")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'export':
        export_data()
    elif command == 'import':
        import_data()
    else:
        print("Comando desconhecido. Use 'export' ou 'import'.")
        sys.exit(1)