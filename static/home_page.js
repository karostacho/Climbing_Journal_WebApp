// Not logged in window when user is not logged and click on "Journal"

window.onload=function(){
	const notLoggedInWindow = document.getElementById("notLoggedInWindow");
	const openNotLoggedIn = document.getElementById("openNotLoggedIn");
	const closeLoggedIn = document.getElementById("closeLoggedIn");
	// For Mobile navbar
	const navbar_menu_btn = document.getElementById("navbar-menu-btn");
	const menu_mobile = document.getElementById("menu-mobile");

	// Open modal
	openNotLoggedIn.addEventListener("click", () => {
		notLoggedInWindow.style.display = "block";
	});

	// Close modal
	closeLoggedIn.addEventListener("click", () => {
		notLoggedInWindow.style.display = "none";
	});

	// Stop propagation on inner clicks
	notLoggedInWindow.addEventListener("click", (e) => {
		e.stopPropagation();
	});

	// JavaScript to toggle navbar open/close
	navbar_menu_btn.addEventListener("click", () => {
		menu_mobile.classList.toggle("open");
	});
}
