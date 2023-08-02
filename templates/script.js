document.addEventListener("DOMContentLoaded", function () {
    const rockClimbingForm = document.getElementById("rockClimbingForm");
    const boulderingForm = document.getElementById("boulderingForm");
  
    function handleFormSubmit(form) {
      const formData = new FormData(form);
  
      fetch("/", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          const rockResults = data.rock_results;
          const boulderingResults = data.bouldering_results;
  
          // Update the rock climbing grades
          const rockClimbingDropdowns = rockClimbingForm.querySelectorAll(".grade-dropdowns select");
          updateDropdowns(rockClimbingDropdowns, rockResults);
  
          // Update the bouldering grades
          const boulderingDropdowns = boulderingForm.querySelectorAll(".grade-dropdowns select");
          updateDropdowns(boulderingDropdowns, boulderingResults);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  
    function updateDropdowns(dropdowns, results) {
      dropdowns.forEach((dropdown, index) => {
        dropdown.value = results[index];
      });
    }
  
    rockClimbingForm.addEventListener("submit", function (event) {
      event.preventDefault();
      handleFormSubmit(rockClimbingForm);
    });
  
    boulderingForm.addEventListener("submit", function (event) {
      event.preventDefault();
      handleFormSubmit(boulderingForm);
    });
  });