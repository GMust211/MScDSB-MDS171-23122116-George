document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    
    alert('Login successful! Redirecting to mailbox...');
    window.location.href = 'mailbox.html';
  });