"use strict"

const radius = 50;  // Radius of the circle
let y = 0;          // height (/vertical) of the circle within the viewport
// let circleElement = document.querySelector('.circle');

let circleArr = [];

let leftPos = 0;
const follower = document.getElementById("follower");

document.addEventListener("mousemove", (e) => {
    const x = e.clientX;
    const y = e.clientY;

    // Use transform for better performance
    follower.style.transform = `translate(${x}px, ${y}px)`;
});

main();

function main() {
    document.addEventListener('click', createCircle);
    animationLoop();

    function animationLoop() {
        
        circleArr.forEach(circle => {
            let crt_top = parseFloat(circle.style.top);
            circle.style.top = `${crt_top+1}px`;
            if (crt_top > 1200) {
                circle.remove();
            }
        });


    
        requestAnimationFrame( animationLoop );
    }
}

function createCircle(event) {
    
    let new_circle = document.createElement("div");
    new_circle.setAttribute("class" , "circle")
    
    const x = event.clientX;
    y = event.clientY;
    leftPos = x;
    new_circle.style.top = `${y-radius}px`;
    new_circle.style.left = `${x-radius}px`;
    const body = document.querySelector("body")
    body.appendChild(new_circle);
    circleArr.push(new_circle);
}


  