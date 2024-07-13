const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");
const cors = require("cors");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

app.post("/api/send-id", async (req, res) => {
  const { id } = req.body;
  localStorage.setItem("id", id);
  try {
    const response = await axios.post("http://localhost:8000/get-data", { id });
    res.json({ result: response.data.result });
  } catch (error) {
    res.status(500).json({ error: "Error communicating with Flask server" });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
