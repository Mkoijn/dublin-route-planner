function isValidTime(){
  var now_hours = new Date().getHours();
  var now_minutes = new Date().getMinutes();
  var valid = false;
  if (now_hours >= 5 || (now_hours < 1 && now_minutes < 30)) {
     valid = true;
  }
  return valid;
}
