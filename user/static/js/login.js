$(document).ready(function() {
	if ($('#login').length > 0){
		$("#login").validationEngine('attach', {bindMethod:"live"});
	}
	if ($('#register').length > 0){
		$("#register").validationEngine('attach', {bindMethod:"live"});
	}

	$("#choose-company").select2({placeholder: "Company (leave blank for new)", allowClear: true, width:'280px', height: '50px'});
});