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
