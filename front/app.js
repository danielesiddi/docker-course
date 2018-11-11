var express = require('express');
var request = require('sync-request')
var app = express();

app.get_users = function() {
  const http = require('http');

  users_url='http://' + process.env.BACKEND_HOSTNAME + '/users'
  console.log('Getting users from URL: ' + users_url)
  var res = request('GET',users_url);

  if(res.statusCode == 200) {

    var result = res.getBody();
    console.log('Response received with success: [' + result + ']');
    var decoded=JSON.parse(result);

    return decoded.result;
  }

  console.log('Error retrieving users');
  return [];
};

app.get('/', function (req, res) {
  users=app.get_users();
  console.log(users)
  if(!users) {
    res.send('<h3>No employees found</h3>');
    return;
  }
  var html_page='<html><body><h3>Employees List</h3>';
  for (var user_pos in users) {
    var user=users[user_pos];
    console.log("User found: " + user)
    html_page += "<p>" + user[1] + " (" + user[0] + ")</p>";
  }
  html_page += "</body></html>";
  res.send(html_page);
});

app.listen(3000, function () {
  console.log('App listening on port 3000!');
});

