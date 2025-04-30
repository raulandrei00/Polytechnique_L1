"use strict"

const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');
ctx.canvas.width = window.innerWidth;
ctx.canvas.height = window.innerHeight;


ctx.strokeStyle = 'red';
ctx.lineWidth = 2;
let drawing = false;

let lastX = 0;
let lastY = 0;

document.getElementById('backgroundColorPicker').addEventListener('input', (e) => {
    canvas.style.backgroundColor = e.target.value;
});

// Change pen color
document.getElementById('penColorPicker').addEventListener('input', (e) => {
    ctx.strokeStyle = e.target.value;
});

document.getElementById('penWidthSlider').addEventListener('input', (e) => {
    ctx.lineWidth = e.target.value;
});

document.getElementById('clearCanvasButton').addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = canvas.style.backgroundColor || 'white'; // Set default background color
    ctx.fillRect(0, 0, canvas.width, canvas.height); // Fill the canvas with the background color
}
);

canvas.addEventListener('mousedown', (e) => {
    if (e.button === 0) { // Check if the left mouse button is clicked
        drawing = true;
        lastX = e.offsetX;
        lastY = e.offsetY;

        ctx.beginPath();
        ctx.arc(lastX, lastY, 1, 0, Math.PI * 2); // Draw a small circle with radius 1
        ctx.fillStyle = ctx.strokeStyle; // Use the same color as the stroke
        ctx.fill();
    }
});

canvas.addEventListener('mouseup', () => {
    drawing = false;
});

canvas.addEventListener('mousemove', (e) => {
    if (drawing) {
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
        lastX = e.offsetX;
        lastY = e.offsetY;
    }
}
);

