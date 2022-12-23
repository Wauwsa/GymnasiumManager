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
    let states_of_button = [] // list of indexes of buttons that are activated
    let states_string = localStorage.getItem(window.location.pathname.toString()) // get current list of buttons (url bound)
    if (states_string) { // if there are already activated buttons, turn that into a list
        states_of_button = states_string.split(',')
    }
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
            let index = states_of_button.indexOf(all_buttons.indexOf(ele).toString()) // get index of the activated buttons index
            if (index !== -1) {
                states_of_button.splice(index, 1); // delete that from the list
            }
            content.style.maxHeight = null;
            await sleep(100)
            ele.classList.add('bottom-collapsible')  // adds the roundness
        } else {
            states_of_button.push(all_buttons.indexOf(ele).toString()) // add index of activated button to the list
            ele.classList.remove('bottom-collapsible') // removes roundness (content roundness always there)
            await sleep(100)
            content.style.maxHeight = content.scrollHeight + "px";
        }
    } else {
        if (content.style.maxHeight) {
            let index = states_of_button.indexOf(all_buttons.indexOf(ele).toString())
            if (index !== -1) {
                states_of_button.splice(index, 1);
            }
            content.style.maxHeight = null;
        } else {
            states_of_button.push(all_buttons.indexOf(ele).toString())
            content.style.maxHeight = content.scrollHeight + "px";
        }
    }
    localStorage.setItem(window.location.pathname, states_of_button.toString()) // save states of button in local storage under key of url
}

function change_color() { // change color depending on grade
    let ele = Array.from(document.getElementsByClassName("noten-avg")) // div needs class "noten-avg"
    for (let x in ele) {
        let current_element = ele[x]
        let i = current_element.innerText.toString().replace(/[()]/g, "") // replaces () in inner text
        if (i >= 5.5) {
            ele[x].style.color = "rgb(8,255,0)"
        } else if (i >= 5) {
            ele[x].style.color = "rgb(162,255,0)"
        } else if (i >= 4) {
            ele[x].style.color = "rgb(255, 204, 0)"
        } else if (i >= 4) {
            ele[x].style.color = "rgb(236,117,42)"
        } else if (i >= 3) {
            ele[x].style.color = "rgb(255, 0, 0)"
        } else if (i < 3) {
            ele[x].style.color = "rgb(166,0,0)"
        }
    }
}

function button_radius() {
    let ele = Array.from(document.getElementsByClassName('collapsible')) // get all elements that are collapsible
    if (ele.length > 0) {
        const content = ele[ele.length-1].nextElementSibling // get the content for last button
        content.classList.add('content-bottom-collapsible')
    }
}

function button_states() {
    let elements = Array.from(document.getElementsByClassName('collapsible')) // get all buttons
    elements.forEach(function (element, index) { // foreach loop with element and index of list
        let states_string = localStorage.getItem(window.location.pathname.toString()) // get the states of button in current url
        if ((states_string) || (states_string.length <= 0)) { // check if there are any saved states
            let states = states_string.split(',') // if so, turn it into list, seperated by the "," in the string
            if (states.includes(index.toString())) { // if the index of current button is in the list of activated buttons
                const content = element.nextElementSibling;
                content.classList.add('content-no-animation') // add a no animation class, so animation doesn't get replayed on refresh
                if (content.classList.contains('content-bottom-collapsible')) { // check if button is last button
                    element.classList.add('collapsible-no-animation') // add no animation class for rounded corners
                    element.classList.remove('bottom-collapsible') // remove rounded corners (button is activated)
                }
                element.classList.toggle("active"); // toggle class active
                content.style.maxHeight = content.scrollHeight + "px"; // show content of button
            }
        }
    })
}
