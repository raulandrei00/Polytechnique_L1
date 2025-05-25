"use strict";

const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const colorPicker = document.getElementById('color');
const sizeInput = document.getElementById('size');
const clearButton = document.getElementById('clear');

let drawing = false;
let brushColor = colorPicker.value;
let brushSize = sizeInput.value;

// canvas.addEventListener('mousedown', () => drawing = true);
canvas.addEventListener('mouseup', () => drawing = false);
canvas.addEventListener('mousemove', draw);

colorPicker.addEventListener('input', (e) => brushColor = e.target.value);
sizeInput.addEventListener('input', (e) => brushSize = e.target.value);
clearButton.addEventListener('click', () => ctx.clearRect(0, 0, canvas.width, canvas.height));
userKey = `savedImages_${localStorage.getItem('currentUser')}`;
// Save the canvas as an image
document.getElementById('save').addEventListener('click', () => {
    const imgSrc = canvas.toDataURL('image/png');
    const canvasData = {
        img: imgSrc,
        width: canvas.width,
        height: canvas.height
    };
    let saved = JSON.parse(localStorage.getItem(userKey) || "[]");
    saved.push(canvasData);
    localStorage.setItem(userKey, JSON.stringify(saved));
    alert("Image and dimensions saved in browser!");
});

window.addEventListener('DOMContentLoaded', () => {
  const openImage = localStorage.getItem('openImage');
  if (openImage) {
    // openImage is now a JSON string with img, width, height
    const data = JSON.parse(openImage);
    const img = new Image();
    img.onload = function() {
      canvas.width = data.width;
      canvas.height = data.height;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    };
    img.src = data.img;
    localStorage.removeItem('openImage');
  }
});

let lastX = 0;
let lastY = 0;

canvas.addEventListener('mousedown', (e) => {
    drawing = true;
    lastX = e.offsetX;
    lastY = e.offsetY;
});

// TODO: canvas does not draw points
function draw(e) {
    if (!drawing) return;
    ctx.lineWidth = brushSize;
    ctx.lineCap = 'round';
    ctx.strokeStyle = brushColor;

    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();

    lastX = e.offsetX;
    lastY = e.offsetY;
}

// Dynamic canvas resizing
const GROW_MARGIN = 100; // px from edge to trigger grow
const GROW_AMOUNT = 1000; // px to grow each time

function growCanvasIfNeeded(e) {
    const container = document.getElementById('canvas-container');
    // Check scroll position
    if (container.scrollLeft + container.clientWidth >= canvas.width - GROW_MARGIN) {
        growCanvas(canvas.width + GROW_AMOUNT, canvas.height);
    }
    if (container.scrollTop + container.clientHeight >= canvas.height - GROW_MARGIN) {
        growCanvas(canvas.width, canvas.height + GROW_AMOUNT);
    }
}

function growCanvas(newWidth, newHeight) {
    // Save current content
    const temp = document.createElement('canvas');
    temp.width = canvas.width;
    temp.height = canvas.height;
    temp.getContext('2d').drawImage(canvas, 0, 0);

    // Resize and restore
    canvas.width = newWidth;
    canvas.height = newHeight;
    ctx.drawImage(temp, 0, 0);
}

// Attach scroll event
document.getElementById('canvas-container').addEventListener('scroll', growCanvasIfNeeded);


