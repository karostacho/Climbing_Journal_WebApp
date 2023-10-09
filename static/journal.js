// Add route modal window  
  
const modal = document.getElementById('addRouteWindow');
const openBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementById('closeModalBtn');
const submitBtn = document.getElementById('submitBtn');
var currentDate = new Date().toISOString().split('T')[0];
var date = document.getElementById('date');
  
  date.setAttribute('max', currentDate);

// Open modal
openBtn.addEventListener('click', () => {
  modal.style.display = 'block';
  openBtn.style.display = 'none';
  date.value = currentDate;
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

function getGradeValue(scale){
  var grade = document.getElementById(scale);
  return grade.value
  }

function validationForm(){
  var french = getGradeValue('french');
  var kurtyka = getGradeValue('kurtyka');
  var british = getGradeValue('british');
  var uiaa = getGradeValue('uiaa');
  var usa = getGradeValue('usa');
  

  if (!french && !kurtyka && !british && !uiaa && !usa)  {
    alert ('Grade must be selected')
    return false
  }
  else{
    return true
  }
}


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


  var currentSortOrder = "DESC"; // Initial sorting order

  function toggleSortOrder() {
      // Toggle sorting order between ASC and DESC
      if (currentSortOrder === "ASC") {
          currentSortOrder = "DESC";
      } else {
          currentSortOrder = "ASC";
      }

      // Update the hidden input value
      var sortOrderInput = document.querySelector('input[name="sortOrder"]');
      sortOrderInput.value = currentSortOrder;

      // Trigger form submission
      document.getElementById('sortForm').submit();
  }