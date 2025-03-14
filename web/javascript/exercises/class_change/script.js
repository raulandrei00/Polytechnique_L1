
function switch_circle (event) {
    // document.querySelector("div").classList.remove("square");
    document.querySelector("div").classList.add("circle");
}

function switch_square (event) {
    // document.querySelector("div").classList.add("square");
    document.querySelector("div").classList.remove("circle");
}


document.querySelector(".click_circle").addEventListener("click" , switch_circle);
document.querySelector(".click_square").addEventListener("click" , switch_square);