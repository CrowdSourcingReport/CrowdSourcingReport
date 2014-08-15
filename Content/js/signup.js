function signup() {
	Parse.initialize("3lKrL4HTUMbclk8CikblOpWZlJA7OLWkI7BMxP03", "vLhckw4U9M0TtXcPjEQLIOpnC1e8enWURTMlyoUb");

	var user = new Parse.User();
	user.set("first", document.getElementsByName("fname")[0].value);
	user.set("last", document.getElementsByName("lname")[0].value);
	user.set("email", document.getElementsByName("email")[0].value);
	user.set("password", document.getElementsByName("pass")[0].value);
	console.log("I am here");  
	user.signUp(null, {
	  success: function(user) {
    // Hooray! Let them use the app now.
  },
  error: function(user, error) {
    // Show the error message somewhere and let the user try again.
    alert("Error: " + error.code + " " + error.message);
  }
});
}

