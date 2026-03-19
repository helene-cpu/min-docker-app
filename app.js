// app.js
const http = require("http");

const server = http.createServer((req, res) => {
  res.write("1,2,3");
  res.end();
});

server.listen(3000, () => {
  console.log("Server kjører på port 3000");
});