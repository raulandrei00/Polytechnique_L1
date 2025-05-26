"use strict";

const GROW_MARGIN = 10; // px from bottom edge to trigger grow
const GROW_AMOUNT = 500; // px to grow each time

const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const container = document.getElementById('canvas-container');
const colorPicker = document.getElementById('color');
const sizeInput = document.getElementById('size');
const clearButton = document.getElementById('clear');
const container = document.getElementById('canvas-container');

let drawing = false;
let brushColor = colorPicker.value;
let brushSize = sizeInput.value;

colorPicker.addEventListener('input', (e) => brushColor = e.target.value);
sizeInput.addEventListener('input', (e) => brushSize = e.target.value);
clearButton.addEventListener('click', () => ctx.clearRect(0, 0, canvas.width, canvas.height));

// Dynamic canvas growth
const GROW_MARGIN = 1;
const GROW_AMOUNT = 10;

function growCanvasIfNeeded() {
    if (container.scrollTop + container.clientHeight >= container.scrollHeight - GROW_MARGIN) {
        const oldHeight = canvas.height;
        // Save current content
        const temp = document.createElement('canvas');
        temp.width = canvas.width;
        temp.height = canvas.height;
        temp.getContext('2d').drawImage(canvas, 0, 0);

        // Resize and restore
        canvas.height += GROW_AMOUNT;
        ctx.drawImage(temp, 0, 0);

        // Keep user just above the trigger zone
        container.scrollTop = container.scrollHeight - container.clientHeight - 2 * GROW_MARGIN;
    }
}
container.addEventListener('scroll', growCanvasIfNeeded);

// Drawing logic that accounts for scroll
let lastX = 0;
let lastY = 0;

canvas.addEventListener('mousedown', (e) => {
    drawing = true;
    lastX = e.offsetX;
    lastY = e.offsetY;
    ctx.beginPath();
    ctx.arc(lastX, lastY, brushSize / 2, 0, 2 * Math.PI);
    ctx.fillStyle = brushColor;
    ctx.fill();
});

canvas.addEventListener('mousemove', (e) => {
    if (!drawing) return;
    ctx.strokeStyle = brushColor;
    ctx.lineWidth = brushSize;
    ctx.lineCap = 'round';

    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();

    lastX = e.offsetX;
    lastY = e.offsetY;
});

canvas.addEventListener('mouseup', () => drawing = false);
canvas.addEventListener('mouseleave', () => drawing = false);

// Save the canvas as an image
document.getElementById('save').addEventListener('click', () => {
    if (!localStorage.getItem('currentUser')) {
      alert("No user is currently logged in. Please log in first.");
      return;
    }
    else userKey = `savedImages_${localStorage.getItem('currentUser')}`;
    // console.log("Saving canvas to localStorage with key:", userKey);
    const imgSrc = canvas.toDataURL('image/png');
    let saved = JSON.parse(localStorage.getItem("savedImages") || "[]");
    saved.push(imgSrc);
    localStorage.setItem("savedImages", JSON.stringify(saved));
    alert("Image saved in browser!");
});

// Load image if needed (your existing logic)
window.addEventListener('DOMContentLoaded', () => {
    const openImage = localStorage.getItem('openImage');
    if (openImage) {
        const img = new Image();
        img.onload = function() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        };
        img.src = openImage;
        localStorage.removeItem('openImage');
    }
});

