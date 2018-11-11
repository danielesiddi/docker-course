var express = require('express');
var request = require('request')
var app = express();

app.get_users = function() {
  const http = require('http');

  users_url='http://' + process.env.BACKEND_HOSTNAME + '/users'
  console.log('Getting users from URL: ' + users_url)
  request.get(users_url, { json: true }, (err, res, body) => {
    if(err) { return console.log(err); }
    console.log('Response received with success: [' + body.success + ']');

    return body.result
  });
};

app.get('/', function (req, res) {
  users=app.get_users();
  if(!users) {
    res.send('<h3>No employees found</h3>');
    return;
  }
  var html_page='<html><body><h3>Employees List</h3>'
  for (var user in users) {
    html_page += "<p>" + user.name + "</p"
  }
  res.send(html_page);
});

app.listen(3000, function () {
  console.log('App listening on port 3000!');
});

