function signup() {
	
	alert("Please wait for a moment.");
	
	Parse.initialize("3lKrL4HTUMbclk8CikblOpWZlJA7OLWkI7BMxP03", "vLhckw4U9M0TtXcPjEQLIOpnC1e8enWURTMlyoUb");
	
	var user = new Parse.User();
	user.set("username",document.getElementsByName("email")[0].value)
	user.set("first", document.getElementsByName("fname")[0].value);
	user.set("last", document.getElementsByName("lname")[0].value);
	user.set("email", document.getElementsByName("email")[0].value);
	user.set("password", document.getElementsByName("pass")[0].value);
	
	user.signUp(null, {
	  success: function(user) {
    alert("A verification email has been sent to you. Please verify your email.");
    document.getElementsByName("fname")[0].value = "";
    document.getElementsByName("lname")[0].value = "";
    document.getElementsByName("email")[0].value = "";
    document.getElementsByName("pass")[0].value = "";
    document.getElementsByName("pass_confirmation")[0].value = "";

  },
  error: function(user, error) {
    // Show the error message somewhere and let the user try again.
    alert("Error: " + error.message); //+ error.code + " " + error.message);
  }
});
}

