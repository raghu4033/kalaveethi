// start logi page js
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
// end login page js
$(document).ready(function() {

  // SideNav Button Initialization
  $(".button-collapse").sideNav();
  // SideNav Scrollbar Initialization
  var sideNavScrollbar = document.querySelector('.custom-scrollbar');
  var ps = new PerfectScrollbar(sideNavScrollbar);
})
// end admin_header 
