const express = require("express");

const app=express();
const PORT =3000;

app.use(express.json());

app.listen(PORT, async () => {
    console.log(`Servidor ejecutable en http://localhost:${PORT}`)
})