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

function collapse_show_button(ele) {
    ele.classList.toggle("active");
    const content = ele.nextElementSibling;
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}

function change_color() { // change color depending on grade
    let ele = Array.from(document.getElementsByClassName("noten-avg")) // div needs class "noten-avg"
    for (let x in ele) {
        let current_element = ele[x]
        let i = current_element.innerText.toString().replace(/[()]/g,"") // replaces () in inner text
        if (i >= 5) {
            ele[x].style.color = "rgb(51, 204, 51)"
        } else if (i >= 4) {
            ele[x].style.color = "rgb(255, 204, 0)"
        } else if (i < 4) {
            ele[x].style.color = "rgb(255, 0, 0)"
        }
    }
}