$(document).ready(function(){
	$( "#fileSelect" ).click(function() {
	  $('#fileElem').click();
	});

	$('#fileElem').change(function() {
		if (CheckFileName("fileElem") == true){
			$('#photo-change-form').submit();
		}
    });

    $( "#fileSelectCompany" ).click(function() {
      $('#fileElemCompany').click();
    });

    $('#fileElemCompany').change(function() {
        if (CheckFileName("fileElemCompany") == true){
            $('#photo-change-form-company').submit();
        }
    });


	$('#photo-change-form').ajaxForm({url: '/user/photo_upload/user', type: 'post',
        success: function(data){
            $('#profile-img').attr("src", data);
            $('#dropdown-profile').attr("src", data);
            $('#main-profile').attr("src", data);
    }});

    $('#photo-change-form-company').ajaxForm({url: '/user/photo_upload/company', type: 'post',
        success: function(data){
            $('#profile-img-company').attr("src", data);
    }});


	$("#change-settings").validationEngine('attach', {bindMethod:"live"});

    $("#company-settings").click(function() {
        $("#personal-settings-form").fadeOut();
        $("#company-settings-form").fadeIn(300);
        $("#personal-settings").removeClass("bold-text");
        $("#company-settings").addClass("bold-text");
    });

    $("#personal-settings").click(function() {
        $("#company-settings-form").fadeOut();
        $("#personal-settings-form").fadeIn();
        $("#company-settings").removeClass("bold-text");
        $("#personal-settings").addClass("bold-text");
    });
});

function CheckFileName(fileFieldName) {
    var fileName = document.getElementById(fileFieldName).value;
    var pieces = fileName.split(/[\s.]+/);
    var finalS = pieces[pieces.length-1].toUpperCase();
    if (fileName == "") {
        alert("Browse to upload a valid File with png extension");
        return false;
    }
    else if (finalS == "PNG" || finalS == "JPG" || finalS == "BMP" || finalS == "JPEG")
        return true;
    else {
        alert("File with " + pieces[pieces.length-1] + " is invalid. Upload a valid file with JPG, PNG, JPEG, or BMP extensions.");
        return false;
    }
    return true;
}