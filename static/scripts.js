$(document).ready(function() {
    // Check if home is loaded
    if($('#childLooper').length > 0) {
        var numberOfDivs = showChildrenLoop();
        //loopChildrenDivs(numberOfDivs);
    }

    // Add class active to the active link
    var url = window.location;
    $("ul.nav a").filter(function() {
        return this.href == url;
    }).parent().addClass("active");
});

function showChildrenLoop() {
    // Load 3 random pictures to an array, with information
    // Loop through the array
    // Add links to the pictures (1 - 2 - 3) so the user can switch back to a child
    // Easier to do this in Python, but how do I transfer the variables?

    // Create a new div
    // Add a link to it, to pic 1, 2 or 3 depending on which picture it's on

    hideChildrenDivs();
    $("#child_div_1").show();

    var i = 1;
    var left_counter = 540;
    $("#childLooper div").each(function() {
        var current = i;
        $("<div/>", {
            "class": "child_link",
            "style": "left: " + left_counter + "px;",
            text: i,
            click: function() {
                hideChildrenDivs();
                showChildrenDiv(current);
            }
        }).prependTo("#childLooper");
        i++;
        left_counter = left_counter + 30;
    });

    return i;
}

function hideChildrenDivs() {
    var i = 1;
    $("#childLooper div").each(function() {
        $("#child_div_" + i).hide();
        i++;
    });
}

function showChildrenDiv(divNumber) {
    $("#child_div_" + divNumber).fadeIn(400);
}

function loopChildrenDivs(numberOfDivs) {
    var i = 1;
    while (i <= numberOfDivs) {
        //alert(i);
        window.setInterval(function() {
            $("#child_div_" + i).fadeIn(800)
        }, 1000);
        i++;
    }
}