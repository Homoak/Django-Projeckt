// static/main/js/flip-card.js

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
      card.classList.toggle('flip');
    });
  });
});
