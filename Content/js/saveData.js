function saveData(){
	if(typeof(Storage) !== "undefined") {
		sessionStorage.user = document.getElementById("user_username").value;
		sessionStorage.pass = document.getElementById("user_password").value;
		sessionStorage.remember = document.getElementById("user_remember_me").checked;
	} else {
    // Sorry! No Web Storage support..
	}
}

