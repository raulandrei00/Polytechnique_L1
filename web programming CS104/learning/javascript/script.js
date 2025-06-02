"use strict;"

const element = document.querySelector(".myElement")

element.textContent = "hello there\n"

for (let k = 0; k < 10; k++) {
    // console.log(k + 1);
    element.textContent += "hello there\n";
}

