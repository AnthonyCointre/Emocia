document.addEventListener("DOMContentLoaded", () => {
  const errorMessage = document.getElementById("booking-error");

  if (errorMessage && errorMessage.value) {
    alert(errorMessage.value);
  }
});