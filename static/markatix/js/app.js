$(document).ready(function() {
    var checkMod = function(){
    if($(window).width() < 769){    
            $('#mob').removeClass("padding-change-1").addClass("padding-change-2");
            $('#mob').removeClass("col-md-3").addClass("col-md-4");
            $('#place-1').removeClass("recom-place-1").addClass("recom-place-3");
            $('#place-2').removeClass("recom-place-2").addClass("recom-place-3");
            $('#place-1').find('.content-overlay-1').addClass("content-overlay-2");
            $('#place-2').find('.content-overlay-1').addClass("content-overlay-2");
            $('#place-1').find('.content-image-1').addClass("content-image-2");
            $('#place-2').find('.content-image-1').addClass("content-image-2");
        }
        else{
            $('#mob').removeClass("padding-change-2").addClass("padding-change-1");
            $('#mob').removeClass("col-md-4").addClass("col-md-3");
            $('#place-1').removeClass("recom-place-3").addClass("recom-place-1");
            $('#place-2').removeClass("recom-place-3").addClass("recom-place-2");
            $('#place-1').find('.content-overlay-1').removeClass("content-overlay-2");
            $('#place-2').find('.content-overlay-1').removeClass("content-overlay-2");
            $('#place-1').find('.content-image-1').removeClass("content-image-2");
            $('#place-2').find('.content-image-1').removeClass("content-image-2");
        }
    }
    $(window).resize(checkMod);
     // Call once on initial load
     checkMod ();
    
    var heightNav = $('.primary-nav').outerHeight();
    var heightHeader = $('#exp-header').outerHeight();
    var heightExpNav = $('#exp-nav').outerHeight();
    var totalTop = heightHeader + heightNav;
    var totalNewTop = totalTop + heightExpNav + 54;
     $('#exp-nav').affix({
        offset: {
          top: totalTop
        }
    });
    $(window).scroll(function() {
        if($('#exp-nav').affix().offset().top >= totalNewTop && $('#exp-nav').affix().offset().top > ( $("#exp-header").offset().top + heightHeader)){
            $('.hide-scroll').hide();
        }
        else{ 
            $('.hide-scroll').show();
        }
    });
    $('.smoothscroll').click(function(){
        $('.hide-scroll').hide();
    });

    $(".filter-button").click(function() {
        var value = $(this).attr('data-filter');

        if (value == "all") {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        } else {
            //            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
            //            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.' + value).hide('3000');
            $('.filter').filter('.' + value).show('3000');

        }
    });


    // if ($(".filter-button").removeClass("active")) {
    //     $(this).removeClass("active");
    // }
    // $(this).addClass("active");

    $('[data-filter=".blog"]').click();
    $(".tabs-try li p").on("click", function() {
        $(".tabs-try li").toggleClass("active", false)
        $(this).parent().toggleClass("active", true);

    });



    var clickEvent = false;
    $('#myCarousel').carousel({
        interval: 4000
    }).on('click', '.list-group li', function() {
        clickEvent = true;
        $('.list-group li').removeClass('active');
        $(this).addClass('active');
    }).on('slid.bs.carousel', function(e) {
        if (!clickEvent) {
            var count = $('.list-group').children().length - 1;
            var current = $('.list-group li.active');
            current.removeClass('active').next().addClass('active');
            var id = parseInt(current.data('slide-to'));
            if (count == id) {
                $('.list-group li').first().addClass('active');
            }
        }
        clickEvent = false;
    });


    $(window).load(function() {
        var boxheight = $('#myCarousel .carousel-inner').innerHeight();
        var itemlength = $('#myCarousel .item').length;
        var triggerheight = Math.round(boxheight / itemlength + 1);
        $('#myCarousel .list-group-item').outerHeight(triggerheight);
        $('a[href*="#"]')
    // Remove links that don't actually link to anything
    .not('[href="#"]')
    .not('[href="#0"]')
    .click(function(event) {
        // On-page links
        if (
        location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
        && 
        location.hostname == this.hostname
        ) {
        // Figure out element to scroll to
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        // Does a scroll target exist?
        if (target.length) {
            // Only prevent default if animation is actually gonna happen
            event.preventDefault();
            $('html, body').animate({
            scrollTop: target.offset().top - 154
            }, 700, function() {
            // Callback after animation
            // Must change focus!
            var $target = $(target);
            $target.focus();
            if ($target.is(":focus")) { // Checking if the target was focused
                return false;
            } else {
                $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
                $target.focus(); // Set focus again
            };
            });
        }
        }
    });
    });
    // Select all links with hashes
    
    $('[data-filter="blog"]').click();
     $('#selectId').change(function() {
        var selectVal = $("#selectId option:selected").val();
        alert(selectVal);
        $('form').attr('action', selectVal);
    });
     $('#MselectId').change(function() {
        var selectVal = $("#MselectId option:selected").val();
        alert(selectVal);
        $('form').attr('action', selectVal);
    });
});



$('.view-more').click(function(e) {
    e.preventDefault();
    $(this).prev('p').slideToggle();
    $(this).html('close');
});


var nowTemp = new Date();
var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
 
var checkin = $('#dpd1').datepicker({
  onRender: function(date) {
    return date.valueOf() < now.valueOf() ? 'disabled' : '';
  }
}).on('changeDate', function(ev) {
  if (ev.date.valueOf() > checkout.date.valueOf()) {
    var newDate = new Date(ev.date)
    newDate.setDate(newDate.getDate() + 1);
    checkout.setValue(newDate);
  }
  checkin.hide();
  $('#dpd2')[0].focus();
}).data('datepicker');
var checkout = $('#dpd2').datepicker({
  onRender: function(date) {
    return date.valueOf() <= checkin.date.valueOf() ? 'disabled' : '';
  }
}).on('changeDate', function(ev) {
  checkout.hide();
}).data('datepicker');


