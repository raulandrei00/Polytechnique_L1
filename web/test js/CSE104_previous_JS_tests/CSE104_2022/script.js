"use strict;"

const pixelsContainer = document.querySelector('#pixels');
const colorInput = document.querySelector('#colorInput')
const N = 12;

let currentColor = colorInput.value;
colorInput.addEventListener('input',setCurrentColor);

let boxes = [];
for(let kx=0; kx<N; ++kx) {
    for(let ky=0; ky<N; ++ky) {
        const box = document.createElement("div");
        box.classList.add('box');
        box.classList.add('selectable');
        pixelsContainer.appendChild(box);
        box.addEventListener('click', clickOnBox);
        boxes[kx+N*ky] = box;
    }
    pixelsContainer.appendChild(document.createElement("div"));
}

function setCurrentColor(event) {
    currentColor = colorInput.value;
}

function clickOnBox(event)
{
    const box = event.currentTarget;
    box.removeEventListener('click', clickOnBox);
    box.classList.remove('selectable');
    box.style.backgroundColor = currentColor;
}


// Animation

let continueAnimation = true;
idx = 0;
const animateButton = document.querySelector('#animateButton');
animateButton.addEventListener('click',startAnimation);

function animationLoop(event)
{
    for(let k=0; k<2; ++k){
        let r = Math.floor(Math.random()*256);
        let g = Math.floor(Math.random()*256);
        let b = Math.floor(Math.random()*256);
        idx = Math.floor(Math.random()*N*N);

        boxes[idx].style.backgroundColor = `rgb(${r},${g},${b})`;
        if(boxes[idx].classList.contains('selectable')===false) {
            boxes[idx].classList.add('selectable');
            boxes[idx].addEventListener('click', clickOnBox);
        }
    }

    if(continueAnimation){
        requestAnimationFrame(animationLoop);
    }
}

function startAnimation(event)
{
    continueAnimation = true;
    animateButton.removeEventListener('click', startAnimation);
    animateButton.addEventListener('click', stopAnimation);
    animateButton.value = "Stop Animation";

    animationLoop();
}
function stopAnimation(event)
{
    continueAnimation = false;
    animateButton.removeEventListener('click',stopAnimation);
    animateButton.addEventListener('click',startAnimation);
    animateButton.value = "Animate Random Colors!";
}