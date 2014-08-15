function selectById(picked_id){
	var selectBox = document.getElementById(picked_id);
	var outputBox = document.getElementById(picked_id + "_output");
	var output = outputBox.innerHTML;
	var input = selectBox.options[selectBox.selectedIndex].text;
	if(output.indexOf(input + "; ") == -1){
		output = output.concat(input);
		output = output.concat('; ');
		outputBox.innerHTML = output;
	}
}
