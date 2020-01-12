
$(document).ready(function () {actions();});
window.onscroll = function () {myFunction()};

function actions() {
    // $('#logo_img').on('click', menu_animate);
    $('[name = "VacancyFilter"]').map(function () {
        $(this).on('change', chenge_url);
    })
}

function chenge_url() {
    let url = new URL(document.location.href);
    url.searchParams.set("filter", 'true');
    history.pushState(null, null, url.search);

    if ($(this).prop('checked')) {
        let url = new URL(document.location.href);
        url.searchParams.set(this.value, 'true');
        history.pushState(null, null, url.search);

    } else {
        let url = new URL(document.location.href);
        url.searchParams.delete(this.value);
        rt = url.search;
        history.replaceState(null, null, rt);
    }
    filter();
}

function filter() {
    let index = 0;
    $('[name = "job"]').map(function () {
        $(this).attr('style', 'display: none !important');

        let elem = this;
        let tags = $(this).attr('tags');
        tags = tags.split(',');
        let url = new URL(document.location.href);
        let url_tags = url.search;
        url_tags = url_tags.replace(/=true/g, "");
        url_tags = url_tags.split('&');
        url_tags.forEach(function (item, i, arr) {
            if (tags.includes(item)) {
                index += 1;
                $(this).attr('style', 'display: block !important');
                $(elem).show();
            }});

    });

    let url = new URL(document.location.href);
    let url_tags = url.search;
    url_tags = url_tags.replace(/=true/g, "");
    url_tags = url_tags.split('&');
    if (url_tags.length <= 1) {
        $('[name = "job"]').map(function () {
            $(this).show();});
        index = 1;}

    if (index > 0) {
         $("#menu_tags").attr('style', 'display: block ');
        $("#box-item-message").hide();}

    else {

        $("#menu_tags").attr('style', 'display: none !important');
        $("#box-item-message").show();}}

// $('#formUserDataSubmit').on('click', function (event) {
//     var fd = new FormData(document.querySelector("#formUserData"));
//     $.ajax({
//         url: "/success",
//         type: "POST",
//         data: fd,
//         processData: false,
//         contentType: false});});

function myFunction() {
    let header = document.getElementById("myHeader");

    let sticky = header.offsetTop;

    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}