let x = document.getElementById("myAudio");

let canvas,
  context,
  counter = 0;
let i = 0;

let playing = false;

const start = () => {
  if (playing == true) {
    i = 0;
    x.pause();
    playing = false;
  } else {
    i = 1;
    x.play();
    playing = true;
  }
};

let draw = () => {
  requestAnimationFrame(draw);
  canvas = document.getElementById("canvas");
  context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);

  context.save();
  context.translate(
    Math.floor(canvas.width / 2),
    Math.floor(canvas.height / 2)
  );
  context.rotate(counter * 0.04);

  let gradient = context.createRadialGradient(850, 100, 10, 10, 10, 1000);
  gradient.addColorStop(0, "white");
  gradient.addColorStop(1, "green");
  context.fillStyle = gradient;
  context.fillRect(-1000, -1000, 10000, 10000);

  context.beginPath();
  //body
  context.moveTo(0, -100);
  context.lineTo(0, 100);
  context.stroke();
  //left arm
  context.moveTo(0, -100);
  context.lineTo(-100, 0);
  context.stroke();
  //right arm
  context.moveTo(0, -100);
  context.lineTo(100, 0);
  context.stroke();
  //right leg
  context.moveTo(0, 100);
  context.lineTo(100, 200);
  context.stroke();
  //left leg
  context.moveTo(0, 100);
  context.lineTo(-100, 200);
  context.stroke();
  //head
  context.moveTo(50, -150);
  context.arc(0, -150, 50, 0, Math.PI * 2, false);
  context.stroke();

  // text
  context.font = "30px Garamond";
  context.fillStyle = "#220033";
  context.fillText("Henri Mattila", 110, 100);

  if (i > 0) {
    counter++;
  }

  context.restore();
};
