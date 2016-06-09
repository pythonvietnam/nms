//Back to Top
jQuery(document).ready(function($) {
    $(function() {
      var headerHeight = $('#header').height();
      $('a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({ scrollTop: target.offset().top - headerHeight }, 600);
            return false;
          }
        }
      });
    });
});

        
//Contact Form
function validate_email(email) {
    var reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var address = email;
    if (reg.test(address) == false) {
        return false;
    }
}

function checkform() {

    var i_email = $("input#email").val();

    var errors = "";
        
    if (i_email.length > 2 && i_email.length < 255 && validate_email(i_email) == false)
        errors = errors + "Email is not valid<br/>";

    if (i_email.length < 3)
        errors = errors + "Email field is too short or empty<br/>";

    if (i_email.length > 254)
        errors = errors + "Email field is too long<br/>";

    if (errors != "") {
        $("form #success").slideUp("fast");
        $("form #error").html(errors).slideDown("fast");
       
        var destination = $('#home').offset().top - 70;
        $("html:not(:animated),body:not(:animated)").animate({
            scrollTop: destination
        }, 200);

       return false;
    } else {
        console.log("Come here");

        $.post('/', $("form#easy").serialize(), function (data) {
            // $("#home").reset();

            if (data == "Email sent") {
                $("form #error").hide();
                $("form #success").slideDown("fast");

                var destination = $('#home').offset().top - 70;
                $("html:not(:animated),body:not(:animated)").animate({
                    scrollTop: destination
                }, 200);
            } else {
                $("form #error").html(data).slideDown("fast");
                var destination = $('#home').offset().top - 70;
                $("html:not(:animated),body:not(:animated)").animate({
                    scrollTop: destination
                }, 200);
            }
        });
        return false;
    }
}