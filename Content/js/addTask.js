var counter = 0;
var titleid, descrid, fundsid;
function addTask(){
	if(counter == 0){
		var table = document.createElement('table');
		table.setAttribute("style", "padding: 2px");
		table.innerHTML = "<thead><tr><th>Sr. No.</th><th>Title</th><th>Description</th><th>Funds</th></tr></thead><tbody></tbody>"
		document.getElementById('tasklist').appendChild(table);
	}
	counter++;
	countid = counter
	titleid = "taskTitle" + counter; 
	descrid = "taskDescription" + counter;
	fundsid= "taskFund" + counter;
	var row = document.createElement('tr');
	var string = "<td>"+counter+"<td><input type = 'text' id = " + titleid + " /></td><td><input type = 'text' " + descrid + " /></td><td><input type = 'text' " + fundsid + " /></td>"
	row.innerHTML = string;
	document.getElementById("count").value=countid;
	document.getElementsByTagName('tbody')[0].appendChild(row);
}
