$('#nav-login-tab').click(function () {
    $('.container').addClass('login-slide').removeClass('register-slide');
});

$('#nav-register-tab').click(function () {
    $('.container').addClass('register-slide').removeClass('login-slide');
});

$('#nav-home-tab').click(function () {
    $('.container').removeClass('register-slide').removeClass('login-slide');
});