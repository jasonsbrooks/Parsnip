$(document).ready(function(){
	console.log("got here");
	$( "#fileSelect" ).click(function() {
	  $('#fileElem').click();
	});

	$('#fileElem').change(function() {
		if (CheckFileName() == true){
			$('#photo-change-form').submit();
		}
    });

	$('#photo-change-form').ajaxForm({url: '/user/photo_upload/', type: 'post',
        success: function(data){
            $('#profile-img').attr("src", data);
            $('#dropdown-profile').attr("src", data);
            $('#main-profile').attr("src", data);
    }});

	$("#change-settings").validationEngine('attach', {bindMethod:"live"});
});

function CheckFileName() {
    var fileName = document.getElementById("fileElem").value;
    var pieces = fileName.split(/[\s.]+/);
    var finalS = pieces[pieces.length-1].toUpperCase();
    if (fileName == "") {
        alert("Browse to upload a valid File with png extension");
        return false;
    }
    else if (finalS == "PNG" || finalS == "JPG" || finalS == "BMP" || finalS == "JPEG" || finalS == "TIF" || finalS == "TIFF" || finalS == "GIT")
        return true;
    else {
        alert("File with " + pieces[pieces.length-1] + " is invalid. Upload a valid file with JPG, PNG, BMP, JPEG, TIF, TIFF, GIF or BMP extensions.");
        return false;
    }
    return true;
}