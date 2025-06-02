

function event_function (event) {
    const response = document.createElement("p");
    if (event.target.className == "red") {
        response.textContent += "red";
    }
    else {
        response.textContent += "yellow";
    }
    document.querySelector("#add_text").appendChild(response);

}

// console.log(document.querySelector("div"))

document.querySelector(".red").addEventListener("click" , event_function);
document.querySelector(".yellow").addEventListener("click" , event_function);