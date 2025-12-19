document.addEventListener('DOMContentLoaded', function () {
  const deleteForms = document.querySelectorAll('.deleteForm');
  deleteForms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
      const confirmDelete = confirm("Are you sure you want to delete this item? This action cannot be undone.");
      if (!confirmDelete) {
        event.preventDefault();
      }
    });
  });
});