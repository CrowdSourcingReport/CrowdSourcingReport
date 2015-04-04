function selectById(picked_id){
	var selectBox = document.getElementById(picked_id);
	var outputBox = document.getElementById(picked_id + "_output");
	var outputDiv = document.getElementById(picked_id + "_output_show");
	var output = outputBox.value;
	var input = selectBox.options[selectBox.selectedIndex].text;
	var search = input + "; "
	if(output.indexOf(search) == -1){
		output = output + search;
		outputBox.value = output;
		outputDiv.innerHTML = output;
	}
}

function clearById(picked_id){
	document.getElementById(picked_id + "_output").value = "";
	document.getElementById(picked_id + "_output_show").innerHTML = "";
}
