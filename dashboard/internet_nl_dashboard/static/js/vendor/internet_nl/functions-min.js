function HideJSLess() {
    var jsless = $(".jsless");
    if (jsless.length) {
        jsless.each(function () {
            $(this).addClass("hidethis").attr("aria-hidden", true);
        });
    }
}

$(document).ready(function () {
    if (document.addEventListener) {
        var theHeader = document.querySelector("header");
        var fixedHeaderbody = document.querySelector("body");
        fixedHeaderbody.classList.add("body-with-semifixed-header");
        var fixedHeader = new Headroom(theHeader, {
            "offset": 205,
            "tolerance": 5,
            "classes": {"initial": "header-js-animated", "pinned": "header-pinned", "unpinned": "header-unpinned"}
        });
        fixedHeader.init();
    }
});
