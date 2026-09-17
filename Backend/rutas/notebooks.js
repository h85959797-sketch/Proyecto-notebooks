const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router

//Agregar una notebook
router.post("/", async(req, res) => {
     const {
      marca,
      empresa,
      num_serie,
      estado
     } = req.body;

     try {
          const[resultado] = await pool.execute(
               `INSERT INTO notebooks (marca, empresa, num_serie, estado) VALUES (?, ?, ?, ?)`,
               [
               marca,
               empresa,
               num_serie,
               estado
               ]
          )
          return res.status(201).json({
               mensaje: "Producto agregado correctamente"
          })
     } catch (error) {
          return res.status(500).json({
               error: "No se pudo agregar el producto",
               detalle: error.message
          })
     }
});