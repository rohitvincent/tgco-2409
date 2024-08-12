var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/json'});
  res.end('{"invoices":'+getBodyMessage()+'}');
}).listen(9092); 

function getBodyMessage() {
    return '[' +
    '{"ID":0,"customerId":0,"amount":12.00},'+
    '{"ID":1,"customerId":0,"amount":235.78},'+
    '{"ID":2,"customerId":1,"amount":5.060},'+
    '{"ID":3,"customerId":2,"amount":12.60},'+
    '{"ID":4,"customerId":3,"amount":0.99},'+
    '{"ID":5,"customerId":1,"amount":12.00},'+
    '{"ID":6,"customerId":1,"amount":235.78},'+
    '{"ID":7,"customerId":1,"amount":5.060},'+
    '{"ID":8,"customerId":1,"amount":12.60},'+
    '{"ID":9,"customerId":1,"amount":0.99},'+
    '{"ID":10,"customerId":3,"amount":12.00},'+
    '{"ID":11,"customerId":2,"amount":235.78},'+
    '{"ID":12,"customerId":1,"amount":5.060},'+
    '{"ID":13,"customerId":0,"amount":12.60},'+
    '{"ID":15,"customerId":3,"amount":0.99}'+          
    ']';
}
