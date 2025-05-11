// Script para formulário de configurações

// Função para mostrar prévia da imagem ao selecionar arquivo
function previewImage(inputId, previewId) {
    const input = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    
    if (input) {
        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    preview.src = e.target.result;
                }
                
                reader.readAsDataURL(file);
            }
        });
    }
}

// Inicializar previews de imagens quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    // Prévia do logo
    previewImage('logo_file', 'logo-preview');
    
    // Prévia do favicon
    previewImage('favicon_file', 'favicon-preview');
    
    // Atualizar preview quando a URL mudar também
    const logoUrlInput = document.getElementById('logo_url');
    if (logoUrlInput) {
        logoUrlInput.addEventListener('input', function() {
            const preview = document.getElementById('logo-preview');
            if (this.value) {
                preview.src = this.value;
            } else {
                preview.src = '/static/img/placeholder-logo.svg';
            }
        });
    }
    
    const faviconUrlInput = document.getElementById('favicon_url');
    if (faviconUrlInput) {
        faviconUrlInput.addEventListener('input', function() {
            const preview = document.getElementById('favicon-preview');
            if (this.value) {
                preview.src = this.value;
            } else {
                preview.src = '/static/img/placeholder-favicon.svg';
            }
        });
    }
});