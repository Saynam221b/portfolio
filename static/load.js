$(document).on('click', 'a[data-ajax-link]', function (event) {
    event.preventDefault();
  
    var url = $(this).attr('href');
    showLoadingOverlay(); // Show the loading overlay
  
    $.ajax({
      url: url,
      type: 'GET',
      success: function (response) {
        $('body').html(response); // Replace the content with the fetched content
        hideLoadingOverlay(); // Hide the loading overlay after the content is loaded
      },
      error: function (xhr, status, error) {
        console.error(error);
        hideLoadingOverlay(); // Hide the loading overlay on error
      }
    });
  });
  
  function showLoadingOverlay() {
    $('.wheel-and-hamster').show();
  }
  
  function hideLoadingOverlay() {
    $('.wheel-and-hamster').hide();
  }
  