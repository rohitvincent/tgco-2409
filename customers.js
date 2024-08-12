var http = require('http');


http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/json'});
  res.end('{"customers":'+getBodyMessage()+'}');
}).listen(9090); 


function getBodyMessage() {
    return '[' +
    '{"ID":0,"name":"Alice","surname":"Klark"},'+
    '{"ID":1,"name":"Bob","surname":"McAdoo"},'+
    '{"ID":2,"name":"Cindy","surname":"Law"},'+
    '{"ID":3,"name":"David","surname":"Nap"},'+
    '{"ID":4,"name":"Elvis","surname":"Blue"}'+
    ']';
}
