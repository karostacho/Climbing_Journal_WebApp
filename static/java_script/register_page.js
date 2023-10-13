const e_mail = document.getElementById("email");
const password = document.getElementById("password");
const repeat_password = document.getElementById("repeat_password");
email_regex = '[^@]+@[^@]+\.[^@]+'
password_regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'

function emailValidation() {
    if (!e_mail.value.match(email_regex)) {
        document.getElementById("invalidEmail").innerHTML = "Invalid e-mail";
        e_mail.style.border = "1px solid red";
        return false;
    } else {
        e_mail.style.border = "1px solid rgba(207, 208, 215, 1)";
        document.getElementById("invalidEmail").innerHTML = "";
        return true;
    }
    }

    function passwordValidation() {
    if (!password.value.match(password_regex)) {
        document.getElementById("invalidPassword").innerHTML =
        "Password must be at least 8 characters and must contain at least: 1 lowercase letter, 1 uppercase letter, 1 numeric character, and 1 special character";
        password.style.border = "1px solid red";
        return false;
    } else {
        password.style.border = "1px solid rgba(207, 208, 215, 1)";
        document.getElementById("invalidPassword").innerHTML = "";
        return true;
    }
    }

    function passwordMatchValidation() {
    if (password.value !== repeat_password.value) {
        document.getElementById("passwordsMismatch").innerHTML =
        "Passwords don't match";
        repeat_password.style.border = "1px solid red";
        password.style.border = "1px solid red";
        return false;
    } else {
        password.style.border = "1px solid rgba(207, 208, 215, 1)";
        repeat_password.style.border = "1px solid rgba(207, 208, 215, 1)";
        document.getElementById("passwordsMismatch").innerHTML = "";
        return true;
    }
    }




function validationForm() {
    const isEmailValid = emailValidation();
    const isPasswordValid = passwordValidation();
    const isPasswordMatchValid = passwordMatchValidation();

    if (isEmailValid && isPasswordValid && isPasswordMatchValid){
        return true
    }
    else {
        return false
    }
    }


   
 