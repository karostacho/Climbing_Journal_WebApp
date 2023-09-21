// Add route modal window  
  
const modal = document.getElementById('addRouteWindow');
const openBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementById('closeModalBtn');
const submitBtn = document.getElementById('submitBtn');


// Open modal
openBtn.addEventListener('click', () => {
  modal.style.display = 'block';
  openBtn.style.display = 'none';
});

submitBtn.addEventListener('click', () => {
  const date = document.querySelector('input[name="date"]').value;
  const routeName = document.querySelector('input[name="route_name"]').value;
  const gradeFields = document.querySelectorAll('input[name="french"], input[name="kurtyka"], input[name="uiaa"], input[name="usa"], input[name="british"]');

  if (!date || !routeName || [...gradeFields].some(field => !field.value)){
    modal.style.display = 'block';
    openBtn.style.display = 'none';
  }
});

// Close modal
closeBtn.addEventListener('click', () => {
  modal.style.display = 'none';
  openBtn.style.display = 'block';
  
  // Reset form
  document.querySelector('form').reset(); 
});


// Stop propagation on inner clicks
modal.addEventListener('click', e => {
  e.stopPropagation();
});









// Dropdown selection reset in add route window
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



