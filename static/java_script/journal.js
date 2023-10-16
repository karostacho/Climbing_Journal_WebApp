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


function getGradeValue(scale) {
	var grade = document.getElementById(scale);
	return grade.value
}


function validationForm() {
	var french = getGradeValue('french');
	var kurtyka = getGradeValue('kurtyka');
	var british = getGradeValue('british');
	var uiaa = getGradeValue('uiaa');
	var usa = getGradeValue('usa');


	if (!french && !kurtyka && !british && !uiaa && !usa) {
		alert('Grade must be selected')
		return false
	}
	else {
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


//TODO repeta
function toggleDatetOrder() {
	const dateForm = document.getElementById('sortDateForm')
	const dateOrder = document.getElementById('sortDateOrder');
	const storedDateOrder = localStorage.getItem('sortDateOrder');


	if (storedDateOrder) {
		dateOrder.value = storedDateOrder;
	}

	if (dateOrder.value === 'DESC') {
		dateOrder.value = 'ASC';
	}
	else {
		dateOrder.value = 'DESC';
	}

	localStorage.setItem('sortDateOrder', dateOrder.value);

	dateForm.submit();
}


function toggleGradeOrder() {
	const gradeForm = document.getElementById('sortGradeForm');
	const gradeOrder = document.getElementById('sortGradeOrder');
	const storedGradeOrder = localStorage.getItem('sortGradeOrder');


	if (storedGradeOrder) {
		gradeOrder.value = storedGradeOrder;
	}

	if (gradeOrder.value === 'DESC') {
		gradeOrder.value = 'ASC';
	}
	else {
		gradeOrder.value = 'DESC';
	}

	localStorage.setItem('sortGradeOrder', gradeOrder.value);

	gradeForm.submit();
}


function deleteRoute(routeId) {
	if (confirm("Are you sure you want to delete this route?")) {
		document.getElementById('deleteRoute').value = routeId;
		const deleteForm = document.getElementById('deleteRouteForm');
		deleteForm.submit()
	}
}
