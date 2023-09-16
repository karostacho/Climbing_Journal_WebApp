from database.password import password
from database.sql_data import SqlData
from database.user_db import add_user_to_db, check_if_user_in_db, find_user_password

import psycopg2
import itertools

conn = psycopg2.connect(
            host='snuffleupagus.db.elephantsql.com',
            port='5432',
            database='qpgrmemq',
            user='qpgrmemq',
            password=password
            )
            #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCurso
cursor = conn.cursor()
#climbing_type_table = 'rock_climbing_grades'
#cursor.execute((f'SELECT * FROM {climbing_type_table} LIMIT 0'))
#rating_systems = [desc[0] for desc in cursor.description[1:]]
#print(rating_systems)

#cursor.execute(f'SELECT * FROM {climbing_type_table}')
#data = [dict(zip(rating_systems, row)) for row in cursor.fetchall()]

#cursor.close()
#conn.close()
# Print the resulting list of dictionaries
#print(data)

climbing_type = 'rock_climbing_grades'
routes_type = 'lead_climbing_routes'

sql = SqlData()
user = find_user_password('tomek@test.pl')

print(user[0])


// Not logged in window when user is not logged and click on "Journal"

  const modal = document.getElementById('notLoggedInWindow');
  const openBtn = document.getElementById('openNotLoggedIn');
  const closeBtn = document.getElementById('closeLoggedIn');

// Open modal
  openBtn.addEventListener('click', () => {
  modal.style.display = 'block';
  openBtn.style.display = 'none';
});

// Close modal
closeBtn.addEventListener('click', () => {
  modal.style.display = 'none';
  openBtn.style.display = 'block';
});
// Close on outside click 
window.addEventListener('click', (e) => {
  if (e.target === modal && !modal.contains(e.target)) {
    modal.style.display = 'none';
  }
});

// Stop propagation on inner clicks
modal.addEventListener('click', e => {
  e.stopPropagation();
});



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