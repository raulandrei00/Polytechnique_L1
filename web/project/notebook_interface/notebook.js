"use strict";

const GROW_MARGIN = 10; // px from bottom edge to trigger grow
const GROW_AMOUNT = 500; // px to grow each time

const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const container = document.getElementById('canvas-container');
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
let userKey = null;
// Save the canvas as an image
document.getElementById('save').addEventListener('click', () => {
    if (!localStorage.getItem('currentUser')) {
      alert("No user is currently logged in. Please log in first.");
      return;
    }
    else userKey = `savedImages_${localStorage.getItem('currentUser')}`;
    // console.log("Saving canvas to localStorage with key:", userKey);
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

function growCanvasIfNeeded() {
    // Only grow if user is near the bottom of the scrollable area
    if (container.scrollTop + container.clientHeight >= container.scrollHeight - GROW_MARGIN) {
        const oldHeight = canvas.height;
        growCanvas(canvas.width, canvas.height + GROW_AMOUNT);
        // Scroll up by GROW_MARGIN to avoid continuous growth
        container.scrollTop = container.scrollHeight - container.clientHeight - GROW_MARGIN - 10;
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

    // Also grow the container if needed (optional, usually not needed if container is fixed height)
    // container.style.height = (parseInt(container.style.height || container.clientHeight) + GROW_AMOUNT) + "px";
}

// Attach scroll event
container.addEventListener('scroll', growCanvasIfNeeded);

document.getElementById('userCircle').onclick = function() {
  window.location.href = '../dashboard/dashboard.html';
};

document.getElementById("userCircle").onmouseover = function() {
  const tooltip = document.createElement('div');
  tooltip.textContent = "click to go to dashboard";
  tooltip.style.position = 'absolute';
  tooltip.style.background = '#333';
  tooltip.style.color = '#fff';
  tooltip.style.padding = '4px 8px';
  tooltip.style.borderRadius = '4px';
  tooltip.style.fontSize = '12px';
  tooltip.style.pointerEvents = 'none';
  tooltip.style.zIndex = 1000;

  document.body.appendChild(tooltip);

  const userCircle = document.getElementById("userCircle");
  const rect = userCircle.getBoundingClientRect();
  tooltip.style.left = (rect.left + window.scrollX + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
  tooltip.style.top = (rect.top + window.scrollY + 30) + 'px';

  userCircle.onmouseleave = function() {
    if (tooltip.parentNode) tooltip.parentNode.removeChild(tooltip);
    userCircle.onmouseleave = null;
  };
}

window.addEventListener('DOMContentLoaded', () => {
    // Set userCircle content
    const user = localStorage.getItem('currentUser') || '';
    const userCircle = document.getElementById('userCircle');
    if (userCircle) {
        userCircle.textContent = user ? user.charAt(1).toUpperCase() : '?';
    }

});