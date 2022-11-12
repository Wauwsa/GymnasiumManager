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

function sleep(milliseconds) {
      return new Promise(resolve => setTimeout(resolve, milliseconds));
   }

async function collapse_show_button(ele) {
    let all_buttons = Array.from(document.getElementsByClassName('collapsible'))
    ele.classList.toggle("active");
    const content = ele.nextElementSibling;
    if (content.classList.contains('content-no-animation')) {
        content.classList.remove('content-no-animation')
    }
    if (ele.classList.contains('collapsible-no-animation')) {
        ele.classList.remove('collapsible-no-animation')
    }
    if (content.classList.contains('content-bottom-collapsible')) { // checks if button is the one at bottom
        if (content.style.maxHeight) {
            localStorage.removeItem(all_buttons.indexOf(ele).toString())
            content.style.maxHeight = null;
            await sleep(100)
            ele.classList.add('bottom-collapsible')  // adds the roundnesse
        } else {
            localStorage.setItem(all_buttons.indexOf(ele).toString(), 'active')
            ele.classList.remove('bottom-collapsible') // removes roundness (content roundness always there)
            await sleep(100)
            content.style.maxHeight = content.scrollHeight + "px";
        }
    } else {
        if (content.style.maxHeight) {
            localStorage.removeItem(all_buttons.indexOf(ele).toString())
            content.style.maxHeight = null;
        } else {
            localStorage.setItem(all_buttons.indexOf(ele).toString(), 'active')
            content.style.maxHeight = content.scrollHeight + "px";
        }
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

function button_radius() {
    let ele = Array.from(document.getElementsByClassName('collapsible')) // get all elements that are collapsible
    const content = ele[ele.length-1].nextElementSibling // get the content for last button
    content.classList.add('content-bottom-collapsible')
}

function button_states() {
    let elements = Array.from(document.getElementsByClassName('collapsible'))
    elements.forEach(function (element, index) {
        let state = localStorage.getItem(index.toString())
        if (state === 'active') {
            const content = element.nextElementSibling;
            content.classList.add('content-no-animation')
            if (content.classList.contains('content-bottom-collapsible')) {
                    element.classList.add('collapsible-no-animation')
                    element.classList.remove('bottom-collapsible')
                }
            element.classList.toggle("active");
            content.style.maxHeight = content.scrollHeight + "px";
        }
    })
}