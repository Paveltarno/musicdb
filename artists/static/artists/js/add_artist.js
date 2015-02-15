$(function(){
  var frm = $('#create-artist-form');
  frm.submit(function (event) {
    event.preventDefault();
    $("#create-artist-message").html("Searching...");
    $.ajax({
      type: frm.attr('method'),
      url: frm.attr('action'),
      data: frm.serialize(),
      success: function (data) {
          $("#create-artist-message").html(data.message);
      },
      error: function(data) {
          $("#create-artist-message").html("Server error. Try again.");
      }
  });
  return false;
  });
});