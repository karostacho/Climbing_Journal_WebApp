// Add route modal window  
  
const modal = document.getElementById('addRouteWindow');
const openBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementById('closeModalBtn');
const submitBtn = document.getElementById('submitBtn');
var currentDate = new Date().toISOString().split('T')[0];
var date = document.getElementById("date");
  
  date.setAttribute("max", currentDate);

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



function validationForm(){
  var french = document.getElementById("french");
  var kurtyka = document.getElementById("kurtyka");
  var british = document.getElementById("british");
  var uiaa = document.getElementById("uiaa");
  var usa = document.getElementById("usa");
  
  var frenchValue = french.value;
  var kurtykaValue = kurtyka.value;
  var britishValue = british.value;
  var uiaaValue = uiaa.value;
  var usaValue = usa.value;


  if (!frenchValue && !britishValue && !kurtykaValue && !uiaaValue && !usaValue)  {
    alert ("Grade must be selected")
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



  function updateData() {
    // Prevent the default link behavior
    

    // Get the link element by its id
    

    // Get the current href attribute value
    let href = link.getAttribute('href');
    if (href.includes('sort_order=asc')) {
      // Replace 'asc' with 'desc' in the href attribute
      href = href.replace('sort_order=asc', 'sort_order=desc');
    }

    // Check if the current sort_order is 'desc' or 'asc'
    if (href.includes('sort_order=desc')) {
      // Replace 'desc' with 'asc' in the href attribute
      href = href.replace('sort_order=desc', 'sort_order=asc');
    } 

    // Update the href attribute
    link.setAttribute('href', href);

    
  }