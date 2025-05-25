"use strict";

const PREVIEW_WIDTH = 300;
const PREVIEW_HEIGHT = 200;
const BOX_WIDTH = 300;
const BOX_HEIGHT = 200;

const userKey = `savedImages_${localStorage.getItem('currentUser')}`;
const saved = JSON.parse(localStorage.getItem(userKey) || "[]");

// Load saved images from localStorage
// const saved = JSON.parse(localStorage.getItem(userKey) || "[]");
const gallery = document.getElementById('gallery');
const emptyMsg = document.getElementById('emptyMsg');
if (saved.length === 0) {
  emptyMsg.style.display = 'block';
} else {
  saved.forEach((data, idx) => {
    const previewCanvas = document.createElement('canvas');
    previewCanvas.width = PREVIEW_WIDTH;
    previewCanvas.height = PREVIEW_HEIGHT;
    previewCanvas.style.border = "2px solid #05386B";
    previewCanvas.style.borderRadius = "8px";
    previewCanvas.style.cursor = "pointer";
    previewCanvas.title = `Size: ${data.width} x ${data.height}`;

    const ctx = previewCanvas.getContext('2d');
    const img = new Image();
    img.onload = function() {
      ctx.clearRect(0, 0, PREVIEW_WIDTH, PREVIEW_HEIGHT);
      ctx.drawImage(
        img,
        0, 0, 3000, 2000, // source: full original image
        0, 0, PREVIEW_WIDTH, PREVIEW_HEIGHT // destination: fit preview canvas
      );
    };
    img.src = data.img;
    
    previewCanvas.onclick = () => {
      localStorage.setItem('openImage', JSON.stringify(saved[idx]));
      window.location.href = "../notebook_interface/notebook.html";
    };
    gallery.appendChild(previewCanvas);
  });
}