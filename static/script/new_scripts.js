$(document).ready(function () {actions();});

function actions() {
    // $('#logo_img').on('click', menu_animate);
    $('[name = "VacancyFilter"]').map(function () {
        $(this).on('change', chenge_url);
    })
}