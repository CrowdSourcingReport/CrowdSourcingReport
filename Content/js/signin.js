function signin() {

	Parse.initialize("3lKrL4HTUMbclk8CikblOpWZlJA7OLWkI7BMxP03", "vLhckw4U9M0TtXcPjEQLIOpnC1e8enWURTMlyoUb");
	
	var user = new Parse.User();
	Parse.User.logIn(document.getElementById("user_username"), document.getElementById("user_password"), {
		success: function(user) {
		// Do stuff after successful login.
		},
		error: function(user, error) {
			// The login failed. Check error to see why.
		}
	});
}

