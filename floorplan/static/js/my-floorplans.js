$(document).ready(function() {
	if ($('#new-floorplan').length > 0){
		$('#new-floorplan').validationEngine('attach', {bindMethod:'live'});
	}
});