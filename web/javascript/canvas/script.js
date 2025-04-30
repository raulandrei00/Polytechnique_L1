"use strict";

// Creation of the canvas
const canvasElement = document.querySelector('canvas');
const ctx = canvasElement.getContext('2d');

// Size of the canvas
ctx.canvas.width = 600;
ctx.canvas.height = 600;

// Draw some rectangles
ctx.fillStyle = 'lightgray';
ctx.fillRect(0,0,600,600);

ctx.fillStyle = 'green';
ctx.fillRect(50,50,250,400);

ctx.fillStyle = 'yellow';
ctx.fillRect(100,150,50,50);

// Draw some lines
ctx.lineWidth = 2;
ctx.strokeStyle = 'red';
ctx.beginPath();
ctx.moveTo(500,150);
ctx.lineTo(500,300);
ctx.lineTo(200,300);
ctx.lineTo(350,75);
ctx.lineTo(150,150);
ctx.fill();
ctx.stroke();

// Draw a circle
ctx.fillStyle = 'salmon';
ctx.beginPath();
ctx.arc(400,400,50,0,2*Math.PI);
ctx.fill();