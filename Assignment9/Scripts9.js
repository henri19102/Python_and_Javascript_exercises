var form = document.querySelector("form");
var log = document.querySelector("#log");

form.addEventListener(
  "submit",
  function (event) {
    var pass = document.getElementById("invalid");
    var data = new FormData(form);
    var output = "";
    var pass1 = document.getElementById("pass1").value;
    var pass2 = document.getElementById("pass2").value;
    if (pass1 === pass2) {
      pass.innerText = "";
      for (const entry of data) {
        if (entry[1] !== "") {
          console.log(entry);
          output += `${entry[1]} \n`;
        }
      }
      log.innerText = output;
      event.preventDefault();
    } else {
      pass.innerText = `INVALID PASSWORD!`;
      event.preventDefault();
    }
  },
  false
);
