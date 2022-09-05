// <Code taken from : https://www.twilio.com/blog/international-phone-number-input-html-javascript
document.addEventListener("DOMContentLoaded", function (){
    let form = document.querySelector("form")
    let phoneInputField = document.querySelector("#phone");
    let phoneInput = window.intlTelInput(phoneInputField, {
        utilsScript:
            "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.15/js/utils.js",
    })

    form.addEventListener("submit", function(){
        form.querySelector("#phone").value = phoneInput.getNumber();
        form.submit();
    })

})