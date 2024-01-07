document.querySelector('#currentYear').innerHTML = new Date().getFullYear();

document.querySelectorAll('.btn').forEach((button) => {
  button.addEventListener('click', (e) => {
    e.target.textContent = 'Loading...';
  });
});
