document.addEventListener('DOMContentLoaded', function () {
  const deleteForm = document.getElementById('deleteAccountForm');
  if (deleteForm) {
    deleteForm.addEventListener('submit', function (event) {
      const confirmDelete = confirm("Are you sure you want to delete your account? This action cannot be undone.");
      if (!confirmDelete) {
        event.preventDefault();
      }
    });
  }
});