function signup() {
	Parse.initialize("3lKrL4HTUMbclk8CikblOpWZlJA7OLWkI7BMxP03", "vLhckw4U9M0TtXcPjEQLIOpnC1e8enWURTMlyoUb");

	var user = new Parse.User();
	user.set("first", document.getElementsBydName[0]("fname").value);
	user.set("last", document.getElementsBydName[0]("lname").value);
	user.set("email", document.getElementsByName[0]("email").value);
	user.set("password", document.getElementsByName[0]("pass").value);
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

