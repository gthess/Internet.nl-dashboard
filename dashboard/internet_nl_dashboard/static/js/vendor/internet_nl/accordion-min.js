$('.accordion').attr({role: 'tablist', multiselectable: 'true'});
$('.panel-content').attr('id', function (IDcount) {
    return 'panel-' + IDcount;
});
$('.panel-content').attr('aria-labelledby', function (IDcount) {
    return 'control-panel-' + IDcount;
});
$('.panel-content').attr('aria-hidden', 'true');
$('.accordion .panel-content').attr('role', 'tabpanel');
$('.panel-title').each(function (i) {
    $target = $(this).next('.panel-content')[0].id;
    $('a', this).attr('href', '#' + 'control-' + $target).attr('aria-controls', $target).attr('id', 'control-' + $target);
    var opentext = $('#panel-item-open').html();
    $('.pre-icon', this).text(opentext);
});
var hash = window.location.hash;
// quick fix to prevent messing up loading SPA pages.
if (hash != '' && hash.startsWith("control-panel")) {
    $(hash).attr('aria-expanded', true).addClass('active').parent().next('.panel-content').slideDown(200).attr('aria-hidden', 'false');
    setPanelItemFoldText($('.pre-icon', hash), 'close');
    refreshPanelButtonText($(hash), 'open');
}
$('.panel-title a').click(function () {
    if ($(this).attr('aria-expanded') == 'false') {
        $(this).attr('aria-expanded', true).addClass('active').parent().next('.panel-content').slideDown(200).attr('aria-hidden', 'false');
        setPanelItemFoldText($('.pre-icon', this), 'close');
        refreshPanelButtonText($(this), 'open');
        var stateObj = {foo: "bar"};
        window.history.pushState(stateObj, null, "#" + $(this).attr('id'));
    } else {
        $(this).attr('aria-expanded', false).removeClass('active').parent().next('.panel-content').slideUp(200).attr('aria-hidden', 'true');
        var stateObj = {foo: "bar"};
        history.pushState(stateObj, null, '#')
        setPanelItemFoldText($('.pre-icon', this), 'open');
        refreshPanelButtonText($(this), 'close');
    }
    return false;
});


/* This should be done in a callable function, but it wasn't. todo: make a pull request at internet.nl */
function accordinate(){
    $('.accordion').attr({role: 'tablist', multiselectable: 'true'});
    $('.panel-content').attr('id', function (IDcount) {
        return 'panel-' + IDcount;
    });
    $('.panel-content').attr('aria-labelledby', function (IDcount) {
        return 'control-panel-' + IDcount;
    });
    $('.panel-content').attr('aria-hidden', 'true');
    $('.accordion .panel-content').attr('role', 'tabpanel');
    $('.panel-title').each(function (i) {
        $target = $(this).next('.panel-content')[0].id;
        $('a', this).attr('href', '#' + 'control-' + $target).attr('aria-controls', $target).attr('id', 'control-' + $target);
        var opentext = $('#panel-item-open').html();
        $('.pre-icon', this).text(opentext);
    });
    var hash = window.location.hash;
    // quick fix to prevent messing up loading SPA pages.
    if (hash != '' && hash.startsWith("control-panel")) {
        $(hash).attr('aria-expanded', true).addClass('active').parent().next('.panel-content').slideDown(200).attr('aria-hidden', 'false');
        setPanelItemFoldText($('.pre-icon', hash), 'close');
        refreshPanelButtonText($(hash), 'open');
    }

    // reset onclicks, because adding on-clicks stack: each one will be called causing the panel to open and close multiple times
    // after calling accordinate multiple times.
    $('.panel-title a').off("click").click(function () {
        if ($(this).attr('aria-expanded') == 'false') {
            $(this).attr('aria-expanded', true).addClass('active').parent().next('.panel-content').slideDown(200).attr('aria-hidden', 'false');
            setPanelItemFoldText($('.pre-icon', this), 'close');
            refreshPanelButtonText($(this), 'open');
            var stateObj = {foo: "bar"};
            window.history.pushState(stateObj, null, "#" + $(this).attr('id'));
        } else {
            $(this).attr('aria-expanded', false).removeClass('active').parent().next('.panel-content').slideUp(200).attr('aria-hidden', 'true');
            var stateObj = {foo: "bar"};
            history.pushState(stateObj, null, '#')
            setPanelItemFoldText($('.pre-icon', this), 'open');
            refreshPanelButtonText($(this), 'close');
        }
        return false;
    });
}