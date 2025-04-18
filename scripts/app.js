// Add to app.js
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  document.querySelector('header').style.background = scrollY > 50 
    ? 'rgba(15, 23, 42, 0.95)' 
    : 'rgba(15, 23, 42, 0.5)';
});
