const hamburger = document.querySelector(".hamburger");
const mobileMenu = document.querySelector(".mobile-menu");

hamburger.addEventListener("click", () => {
  mobileMenu.classList.toggle("show");
});

function toggleChatbot() {
  const chatbotContainer = document.getElementById('chatbotContainer');
  chatbotContainer.style.display = chatbotContainer.style.display === 'none' ? 'block' : 'none';
}

async function sendMessage() {
  const input = document.getElementById('chatbotInput');
  const message = input.value;
  if (message.trim() === '') return;

  displayMessage('You', message);
  input.value = '';

  try {
      const response = await getChatbotResponse(message);
      displayMessage('Bot', response.answer);
  } catch (error) {
      console.error('Error:', error);
  }
}

function displayMessage(sender, message) {
  const messagesContainer = document.getElementById('chatbotMessages');
  const messageElement = document.createElement('div');
  messageElement.textContent = `${sender}: ${message}`;
  messagesContainer.appendChild(messageElement);
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

async function getChatbotResponse(message) {
  const response = await fetch('http://127.0.0.1:8000/api_reply/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ question: message })
  });     
  console.log(response);
  if (!response.ok) {
      throw new Error('Network response was not ok');
  }
  return await response.json();

}

document.getElementById('chatbotInput').addEventListener('keypress', function (event) {
  if (event.key === 'Enter') {
      sendMessage();
  }
});