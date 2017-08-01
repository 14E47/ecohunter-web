$(document).ready(function() {

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
    })
});


$(document).ready(
    function() {
        $('[data-filter="blog"]').click()
    }
);


$('.view-more').click(function(e) {
    e.preventDefault();
    $(this).prev('p').slideToggle();
    $(this).html('close');
});


$(document).ready(function() {
    $('#selectId').change(function() {
        var selectVal = $("#selectId option:selected").val();
        alert(selectVal);
        $('form').attr('action', selectVal);
    });

});

$(document).ready(function() {
    $('#MselectId').change(function() {
        var selectVal = $("#MselectId option:selected").val();
        alert(selectVal);
        $('form').attr('action', selectVal);
    });

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

