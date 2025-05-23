"use strict;"

// radius of the disc in pixel
let r = 15; 

// GLobal Listener
document.addEventListener('click', addDisc);
document.querySelector('#Start').addEventListener('click', startGame);

// Global variables
const discs = [];   // Arrays of created discs 
let cursor_x;       // User cursor-x
let cursor_y;       // User cursor-y


// First part: Add a disc
// ========================================= //
function addDisc(event) {

    // Current cursor position
    const x = event.clientX;
    const y = event.clientY;

    let border_height = 50; // avoid adding discs in the top of the window
    if(y>border_height){

        // Create a new disc at the cursor position with the current color
        discElement = document.createElement('div');
        discElement.classList.add('disc')
        discElement.style.top = `${y-r}px`;
        discElement.style.left = `${x-r}px`;
        discElement.style.backgroundColor = document.querySelector('#inputColor').value;
        document.querySelector('#container').appendChild(discElement);

        // (This is actually the end of the first part - the rest is the preparation for the animation)
        
        // Set and store the position and velocity parameter of the disc
        let vx = 2*(Math.random()-0.5);
        let vy = 2*(Math.random()-0.5);
        let n = Math.sqrt(vx*vx+vy*vy);
        vx = 3*vx/n;
        vy = 3*vy/n;

        // Add the disc and all its parameter in the array
        discs.push({'x':x,'y':y,'vx':vx,'vy':vy, 'html':discElement});
    }

}


// Second part: Animation and Game
// ========================================= //
function startGame(event) {

    // Remove the previous listener (starting game, and adding disc)
    document.querySelector('#Start').removeEventListener('click', startGame);
    document.removeEventListener('click', addDisc);

    // Create the red disc that will follow the mouse
    const discElement = document.createElement('div');
    discElement.classList.add('disc');
    discElement.classList.add('me');
    document.querySelector('body').appendChild(discElement);

    // Add the new listener such for the red disc to follow the mouse
    document.addEventListener('mousemove', cursorFollow);

    // Remove the buttons from the window
    document.querySelector('#inputColor').style.display = "none";
    document.querySelector('#Start').style.display = "none";

    // Go to the animation loop
    updateGame();
}

// Make the red disc follow the user cursor
function cursorFollow(event) {

    const discElement = document.querySelector('.me');
    discElement.style.top = event.clientY-r+'px';
    discElement.style.left = event.clientX-r+'px';

    cursor_x = event.clientX;
    cursor_y = event.clientY;
}

// Animation loop
function updateGame(event) {

    // Current window width/height
    let w = window.innerWidth;
    let h = window.innerHeight;

    // Go through all the discs that we have created
    for(let k=0; k<discs.length; k=k+1) {
        const element = discs[k];

        // Integrate the x/y position along the vx/vy velocity
        element['x'] += element['vx'];
        element['y'] += element['vy'];

        // Replace the disc at their new position
        element['html'].style.top = element['y']-r+'px';
        element['html'].style.left = element['x']-r+'px';

        // Bouncing effect on the screen border
        if(element['x']<r || element['x']>w-r) {
            element['vx'] = -element['vx'];
        }
        if(element['y']<r || element['y']>h-r) {
            element['vy'] = -element['vy'];
        }

        // Check if the red disc is in collision with the current disc
        let dx = element['x']-cursor_x;
        let dy = element['y']-cursor_y;
        let d = Math.sqrt(dx*dx+dy*dy);
        if(d<2*r) {
            failedGame(k);
            return; // quit the animation if we fail
        }
    }

    // Animation loop
    requestAnimationFrame(updateGame);
}

// Game fail function
function failedGame(k_collide){

    // Change the color of all the discs to gray
    for(let k=0; k<discs.length; k=k+1) {
        discs[k]['html'].style.backgroundColor = 'gray';
    }

    // Show in yellow the colliding disc
    discs[k_collide]['html'].style.backgroundColor = "yellow";

    // Remove the red disc following listener
    document.removeEventListener('mousemove', cursorFollow);

    // Show the final failed message
    document.querySelector('#failed').classList.remove('invisible');

}