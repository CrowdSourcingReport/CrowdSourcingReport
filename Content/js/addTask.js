var counter = 0, no = 0;
var titleid, descrid, fundsid;
function addTask(){
	if(counter == 0){
		var table = document.createElement('table');
		table.setAttribute("id", "tasktable");
		table.setAttribute("class", "table table-striped table-condensed");
		table.innerHTML = "<thead><tr><th style='padding:5px; text-align:center;'>Sr. No.</th><th style='padding:5px; text-align:center;'>Title</th><th style='padding:5px; text-align:center;'>Description</th><th style='padding:5px; text-align:center;'>Funds (in &#8377;)</th><th style='padding:5px; text-align:center;'>Remove</th></tr></thead><tbody></tbody>"
		document.getElementById('Tasklist').appendChild(table);
	}
	counter++;
	titleid = "taskTitle" + no; 
	descrid = "taskDescription" + no;
	fundsid= "taskFund" + no;
	var row = document.createElement('tr');
	row.setAttribute("id","row"+no.toString());
	row.setAttribute("class","text-center");
	var string = "<td class='srno' style='padding:5px; vertical-align:middle;'>"+(no+1).toString()+"</td><td style='padding:5px; vertical-align:middle;'><input type = 'text' form='projectRegForm' class='form-control title' name = " + titleid + " /></td><td style='padding:5px;'><textarea form='projectRegForm' class='form-control descr' cols='80' rows='1' name =" + descrid + " ></textarea></td><td style='padding:5px; vertical-align:middle;'><input type = 'text' form='projectRegForm' class='form-control fund' name =" + fundsid + " /></td><td style='padding:5px; text-align:center; vertical-align:middle;'><a class='btn btn-primary form-control' href='#' id=" + counter + " onclick = 'removeTask(this.id)'>-</a></td>"
	row.innerHTML = string;
	document.getElementById("count").value=no;
	document.getElementsByTagName('tbody')[0].appendChild(row);
	no++;
}

function removeTask(count){
	if(document.getElementsByClassName('srno').length > 1){
		var element = document.getElementById(count).parentNode.parentNode;
		element.parentNode.removeChild(element);
		var srno = document.getElementsByClassName('srno');
		var title = document.getElementsByClassName('title');
		var fund = document.getElementsByClassName('fund');
		var descr = document.getElementsByClassName('descr');
		for(var i=0; i<srno.length; i++){
			srno[i].innerHTML = (i+1).toString();
			title[i].name = "taskTitle" + i.toString();
			fund[i].name = "taskFund" + i.toString();
			descr[i].name = "taskDescription" + i.toString();
		}
		no--;

	}
	else if(document.getElementsByClassName('srno').length == 1){
		var element = document.getElementById("tasktable");
		element.parentNode.removeChild(element);
		counter=0;
		no=0;
	}
}

addTask();
