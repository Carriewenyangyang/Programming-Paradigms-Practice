const express = require('express');
const app = express();
const port = 3000;

// 定义一个简单的路由
app.get('/', (req, res) => {
  res.send('Hello, this is a Node.js backend!');
});

// 启动服务器
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
