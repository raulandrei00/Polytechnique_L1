// Video figure CSC_1S004_test2_video.mov illustrates the expected behavior
// of the Web page to reproduce

// STEP_1: When loading the page, this script should automatically create
//         a <div> whose id is 'shapeContainer'. CSS styling instructions
//         for #shapeContainer are already defined in style.css
//         #shapeContainer should be a child of div#main (which already exists)
// 
// STEP_2: Clicking the 'Add' button triggers callback function addShapes().
//         This function is already defined below, but empty. Write its
//         contents. See additional instructions in that function's comments.
//
// STEP_3: Clicking the 'Clear' button triggers callback function
//         clearContainer(). This function is already defined below, but empty.
//         Write its contents. See additional instructions in that function's
//         comments.
//
// STEP_4: Attach an event listener to the shapes that you create in
//         #shapeContainer so that when clicking on a shape, that shape, and
//         that shape *only*, gets removed from the container (it disappears).
//
// BONUS:  in STEP_4 you were asked to remove shapes instantaneously. Change
//         this code so as to fade out the shape smoothly in 800ms before it
//         actually gets removed. Use an opacity animation for this.


// STEP_1: Create div#shapeContainer
let shapeContainer = document.createElement("div");
shapeContainer.id = "shapeContainer";

document.getElementById("main").appendChild(shapeContainer);


/* Callback triggered when any key is pressed in the input text field. */
function handleKeyEvent(e){
   /* e contains data about the event.
      visit http://keycode.info/ to find out how to test for the right key value. */
    if (e.keyCode === 13) {
        // hitting enter key
        e.preventDefault();
        addShapes();
    }
};

/* Function executed when the "Add" button is clicked,
   or from handleKeyEvent when the enter key is pressed. */
function addShapes(){
    // STEP_2: actually add the shapes to div#shapeContainer, taking into account:
    // a) the type of shape selected by the user (circles or squares)
    let shapeType = document.getElementById('shapeType').value;
    let shapeCount = parseInt(document.getElementById("countTf").value) || 10;
    let selectedColor = document.getElementById("selectedColor").value;
    let randomColors = document.getElementById("randomColor").checked;

    for (let i = 0; i < shapeCount; i++) {
        let shape = document.createElement("div");
        shape.className = shapeType; // 'circle' or 'square'
        shape.style.backgroundColor = randomColors 
            ? `#${Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0')}` 
            : selectedColor;
        // shape.style.backgroundColor = randomColors 
        //     ? `#${Math.floor(Math.random() * 16777215).toString(16)}` 
        //     : selectedColor;

        shape.addEventListener("click", function () {
            shape.style.transition = "opacity 0.8s";
            shape.style.opacity = "0";
            setTimeout(() => shape.remove(), 800);
        });

        shapeContainer.appendChild(shape);
        console.log("Shape added:", shapeType, "with color:", shape.style.backgroundColor);
        console.log(shape);
    }
    // b) the number of shapes entered by the user (10 by default)
    // c) the color of shapes selected by the user (black by default)
    // d) or generating a random color for each shape individually
    //    if the 'random' checkbox is ticked.
};

function clearContainer(){
    // STEP_3: clear div#shapeContainer
    // remove all shapes from the container
    while (shapeContainer.firstChild) {
        shapeContainer.removeChild(shapeContainer.firstChild);
    }
};
