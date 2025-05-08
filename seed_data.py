import datetime
from app import app, db
from models import User, Project, Service, Testimonial
from werkzeug.security import generate_password_hash

def seed_database():
    """
    Popula o banco de dados com informações iniciais de usuário admin, projetos, serviços e depoimentos.
    """
    print("Inicializando o banco de dados com dados de exemplo...")
    
    # Verifica se já existe um usuário admin
    existing_admin = User.query.filter(User.is_admin == True).first()
    if not existing_admin:
        print("Criando usuário administrador...")
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
        print(f"Usuário admin criado com ID: {admin.id}")
    else:
        print(f"Usuário admin já existe com ID: {existing_admin.id}")
    
    # Verifica se já existem projetos
    if Project.query.count() == 0:
        print("Criando projetos de exemplo...")
        projects = [
            {
                "title": "E-commerce Responsivo",
                "description": "Desenvolvimento de loja virtual completa com sistema de pagamento integrado, carrinho de compras e painel administrativo.",
                "image_url": "https://images.unsplash.com/photo-1523474253046-8cd2748b5fd2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
                "link": "https://exemplo.com/projeto1"
            },
            {
                "title": "Aplicativo de Gestão Financeira",
                "description": "Sistema web para controle financeiro pessoal com gráficos e relatórios detalhados sobre entradas, saídas e investimentos.",
                "image_url": "https://images.unsplash.com/photo-1563986768609-322da13575f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
                "link": "https://exemplo.com/projeto2"
            },
            {
                "title": "Portal Institucional",
                "description": "Desenvolvimento de portal institucional para empresa de grande porte, com área de notícias, contato e intranet.",
                "image_url": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?ixlib=rb-1.2.1&auto=format&fit=crop&w=1055&q=80",
                "link": "https://exemplo.com/projeto3"
            },
            {
                "title": "Sistema de Agendamento Online",
                "description": "Plataforma para profissionais autônomos gerenciarem agendamentos, clientes e pagamentos de forma eficiente.",
                "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
                "link": "https://exemplo.com/projeto4"
            },
            {
                "title": "Marketplace de Cursos",
                "description": "Plataforma online para venda e compra de cursos digitais com sistema de streaming de vídeo e recursos educacionais.",
                "image_url": "https://images.unsplash.com/photo-1501504905252-473c47e087f8?ixlib=rb-1.2.1&auto=format&fit=crop&w=1074&q=80",
                "link": "https://exemplo.com/projeto5"
            }
        ]
        
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        
        db.session.commit()
        print(f"Criados {len(projects)} projetos de exemplo")
    else:
        print(f"Já existem {Project.query.count()} projetos no banco")
    
    # Verifica se já existem serviços
    if Service.query.count() == 0:
        print("Criando serviços de exemplo...")
        services = [
            {
                "title": "Desenvolvimento Web",
                "description": "Criação de sites modernos, responsivos e otimizados para SEO utilizando as tecnologias mais recentes do mercado.",
                "icon": "fas fa-code",
                "price": 2500.00
            },
            {
                "title": "E-commerce",
                "description": "Desenvolvimento de lojas virtuais completas com controle de estoque, pagamento seguro e experiência de compra personalizada.",
                "icon": "fas fa-shopping-cart",
                "price": 4500.00
            },
            {
                "title": "Design Responsivo",
                "description": "Layout adaptativo que funciona perfeitamente em todos os dispositivos, desde celulares até desktops.",
                "icon": "fas fa-laptop-code",
                "price": 1800.00
            },
            {
                "title": "Desenvolvimento Backend",
                "description": "Implementação de APIs robustas, seguras e escaláveis para aplicações web e mobile.",
                "icon": "fas fa-database",
                "price": 3200.00
            },
            {
                "title": "Marketing Digital",
                "description": "Estratégias completas de marketing online para aumentar a visibilidade da sua marca e converter visitantes em clientes.",
                "icon": "fas fa-bullhorn",
                "price": 1500.00
            },
            {
                "title": "Consultoria em Tecnologia",
                "description": "Aconselhamento especializado para escolha das melhores tecnologias e práticas para seu projeto ou negócio digital.",
                "icon": "fas fa-users",
                "price": 900.00
            }
        ]
        
        for service_data in services:
            service = Service(**service_data)
            db.session.add(service)
        
        db.session.commit()
        print(f"Criados {len(services)} serviços de exemplo")
    else:
        print(f"Já existem {Service.query.count()} serviços no banco")
    
    # Verifica se já existem depoimentos
    if Testimonial.query.count() == 0:
        print("Criando depoimentos de exemplo...")
        testimonials = [
            {
                "client_name": "Carlos Silva",
                "content": "O desenvolvimento do nosso site superou todas as expectativas. A equipe foi extremamente profissional e entregou o projeto antes do prazo previsto. Recomendo fortemente!",
                "company": "Silva & Associados",
                "position": "Diretor Executivo",
                "rating": 5
            },
            {
                "client_name": "Ana Ferreira",
                "content": "Nossa experiência com a SeuCodigo foi excepcional. Eles transformaram nossa presença online e ajudaram a aumentar nossas vendas em mais de 70% nos primeiros três meses.",
                "company": "Boutique Online",
                "position": "Proprietária",
                "rating": 5
            },
            {
                "client_name": "Marcelo Costa",
                "content": "Excelente trabalho na criação do nosso sistema de gestão. A interface é intuitiva e tudo funciona exatamente como precisávamos. Estamos muito satisfeitos com o resultado.",
                "company": "Tech Solutions",
                "position": "Gerente de Projetos",
                "rating": 4
            },
            {
                "client_name": "Juliana Santos",
                "content": "A atenção aos detalhes e o suporte técnico oferecido pela equipe foram fundamentais para o sucesso do nosso projeto. Certamente trabalharemos juntos novamente.",
                "company": "Arquitetura Moderna",
                "position": "Diretora Criativa",
                "rating": 5
            },
            {
                "client_name": "Pedro Mendes",
                "content": "O aplicativo desenvolvido trouxe uma nova dimensão para nosso negócio. A integração com nossos sistemas existentes foi perfeita e agora conseguimos atender nossos clientes com muito mais eficiência.",
                "company": "Delivery Express",
                "position": "CEO",
                "rating": 5
            }
        ]
        
        for testimonial_data in testimonials:
            testimonial = Testimonial(**testimonial_data)
            db.session.add(testimonial)
        
        db.session.commit()
        print(f"Criados {len(testimonials)} depoimentos de exemplo")
    else:
        print(f"Já existem {Testimonial.query.count()} depoimentos no banco")
    
    print("Inicialização do banco de dados concluída!")

if __name__ == "__main__":
    with app.app_context():
        seed_database()