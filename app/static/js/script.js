//account
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

//admin_account
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

//booking
document.addEventListener("DOMContentLoaded", () => {
  const errorMessage = document.getElementById("booking-error");

  if (errorMessage && errorMessage.value) {
    alert(errorMessage.value);
  }
});

//contact
document.addEventListener("DOMContentLoaded", () => {
  const successMessage = document.getElementById("contact-success");

  if (successMessage && successMessage.value) {
    alert(successMessage.value);
  }
});

//footer
document.addEventListener("DOMContentLoaded", function () {
  const yearElement = document.getElementById("year");
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }
});

//header
document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('show');
    });
  }
});

//login
function showTab(tab) {
  const tabs = document.querySelectorAll('.login-tab');
  const titles = document.querySelectorAll('.login-tab-title');
  tabs.forEach(t => {
    t.classList.remove('active');
  });
  titles.forEach(title => {
    title.style.display = 'none';
  });
  document.getElementById(tab).classList.add('active');
  if (tab === 'login') {
    document.getElementById('login-title').style.display = 'block';
  } else if (tab === 'sign-up') {
    document.getElementById('signup-title').style.display = 'block';
  }
}