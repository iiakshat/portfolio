document.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("loaded");
  const homeContainer = document.querySelector(".homecontainer");
  if (homeContainer) {
    homeContainer.classList.add("loaded");
  }
});

document.addEventListener("DOMContentLoaded", function() {
  const aboutSection = document.querySelector(".about-section");
  if (aboutSection) {
    aboutSection.classList.add("loaded");
  }
});
