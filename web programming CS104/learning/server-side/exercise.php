<?php
// Save canvas image to server
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['image'])) 
{
    $data = $_POST['image'];

    $data = str_replace('data:image/png;base64,', '', $data);
    $data = base64_decode($data);

    if (!file_exists('drawings')) {
        mkdir('drawings', 0777, true);
    }

    $filename = 'drawings/' . uniqid('canvas_', true) . '.png';
    file_put_contents($filename, $data);
    exit;
}

// delete gallery 
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset( $_POST['deleteGallery'])) { 

    rmdir('drawings');

}
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Writable Canvas with Save and Load</title>
  <style>
    canvas {
      border: 1px solid #000;
      cursor: crosshair;
    }
    #controls {
      margin-top: 10px;
    }
    #gallery img {
      width: 150px;
      margin: 5px;
      cursor: pointer;
      border: 1px solid #ccc;
    }
  </style>
</head>
<body>
  <h2>Draw on the Canvas</h2>
  <canvas id="drawCanvas" width="600" height="400"></canvas>

  <div id="controls">
    <button onclick="clearCanvas()">Clear</button>
    <button onclick="saveCanvas()">Save</button>
  </div>

  <h3>Saved Drawings (Click to Edit)</h3>
  <div id="gallery">
    <?php
    $files = glob("drawings/*.png");
    foreach ($files as $file) {
        $escaped = htmlspecialchars($file);
        echo "<img src='$escaped' onclick=\"loadImageToCanvas('$escaped')\" alt='Saved drawing'>";
    }
    ?>
  </div>

  <script>
    const canvas = document.getElementById('drawCanvas');
    const ctx = canvas.getContext('2d');
    let drawing = false;

    // Drawing behavior
    canvas.addEventListener('mousedown', (e) => {
      drawing = true;
      ctx.beginPath();
      ctx.moveTo(e.offsetX, e.offsetY);
    });

    canvas.addEventListener('mousemove', (e) => {
      if (!drawing) return;
      ctx.lineTo(e.offsetX, e.offsetY);
      ctx.stroke();
    });

    canvas.addEventListener('mouseup', () => drawing = false);
    canvas.addEventListener('mouseleave', () => drawing = false);

    function clearCanvas() {
      // Clear canvas on screen
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
    //   rmdir("gallery");
      
      fetch('', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'deleteGallery=' + "yes",
      }).then(() => {
        location.reload(); // reload to show saved image
      });
    }

    function saveCanvas() {
      const image = canvas.toDataURL('image/png');
      fetch('', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'image=' + encodeURIComponent(image),
      }).then(() => {
        location.reload(); // reload to show saved image
      });
    }

    function loadImageToCanvas(src) {
      const img = new Image();
      img.onload = function() {
        clearCanvas();
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      };
      img.src = src;
    }
  </script>
</body>
</html>
