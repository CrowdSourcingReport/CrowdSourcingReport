function signin() {

	Parse.initialize("12ySyuWoqXJ4lRxzGzr7xJeN4p7rnIsWUguNSQG3", "12ySyuWoqXJ4lRxzGzr7xJeN4p7rnIsWUguNSQG3");
	
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

