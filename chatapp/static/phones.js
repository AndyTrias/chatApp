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

document.addEventListener("DOMContentLoaded", function () {
    let button = document.querySelector('.button');
    let buttonText = document.querySelector('.tick');

    const tickMark = "<svg width=\"58\" height=\"45\" viewBox=\"0 0 58 45\" xmlns=\"http://www.w3.org/2000/svg\"><path fill=\"#fff\" fill-rule=\"nonzero\" d=\"M19.11 44.64L.27 25.81l5.66-5.66 13.18 13.18L52.07.38l5.65 5.65\"/></svg>";

    buttonText.innerHTML = "Submit";

    button.addEventListener('click', function () {

        if (buttonText.innerHTML !== "Submit") {
            buttonText.innerHTML = "Submit";
        } else if (buttonText.innerHTML === "Submit") {
            buttonText.innerHTML = tickMark;
        }
        this.classList.toggle('button__circle');
    })
})