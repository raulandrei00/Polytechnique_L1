const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const colorPicker = document.getElementById('color');
const sizeInput = document.getElementById('size');
const clearButton = document.getElementById('clear');

let drawing = false;
let brushColor = colorPicker.value;
let brushSize = sizeInput.value;

canvas.addEventListener('mousedown', () => drawing = true);
canvas.addEventListener('mouseup', () => drawing = false);
canvas.addEventListener('mousemove', draw);

colorPicker.addEventListener('input', (e) => brushColor = e.target.value);
sizeInput.addEventListener('input', (e) => brushSize = e.target.value);
clearButton.addEventListener('click', () => ctx.clearRect(0, 0, canvas.width, canvas.height));

// Save the canvas as an image
document.getElementById('save').addEventListener('click', () => {
    const link = document.createElement('a');
    link.download = '/users/eleves-a/2024/raul-andrei.pop/Desktop/web/project/canvas-image.png'; // File path for the saved image
    link.href = canvas.toDataURL(); // Convert canvas to a data URL
    link.click(); // Trigger the download
});

function draw(e) {
    if (!drawing) return;
    ctx.lineWidth = brushSize;
    ctx.lineCap = 'round';
    ctx.strokeStyle = brushColor;

    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
}