function validationForm(){
    const e_mail = document.getElementById("email")
    const password = document.getElementById("password")
    const repeat_password = document.getElementById("repeat_password")
    email_regex = '[^@]+@[^@]+\.[^@]+'
    password_regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'

    if (!e_mail.value.match(email_regex)){
        alert("Invalid e-mail")
        return false
    }

    if (!password.value.match(password_regex)){
        alert("Password must be at least 8 character and must contain at least: 1 lower case letter, 1 upper case letter, 1 numeric character and 1 special character")
        return false
    }

    if (password.value !== repeat_password.value){
        alert("Passwords don't match")
        return false
    }
    else{
        return true
    }
}