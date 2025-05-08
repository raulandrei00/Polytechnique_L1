"use strict;"


// Global variables
const N_row_grid = 9;
const N_col_grid = 10;

let global_time = 0;
let element_to_rotate = []


main();
function main() {
    create_grid();
    animate();
}


// ---------------------------------------------------- //
//                     Grid creation
// ---------------------------------------------------- //
function create_grid() {
    for(let i = 0; i < N_row_grid; i++) {
        const lineContainer = document.createElement('div');
        document.querySelector('#container').appendChild(lineContainer);

        for(let j = 0; j < N_col_grid; j++) { 
            const boxElement = document.createElement('div');
            boxElement.classList.add('box');
            boxElement.classList.add('outline');
            
            lineContainer.appendChild(boxElement);
            set_conditions(i,j,boxElement);
        }
    }
}

function set_conditions(i,j,boxElement) {
    if(j === N_row_grid) {
        boxElement.classList.add('level3');
        boxElement.addEventListener('click', start_rotate);
    }
    else if(j > i) {
        boxElement.classList.add('level2');
        boxElement.addEventListener('click', splitBox);
    }
    else if(j === i) {
        boxElement.classList.add('level1');
        boxElement.addEventListener('click', changeColor);
    }
    else {
        boxElement.classList.add('level0');
        boxElement.addEventListener('click', removeBox);
    }
}

// ---------------------------------------------------- //
//                     Basic functions
// ---------------------------------------------------- //
function removeBox(event) {
    event.target.remove();
}
function changeColor(event) {
    event.target.style.backgroundColor = 'cyan';
}

// ---------------------------------------------------- //
//                     Box Splitting
// ---------------------------------------------------- //
function splitBox(event) {
    const element = event.target;

    // Create two new little boxes
    element.appendChild(createNewLittleBox());
    element.appendChild(createNewLittleBox());
    
    // Clean current targeted element
    element.removeEventListener('click', splitBox);
    element.classList.remove('level2');
    element.classList.remove('outline');
}
function createNewLittleBox() {
    const newBox =  document.createElement('div');
    newBox.classList.add('splitBox');
    newBox.classList.add('outline');
    return newBox;
}



// ---------------------------------------------------- //
//                     Animation 
// ---------------------------------------------------- //

function start_rotate(event) {
    // add the element and the time at which the user clicked on it
    element_to_rotate.push({'element':event.currentTarget,'t0':global_time});
}

const Period = 3000; // 3 seconds
function animate(timestamp) {
    global_time = timestamp;
    for(let i = 0; i < element_to_rotate.length; i++) 
    {
        const e = element_to_rotate[i]['element'];
        const t0 = element_to_rotate[i]['t0'];
        let t = timestamp-t0; // elapsed time since the start of the rotation

        // angle of rotation varies as pi (cos(2 pi t/Period)-1)
        let angle = 3.14*(Math.cos(2*3.14*t/Period)-1);
        e.style.transform = `rotate(${angle}rad)`;

        // remove element from the list once the animation is done
        if(t>=Period) {
            element_to_rotate.splice(i,1);
        }
    }

    requestAnimationFrame( animate );
}