// Update quantity on click
$('.update-cart').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})