function isValidTime(){
  var now_hours = new Date().getHours();
  var now_minutes = new Date().getMinutes();
  var valid = false;
  if (now_hours >= 5 || (now_hours < 1 && now_minutes < 30)) {
     valid = true;
  }
  return valid;
}

function time_convert(num){
  var converted = '';
  var hours = Math.floor(num / 60);
  var minutes = num % 60;
  if(hours == 0){
    converted = minutes + ' mins';
    return converted;
  } else if (hours == 1){
      converted = hours + ' hr' + ' ' + minutes + ' mins';
      return converted
  } else {
      converted = hours + ' hrs' + ' ' + minutes + ' mins';
      return converted
  }
}
