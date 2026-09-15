const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router

//Agregar una notebook
router.post("/", async(req, res) => {
     const {
      id_notebooks,
      marca,
      empresa,
      num_serie,
      estado
     } = req.body;
});