var leapFare = "";
var cashFare = "";
function getBusFares(noStops){
    if(noStops < 10){
      leapFare = "1.55";
      cashFare = "2.15";
    } else if (noStops < 31) {
      leapFare = "2.25";
      cashFare = "3.00";
    } else {
      leapFare = "2.50";
      cashFare = "3.30";
    }
}
function getDiscountBusFares(noStops){
  if(noStops < 10){
    leapFare = "0.55";
    cashFare = "2.15";
  } else if (10 < noStops < 31) {
    leapFare = "1.25";
    cashFare = "3.00";
  } else {
    leapFare = "1.50";
    cashFare = "3.30";
  }
}
function getLuasZone(stop){
  var zone;
  switch (stop) {
    case "Broombridge Luas Stop":
    case "Cabra Luas Stop":
    case "Phibsborough Luas Stop":
    case "Grangegorman Luas Stop":
      zone = "G1";
      break;
    case "Broadstone - DIT Luas Stop":
      zone = "G1C";
      break;
    case "Dominick Luas Stop":
    case "Parnell Luas Stop":
    case "O'Connell Upper Luas Stop":
    case "GPO Luas Stop":
    case "Westmoreland Luas Stop":
    case "Dawson Luas Stop":
    case "St.Stephen's Green Luas Stop":
    case "Harcourt Luas Stop":
    case "Trinity Luas Stop":
    case "Trinity Luas Stop":
    case "Marlborough Luas Stop":
    case "Abbey Street Luas Stop":
    case "Jervis Luas Stop":
    case "Four Courts Luas Stop":
    case "Smithfield Luas Stop":
    case "Museum Luas Stop":
      zone = 7;
      break
    case "Busáras Luas Stop":
    case "George's Dock Luas Stop":
    case "Connolly Luas Stop":
      zone = "R1C";
      break;
    case "Mayor Square - NCI Luas Stop":
    case "Spencer Dock Luas Stop":
    case "The Point Luas Stop":
      zone = "R1";
      break
    case "Heuston Luas Stop":
      zone = 6;
      break;
    case "Charlemont Luas Stop":
      zone = 8;
      break;
    case "James's Luas Stop":
    case "Fatima Luas Stop":
    case "Rialto Luas Stop":
      zone = 5;
      break;
    case "Suir Road Luas Stop":
      zone = 4;
      break;
    case "Goldenbridge Luas Stop":
    case "Drimnagh Luas Stop":
    case "Blackhorse Luas Stop":
    case "Bluebell Luas Stop":
    case "Kylemore Luas Stop":
      zone = 3;
      break;
    case "Red Cow Luas Stop":
      zone = 2;
      break;
    case "Kingswood Luas Stop":
    case "Belgard Luas Stop":
    case "Cookstown Luas Stop":
    case "Hospital Luas Stop":
    case "Tallaght (The Square) Luas Stop":
    case "Fettercairn Luas Stop":
    case "Cheeverstown Luas Stop":
    case "Citywest Campus Luas Stop":
    case "Fortunestown Luas Stop":
    case "Saggart Luas Stop":
      zone = 1;
      break;
    case "Ranelagh Luas Stop":
    case "Beechwood Luas Stop":
    case "Cowper Luas Stop":
    case "Milltown Luas Stop":
    case "Windy Arbour Luas Stop":
      zone = 9;
      break;
    case "Dundrum Luas Stop":
      zone = 10;
      break;
    case "Balally Luas Stop":
    case "Kilmacud Luas Stop":
    case "Stillorgan Luas Stop":
      zone = 11;
      break;
    case "Sandyford Luas Stop":
      zone = 12;
      break;
    case "Central Park Luas Stop":
    case "Glencairn Luas Stop":
    case "The Gallops Luas Stop":
    case "Leopardstown Valley Luas Stop":
      zone = 13;
      break;
    case "Ballyogan Wood Luas Stop":
      zone = 14;
      break;
    case "Carrickmines Luas Stop":
    case "Laughanstown Luas Stop":
    case "Cherrywood Luas Stop":
    case "Bride's Glen Luas Stop":
      zone = 15;
      break;
  }
  return zone;
}

function cleanLuasZone(startZone,finishZone){
  if(startZone == "G1C" && finishZone == "R1C")
  {
    startZone = 6;
    finishZone = 8;
  } else if(startZone == "G1C" && finishZone == "R1")
  {
    startZone = 6;
    finishZone = 9;
  } else if(startZone == "R1" && finishZone == "R1")
  {
    startZone = 6;
    finishZone = 6;
  } else if(startZone == "G1C" && finishZone == "G1")
  {
    startZone = 6;
    finishZone = 5;
  } else if(startZone == "G1" && finishZone == "G1")
  {
    startZone = 6;
    finishZone = 6;
  } else if(startZone == "G1" && finishZone == "G1C")
  {
    startZone = 5;
    finishZone = 6;
  } else if(startZone == "G1" && finishZone == "R1C")
  {
    startZone = 5;
    finishZone = 8;
  } else if(startZone == "G1" && finishZone == "R1")
  {
    startZone = 5;
    finishZone = 9;
  } else if(startZone == "R1C" && finishZone == "R1")
  {
    startZone = 5;
    finishZone = 6;
  } else if(startZone == "R1C" && finishZone == "R1C")
  {
    startZone = 6;
    finishZone = 6;
  } else if(startZone == "R1C" && finishZone == "G1C")
  {
    startZone = 6;
    finishZone = 8;
  } else if(startZone == "R1C" && finishZone == "G1")
  {
    startZone = 6;
    finishZone = 9;
  } else if(startZone == "R1" && finishZone == "R1C")
  {
    startZone = 5;
    finishZone = 6;
  } else if(startZone == "R1" && finishZone == "G1C")
  {
    startZone = 5;
    finishZone = 8;
  } else if(startZone == "R1" && finishZone == "G1")
  {
    startZone = 5;
    finishZone = 9;
  } else if (startZone <= 7 && finishZone == "G1C") {
    finishZone = 8;
  } else if (startZone <= 7 && finishZone == "R1C") {
    finishZone = 8;
  } else if (startZone <= 7 && finishZone == "R1") {
    finishZone = 9;
  } else if (startZone <= 7 && finishZone == "G1") {
    finishZone = 9;
  } else if (startZone > 7 && finishZone == "G1C") {
    finishZone = 6;
  } else if (startZone > 7 && finishZone == "R1C") {
    finishZone = 6;
  } else if (startZone > 7 && finishZone == "G1")  {
    finishZone = 5;
  } else if (startZone > 7 && finishZone == "R1") {
    finishZone = 5;
  } else if (finishZone <= 7 && startZone == "G1C") {
    startZone = 8;
  } else if (finishZone <= 7 && startZone == "R1C") {
    startZone = 8;
  } else if (finishZone <= 7 && startZone == "R1") {
    startZone = 9;
  } else if (finishZone <= 7 && startZone == "G1") {
    startZone = 9;
  } else if (finishZone > 7 && startZone == "R1C") {
    startZone = 6;
  } else if (finishZone > 7 && startZone == "G1C") {
    startZone = 6;
  } else if (finishZone > 7 && startZone == "G1") {
    startZone = 5;
  } else if (finishZone > 7 && startZone == "R1") {
    startZone = 5;
  }
  return {startZone, finishZone};
}
function getLuasFares(start, finish){
  leapFare = "";
  cashFare = "";
  var startZone = getLuasZone(start);
  var finishZone = getLuasZone(finish);

  var zones = cleanLuasZone(startZone, finishZone);
  console.log(zones);
  var difference = Math.abs(zones.startZone - zones.finishZone);
  console.log("diff: " + difference);
  if(isNaN(difference)){
    return;
  }

  switch (difference) {
    case 0:
    case 1:
      leapFare = "<span style='background-color: #00AC70;padding-left:1px;padding-top:3px;padding-bottom:3px;padding-right:5px;border-radius:2px;color:white;margin-left: 10px;'>&nbsp;Leap €1.54</span>";
      cashFare = "<br>Cash €2.10";
      break;
    case 2:
    case 3:
      leapFare = "<span style='background-color: #00AC70;padding-left:1px;padding-top:3px;padding-bottom:3px;padding-right:5px;border-radius:2px;color:white;margin-left: 10px;'>&nbsp;Leap €2.00</span>";
      cashFare = "<br>Cash €2.80";
      break;
    case 4:
    case 5:
    case 6:
    case 7:
      leapFare = "<span style='background-color: #00AC70;padding-left:1px;padding-top:3px;padding-bottom:3px;padding-right:5px;border-radius:2px;color:white;margin-left: 10px;'>&nbsp;Leap €2.27</span>";
      cashFare = "<br>Cash €3.10";
      break;
    case 8:
    case 9:
    case 10:
    case 11:
    case 12:
    case 13:
    case 14:
      leapFare = "<span style='background-color: #00AC70;padding-left:1px;padding-top:3px;padding-bottom:3px;padding-right:5px;border-radius:2px;color:white;margin-left: 10px;'>&nbsp;Leap €2.40</span>";
      cashFare = "<br>Cash €3.20";
      break;
  }
  var x = document.getElementById("leapFares");
  x.innerHTML = cashFare  + leapFare;
  console.log(x);
}
