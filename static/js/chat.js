// Chat functionality for SeuCodigo

document.addEventListener('DOMContentLoaded', function() {
  const chatContainer = document.querySelector('.chat-container');
  const messageForm = document.getElementById('message-form');
  const messageInput = document.getElementById('content');
  const partnerId = document.getElementById('partner-id')?.value;
  
  // Scroll chat to bottom
  function scrollChatToBottom() {
    if (chatContainer) {
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  }
  
  // Initialize chat scroll position
  scrollChatToBottom();
  
  // Send message via AJAX
  if (messageForm && partnerId) {
    messageForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const content = messageInput.value.trim();
      if (!content) return;
      
      fetch('/api/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          content: content,
          recipient_id: parseInt(partnerId)
        }),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        // Add the new message to the chat
        addMessageToChat(data);
        
        // Clear the input
        messageInput.value = '';
        
        // Scroll to the bottom of the chat
        scrollChatToBottom();
      })
      .catch(error => {
        console.error('Error sending message:', error);
        alert('Erro ao enviar mensagem. Por favor, tente novamente.');
      });
    });
  }
  
  // Add message to the chat interface
  function addMessageToChat(message) {
    if (!chatContainer) return;
    
    const messageElement = document.createElement('div');
    
    // Get current user ID from data attribute
    const currentUserId = parseInt(chatContainer.dataset.currentUser);
    
    // Check if message is from current user
    const isFromCurrentUser = message.sender_id === currentUserId;
    
    // Build message class based on sender
    const messageClass = isFromCurrentUser ? 'chat-message chat-message-user' : 'chat-message chat-message-admin';
    
    // Format timestamp
    const timestamp = new Date(message.timestamp);
    const formattedTime = timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    
    // Set message content
    messageElement.className = messageClass;
    messageElement.innerHTML = `
      <div class="mb-1 font-bold">${isFromCurrentUser ? 'Você' : message.sender_name}</div>
      <div>${message.content}</div>
      <div class="text-xs text-right mt-1 opacity-75">${formattedTime}</div>
    `;
    
    // Add to chat container
    chatContainer.appendChild(messageElement);
  }
  
  // Periodic check for new messages
  function fetchMessages() {
    if (!chatContainer || !partnerId) return;
    
    fetch(`/api/messages?partner_id=${partnerId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(messages => {
        // Clear existing messages
        chatContainer.innerHTML = '';
        
        // Add all messages
        messages.forEach(message => {
          addMessageToChat(message);
        });
        
        // Scroll to bottom
        scrollChatToBottom();
      })
      .catch(error => {
        console.error('Error fetching messages:', error);
      });
  }
  
  // Initial fetch
  if (chatContainer && partnerId) {
    fetchMessages();
    
    // Fetch new messages every 5 seconds
    setInterval(fetchMessages, 5000);
  }
  
  // Handle admin chat user selection
  const chatUserLinks = document.querySelectorAll('.chat-user-link');
  
  chatUserLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Remove active class from all user links
      chatUserLinks.forEach(el => el.classList.remove('bg-indigo-100'));
      
      // Add active class to clicked link
      this.classList.add('bg-indigo-100');
      
      // Update the chat interface with the selected user
      const userId = this.dataset.userId;
      window.location.href = `/admin/chats?user_id=${userId}`;
    });
  });
});
