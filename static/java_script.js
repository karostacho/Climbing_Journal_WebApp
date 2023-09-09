// Add route modal window  
  
  const modal = document.getElementById('addRouteWindow');
  const openBtn = document.getElementById('openModalBtn');
  const closeBtn = document.getElementById('closeModalBtn');

// Open modal
openBtn.addEventListener('click', () => {
  modal.style.display = 'block';
  openBtn.style.display = 'none';
});

// Close modal
closeBtn.addEventListener('click', () => {
  modal.style.display = 'none';
  openBtn.style.display = 'block';
  
  // Reset form
  document.querySelector('form').reset(); 
});

// Close on outside click 
window.addEventListener('click', (e) => {
  if (e.target === modal && !modal.contains(e.target)) {
    modal.style.display = 'none';
    
    // Reset form 
    document.querySelector('form').reset();
  }
});

// Stop propagation on inner clicks
modal.addEventListener('click', e => {
  e.stopPropagation();
});



// Dropdown selection reset
  const dropdowns = document.querySelectorAll('.grade-dropdowns select');
  
  dropdowns.forEach(dropdown => {
      dropdown.addEventListener('change', () => {
          // Reset all other dropdowns
          dropdowns.forEach(otherDropdown => {
              if (otherDropdown !== dropdown) {
                  otherDropdown.selectedIndex = 0;
              }
          });
      });
  });