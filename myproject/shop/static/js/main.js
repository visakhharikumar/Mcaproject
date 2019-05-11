/*price range*/

 $('#sl2').slider();

	var RGBChange = function() {
	  $('#RGB').css('background', 'rgb('+r.getValue()+','+g.getValue()+','+b.getValue()+')')
	};	
		
/*scroll to top*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(document).ready(function(){
	// alert('hi');
	$(".shaddy").each(function(){
		
		$(this).on('click',function(){
		 alert('hi');
	       var  product_id = $(this).attr("product_id");
	       // var csrftoken = getCookie('csrftoken');
	       $.ajax({
		    url: '/cart/',
		    method: 'POST',
		    data: {
			    product_id: product_id
			},
		    success: function(data){
		      console.log('succes: '+ data);
		      alert('data.logged_in'+data.logged_in)
		      obj=JSON.parse(data);
              if(obj.logged_in){
		       window.location = '/cart'
		      }else{
		       	window.location = '/login'

		       }
		    }
		  });
	    });
	})

	$(".delete-item-btn").each(function(){
		// alert('hi');
		$(this).on('click',function(){
		// alert('hi');
	       var  cart_id = $(this).attr("cart_id");
	       // var csrftoken = getCookie('csrftoken');
	       $.ajax({
		    url: '/delete-cart/',
		    method: 'POST',
		    data: {
			    cart_id: cart_id
			},
		    success: function(data){
		      console.log('succes: '+ data);
		      window.location.reload()
		    }
		  });
	    });
	})

		
	$(function () {
		$.scrollUp({
	        scrollName: 'scrollUp', // Element ID
	        scrollDistance: 300, // Distance from top/bottom before showing element (px)
	        scrollFrom: 'top', // 'top' or 'bottom'
	        scrollSpeed: 300, // Speed back to top (ms)
	        easingType: 'linear', // Scroll to top easing (see http://easings.net/)
	        animation: 'fade', // Fade, slide, none
	        animationSpeed: 200, // Animation in speed (ms)
	        scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
					//scrollTarget: false, // Set a custom target element for scrolling to the top
	        scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
	        scrollTitle: false, // Set a custom <a> title if required.
	        scrollImg: false, // Set true to use image
	        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	        zIndex: 2147483647 // Z-Index for the overlay
		});
	});
});
