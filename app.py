def create_app():
    javascript_code = """
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(3000, () => {
  console.log('API server is running on port 3000');
});
"""
    with open("app.js", "w") as file:
        file.write(javascript_code)
