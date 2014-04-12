$(document).ready(function() {
	if ($('#login').length > 0){
		$("#login").validationEngine('attach', {bindMethod:"live"});
	}
	if ($('#register').length > 0){
		$("#register").validationEngine('attach', {bindMethod:"live"});
	}
});