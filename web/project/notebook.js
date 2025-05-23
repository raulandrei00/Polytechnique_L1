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

// Save the canvas as an image
document.getElementById('save').addEventListener('click', () => {
    const imgSrc = canvas.toDataURL('image/png');
    const img = document.createElement('img');
    img.src = imgSrc;
    
    let saved = JSON.parse(localStorage.getItem("savedImages") || "[]");
    saved.push(imgSrc);
    localStorage.setItem("savedImages", JSON.stringify(saved));
    console.log(saved);
    // document.body.appendChild(saved);
    alert("Image saved in browser!");
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
