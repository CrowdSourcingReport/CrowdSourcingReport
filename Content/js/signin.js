Parse.initialize("3lKrL4HTUMbclk8CikblOpWZlJA7OLWkI7BMxP03", "vLhckw4U9M0TtXcPjEQLIOpnC1e8enWURTMlyoUb");
alert(sessionStorage.user + sessionStorage.pass);
Parse.User.logIn(sessionStorage.user, sessionStorage.pass, {
  success: function(user) {
    // Do stuff after successful login.
	alert("Success");
  },
  error: function(user, error) {
    // The login failed. Check error to see why.
	alert(error.message);
  }
});