$(document).ready(function() {

	$('#register').on('submit', function(e) {
		if (($("#choose-company").val() == '') && ($("#new-form-text").length < 1)){
			$("#choose-company").select2("enable", false);
			$('.sign-up-button').before(companyHTML).fadeIn();
			e.preventDefault();
			setTimeout(
			  function() 
			  {
			   	$('#register').validationEngine('hideAll');
			  }, 500);
			$(".time-picker").datetimepicker({datepicker:false,format: 'g:i A', formatTime: 'g:i A'});
		}
		$("#choose-company").select2("enable", true);
	});

	if ($('#login').length > 0){
		$('#login').validationEngine('attach', {bindMethod:'live'});
	}
	if ($('#register').length > 0){
		$("#register").validationEngine('attach', {bindMethod:"live"});
	}

	$("#choose-company").select2({placeholder: "Company (leave blank for new)", allowClear: true, width:'330px', height: '50px'});
});

var companyHTML = "<div id='new-form-text'><input name='companyname' type='text' class='validate[required,maxSize[40]] sign-up-input' placeholder='Company Name' autofocus required><input name='address1' type='text' class='validate[required,maxSize[40]] sign-up-input' placeholder='Address 1' required><input name='address2' type='text' class='validate[optional,maxSize[40]] sign-up-input' placeholder='Address2'><input name='city' type='text' class='validate[required,maxSize[40]] sign-up-input' placeholder='City' required><input name='state' type='text' class='validate[required,maxSize[40]] sign-up-input' placeholder='State' required><input name='zipcode' type='text' class='validate[required,maxSize[40]] sign-up-input' placeholder='Zipcode' required><input name='phone' type='text' class='validate[required,maxSize[40]] sign-up-input' placeholder='Telephone' required><input name='hoursmonday-start' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Monday Start' required><input name='hoursmonday-end' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Monday End' required><input name='hourstuesday-start' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Tuesday Start' required><input name='hourstuesday-end' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Tuesday End' required><input name='hourswednesday-start' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Wednesday Start' required><input name='hourswednesday-end' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Wednesday End' required><input name='hoursthursday-start' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Thursday Start' required><input name='hoursthursday-end' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Thursday End' required><input name='hoursfriday-start' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Friday Start' required><input name='hoursfriday-end' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Friday End' required><input name='hourssaturday-start' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Saturday Start' required><input name='hourssaturday-end' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Saturday End' required><input name='hourssunday-start' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Sunday Start' required><input name='hourssunday-end' type='text' class='validate[required,maxSize[40]] sign-up-input time-picker sign-up-input-half' placeholder='Sunday End' required></div>";