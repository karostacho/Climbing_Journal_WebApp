///Common .js file for all relevant views

// For Mobile navbar
const navbar_menu_btn = document.getElementById("navbar-menu-btn");
const menu_mobile = document.getElementById("menu-mobile");

// JavaScript to toggle mobile navbar open/close
navbar_menu_btn.addEventListener("click", () => {
	menu_mobile.classList.toggle("open");
});
