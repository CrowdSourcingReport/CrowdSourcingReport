$('#navbar').load("/Content/html/navbar.html");

$('document').ready(function () {
    LoadNavbar('Home');
});

function LoadNavbar(locator){  
	if(locator=='Home'){	
		$('#Home').attr("class", "active");
	}
}   



       
