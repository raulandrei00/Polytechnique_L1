const textEntry = document.querySelector("#textentry");
textEntry.addEventListener('change',textModified);

function textModified(event) {
  const textRender = document.querySelector("#textrender");
  textRender.textContent = textEntry.value;
  console.log(textEntry.value);
}

console.log("hello")