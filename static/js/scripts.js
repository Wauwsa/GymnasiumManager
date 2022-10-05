let password_show = false;
function show_password() {
    if(password_show){
        document.getElementById("password").setAttribute("type", "password");
        document.getElementById("eye").setAttribute("class", "bi bi-eye");
        password_show = false
    }
    else {
        document.getElementById("password").setAttribute("type", "text");
        document.getElementById("eye").setAttribute("class", "bi bi-eye-slash");
        password_show = true
    }
}
