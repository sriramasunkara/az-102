const form = document.getElementById('chat-form');
const input = document.getElementById('message-input');
const messagesDiv = document.getElementById('messages');
const resetBtn = document.getElementById('reset-btn');

function appendMessage(role, text) {
  const el = document.createElement('div');
  el.className = 'message ' + role;
  el.textContent = (role === 'user' ? 'You: ' : 'Assistant: ') + text;
  messagesDiv.appendChild(el);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  appendMessage('user', text);
  input.value = '';

  const resp = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: text })
  });

  if (!resp.ok) {
    const err = await resp.json().catch(() => ({ error: 'Unknown error' }));
    appendMessage('assistant', 'Error: ' + (err.error || 'Request failed'));
    return;
  }

  const data = await resp.json();
  appendMessage('assistant', data.reply || '');
});

resetBtn.addEventListener('click', async () => {
  await fetch('/api/reset', { method: 'POST' });
  messagesDiv.innerHTML = '';
  appendMessage('assistant', 'Conversation reset.');
});
