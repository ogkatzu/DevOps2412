//Calculate Tip
function calculateTip() {
  var billAmt = document.getElementById("billamt").value;
  var serviceQual = document.getElementById("serviceQual").value;
  var numOfPeople = document.getElementById("peopleamt").value;
  var musicQual = document.getElementById("musicQual").value;
  //validate input
  if (billAmt === "" || serviceQual == 0) {
    alert("Please enter values");
    return;
  }
  //Check to see if this input is empty or less than or equal to 1
  if (numOfPeople === "" || numOfPeople <= 1) {
    numOfPeople = 1;
    document.getElementById("each").style.display = "none";
  } else {
    document.getElementById("each").style.display = "block";
  }



  // Calculate tip
  var tipPerPerson = (billAmt * serviceQual) / numOfPeople; // Individual tip without music quality
  var tipWithMusic = parseFloat(tipPerPerson) + parseFloat(musicQual); // Adding music quality to the individual tip

  // Display the tip without rounding to ensure music quality is added as intended
  document.getElementById("totalTip").style.display = "block";
  document.getElementById("tip").innerHTML = tipWithMusic;
}



//Hide the tip amount on load
document.getElementById("totalTip").style.display = "none";
document.getElementById("each").style.display = "none";

//click to call function
document.getElementById("calculate").onclick = function() {
  calculateTip();

};
