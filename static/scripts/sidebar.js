document.addEventListener("DOMContentLoaded", function(event) {
  update_sidebar()
  const menuIconButton = document.querySelector("[data-menu-icon-btn]")
  var sidebar = document.querySelector("[data-sidebar]")
  var header_height = document.querySelector(".header").clientHeight
  header_height = header_height.toString() + "px"
  document.documentElement.style.setProperty('--header-height', header_height);
  menuIconButton.addEventListener("click", () => {
    sidebar.classList.toggle("open")
  })
});

function update_sidebar(){
  var page_identifier = document.getElementById("page-identifier").value
  const sidebar_section = document.getElementById(page_identifier)
  sidebar_section.classList.add("active")
}
