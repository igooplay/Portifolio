import os
import uuid
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg', 'ico', 'webp'}
UPLOAD_FOLDER = 'static/uploads'

def allowed_file(filename):
    """Verifica se a extensão do arquivo é permitida"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file, subfolder='logo'):
    """Salva o arquivo enviado e retorna o caminho"""
    if not file or file.filename == '':
        return None
        
    if allowed_file(file.filename):
        # Gera um nome único para o arquivo
        filename = secure_filename(file.filename)
        # Adiciona um ID único para evitar colisões de nomes
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        
        # Cria o diretório se não existir
        directory = os.path.join(UPLOAD_FOLDER, subfolder)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        # Caminho completo para salvar o arquivo
        file_path = os.path.join(directory, unique_filename)
        
        # Salva o arquivo
        file.save(file_path)
        
        # Retorna o path relativo para uso no HTML
        return f"/{file_path}"
    
    return None