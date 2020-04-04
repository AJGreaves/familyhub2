/* variables */
underline = $('#underline-nav-container hr');

/**
 * Detects which url is currently active and displays the underline
 * for the correct navigation link.
 */
function setNavUnderline() {
    url = window.location.href;

    if (url.includes('listings/events')) {
        underline.css('margin-left', '20%').css('display', 'block');
    } else if (url.includes('listings/educational')) {
        underline.css('margin-left', '40%').css('display', 'block');
    } else if (url.includes('listings/clubs')) {
        underline.css('margin-left', '60%').css('display', 'block');
    } else if (url.includes('listings/parties')) {
        underline.css('margin-left', '80%').css('display', 'block');
    } else {
        underline.css('margin-left', '0').css('display', 'block');
    }
}

/**
 * Moves underline on navbar underneath the link hovered over
 */
$('#underline-nav-container a').mouseenter(function () {
    switch (this.id) {
        case 'home-link':
            underline.css('margin-left', '0');
            break;
        case 'events-link':
            underline.css('margin-left', '20%');
            break;
        case 'educational-link':
            underline.css('margin-left', '40%');
            break;
        case 'clubs-link':
            underline.css('margin-left', '60%');
            break;
        case 'parties-link':
            underline.css('margin-left', '80%');
            break;
    }
})

/**
 * Returns underline to under current page link when mouse no longer
 * hovering over other nav item.
 */
$('#underline-nav-container a').mouseleave(function () {
    setNavUnderline();
})

/**
 * Set up page
 */
setNavUnderline()