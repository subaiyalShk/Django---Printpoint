/*!
    * Start Bootstrap - Grayscale v6.0.2 (https://startbootstrap.com/themes/grayscale)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
    */
    (function ($) {
    "use strict"; // Start of use strict

        $('form').submit(function(e){
            e.preventDefault()
            $.ajax({
                url: 'http://localhost:8000/contact',
                method: 'post',
                data: $(this).serialize(),
                success: function(serverResponse){
                $('form').html(serverResponse)
                console.log("Received this from server: ", serverResponse)
                console.log("I should probably put that in the DOM...")
                }
            })
        })

        // $(window).on('scroll', function() {
        //     // if how it works is in view
        //     // if scrollTop 
        //     var y = $(window).scrollTop();
        //     if(y>$('#about').height()+$('#product-section').height()){
        //         $('html, body').stop().animate({
        //             'scrollTop': $('#inquire').offset().top
        //         }, 800)
        //     }
        // });

        $('#navbarResponsive .nav-link').click(function(e){
            e.preventDefault()
            $.ajax({
            url: $(this).attr('href'),
            method: 'get',
            success: function(serverResponse){
                $('#block-content').html(serverResponse)
                console.log("Received this from server: ", serverResponse)
                console.log("I should probably put that in the DOM...")
            }
            })
        })
        

        // Smooth scrolling using jQuery easing
        $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
            if (
                location.pathname.replace(/^\//, "") ==
                    this.pathname.replace(/^\//, "") &&
                location.hostname == this.hostname
            ) {
                var target = $(this.hash);
                target = target.length
                    ? target
                    : $("[name=" + this.hash.slice(1) + "]");
                if (target.length) {
                    $("html, body").animate(
                        {
                            scrollTop: target.offset().top - 70,
                        },
                        1000,
                        "easeInOutExpo"
                    );
                    return false;
                }
            }
        });

        // Closes responsive menu when a scroll trigger link is clicked
        $(".js-scroll-trigger").click(function () {
            $(".navbar-collapse").collapse("hide");
        });

        // Activate scrollspy to add active class to navbar items on scroll
        $("body").scrollspy({
            target: "#mainNav",
            offset: 100,
        });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})(jQuery); // End of use strict


// Tabs
function onTabClick(event) {
    if(event.target.id=="nav-specification-tab"){
        
        document.getElementById("nav-description-tab").className.replace('active', '');
        document.getElementById("nav-description").className.replace('show active', '');
    }else if(event.target.id=="nav-description-tab"){
        
        document.getElementById("nav-specification-tab").className.replace('active', '');
        document.getElementById("nav-specification").className.replace('show active', '');
    }
    
    // event.target.className += ' active';
    // document.getElementById(event.target.id.replace("-tab","")).className += 'show active';
}
const element1 = document.getElementById("nav-specification-tab");
element1.addEventListener('click', onTabClick);
const element2 = document.getElementById("nav-description-tab");
element2.addEventListener('click', onTabClick);


