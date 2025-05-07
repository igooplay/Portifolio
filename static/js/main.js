// Main JavaScript for the SeuCodigo portfolio website

document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle
  const mobileMenuButton = document.getElementById('mobile-menu-button');
  const mobileMenu = document.getElementById('mobile-menu');
  
  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', function() {
      mobileMenu.classList.toggle('hidden');
      mobileMenu.classList.toggle('block');
    });
  }
  
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80, // Offset for the fixed header
          behavior: 'smooth'
        });
        
        // Update URL hash without jumping
        history.pushState(null, null, targetId);
      }
    });
  });
  
  // Add animation to elements when they become visible
  const animatedElements = document.querySelectorAll('.animate-on-scroll');
  
  function checkVisibility() {
    animatedElements.forEach(element => {
      const elementTop = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (elementTop < windowHeight - 100) {
        const animationClass = element.dataset.animation || 'fade-in';
        element.classList.add(animationClass);
      }
    });
  }
  
  // Run on initial load
  checkVisibility();
  
  // Run on scroll
  window.addEventListener('scroll', checkVisibility);
  
  // Flash messages auto-dismiss
  const flashMessages = document.querySelectorAll('.flash-message');
  
  flashMessages.forEach(message => {
    setTimeout(() => {
      message.classList.add('opacity-0');
      message.addEventListener('transitionend', () => {
        message.remove();
      });
    }, 5000);
  });
  
  // Form validations
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      const requiredFields = form.querySelectorAll('[required]');
      let valid = true;
      
      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          valid = false;
          
          // Add error class to parent formgroup
          const formGroup = field.closest('.form-group');
          if (formGroup) {
            formGroup.classList.add('has-error');
          }
          
          // Add error message if doesn't exist
          let errorMessage = field.nextElementSibling;
          if (!errorMessage || !errorMessage.classList.contains('error-message')) {
            errorMessage = document.createElement('p');
            errorMessage.classList.add('error-message', 'text-red-500', 'text-sm', 'mt-1');
            errorMessage.innerText = 'Este campo é obrigatório';
            field.parentNode.insertBefore(errorMessage, field.nextSibling);
          }
        }
      });
      
      if (!valid) {
        e.preventDefault();
      }
    });
  });
  
  // Initialize ratings display
  const ratingElements = document.querySelectorAll('.rating-stars');
  
  ratingElements.forEach(element => {
    const rating = parseInt(element.dataset.rating) || 0;
    let starsHtml = '';
    
    for (let i = 1; i <= 5; i++) {
      if (i <= rating) {
        starsHtml += '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-yellow-500" viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" /></svg>';
      } else {
        starsHtml += '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-300" viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" /></svg>';
      }
    }
    
    element.innerHTML = starsHtml;
  });
  
  // WhatsApp button event
  const whatsappBtn = document.getElementById('whatsapp-btn');
  if (whatsappBtn) {
    whatsappBtn.addEventListener('click', function() {
      // Default WhatsApp number can be replaced with dynamic one from the server
      const phoneNumber = whatsappBtn.dataset.phone || '5500000000000';
      const message = encodeURIComponent('Olá! Vim do seu site e gostaria de mais informações.');
      window.open(`https://wa.me/${phoneNumber}?text=${message}`, '_blank');
    });
  }
});
