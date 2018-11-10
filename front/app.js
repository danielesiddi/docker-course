var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Employees List');
});

app.listen(3000, function () {
  console.log('App listening on port 3000!');
});
