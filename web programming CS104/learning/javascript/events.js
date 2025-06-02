
const title = document.querySelector("h1");

function click_action (event) {

    const new_element = document.createElement("p");
    new_element.textContent = "clicked title";

    document.querySelector(".container").appendChild(new_element);

}


title.addEventListener('click' , click_action);

