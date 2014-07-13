var counter = 0;
var titleid, descrid, fundsid;
function addTask(){
	if(counter == 0){
		var table = document.createElement('table');
		table.setAttribute("id", "tasktable");
		table.innerHTML = "<thead><tr><th>Sr. No.</th><th>Title</th><th>Description</th><th>Funds</th></tr></thead><tbody></tbody>"
		document.getElementById('tasklist').appendChild(table);
	}
	counter++;
	countid = counter
	titleid = "taskTitle" + counter; 
	descrid = "taskDescription" + counter;
	fundsid= "taskFund" + counter;
	var row = document.createElement('tr');
	row.setAttribute("id","row"+counter.toString());
	var string = "<td>"+counter+"<td><input type = 'text' id = " + titleid + " /></td><td><input type = 'text' " + descrid + " /></td><td><input type = 'text' " + fundsid + " /></td>"
	row.innerHTML = string;
	document.getElementById("count").value=countid;
	document.getElementsByTagName('tbody')[0].appendChild(row);
}

function removeTask(){
	if(counter > 1){
		var element = document.getElementById("row"+counter);
		element.parentNode.removeChild(element);
		counter--;
	}
	else if(counter == 1){
		var element = document.getElementById("tasktable");
		element.parentNode.removeChild(element);
		counter--;
	}
}
