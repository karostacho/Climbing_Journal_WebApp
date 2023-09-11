// Not logged in window when user is not logged and click on "Journal"
window.onload=function(){
    const notLoggedInWindow = document.getElementById('notLoggedInWindow');
    const openNotLoggedIn = document.getElementById('openNotLoggedIn');
    const closeLoggedIn = document.getElementById('closeLoggedIn');
    
    // Open modal
    openNotLoggedIn.addEventListener('click', () => {
      notLoggedInWindow.style.display = 'block';
    
    });
    
    // Close modal
    closeLoggedIn.addEventListener('click', () => {
      notLoggedInWindow.style.display = 'none';
    });
    // Close on outside click 
    window.addEventListener('click', (e) => {
    if (e.target === modal && !notLoggedInWindow.contains(e.target)) {
      notLoggedInWindow.style.display = 'none';
    }
    });
    
    // Stop propagation on inner clicks
    notLoggedInWindow.addEventListener('click', e => {
    e.stopPropagation();
    });}