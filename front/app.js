var express = require('express');
var app = express();

app.get_users = function() {
  const https = require('https');

  http.get('http://' + process.env.BACKEND_HOSTNAME + '/users', (resp) => {
    Console.log(resp);
  });
};

app.get('/', function (req, res) {
  res.send('Employees List');
  app.get_users();
});

app.listen(3000, function () {
  console.log('App listening on port 3000!');
});

