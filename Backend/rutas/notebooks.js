const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router();

// ===============================
// AGREGAR UNA NOTEBOOK
// ===============================
router.post("/", async (req, res) => {
     const {
          marca,
          empresa,
          num_serie,
          estado
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `INSERT INTO notebooks (marca, empresa, num_serie, estado)
                VALUES (?, ?, ?, ?)`,
               [
                    marca,
                    empresa,
                    num_serie,
                    estado
               ]
          );

          return res.status(201).json({
               mensaje: "Notebook agregada correctamente",
               id: resultado.insertId
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo agregar la notebook",
               detalle: error.message
          });
     }
});


// ===============================
// LEER TODAS LAS NOTEBOOKS
// GET /notebooks
// ===============================
router.get("/", async (req, res) => {
     try {
          const [notebooks] = await pool.execute(
               `SELECT * FROM notebooks`
          );

          return res.status(200).json(notebooks);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudieron obtener las notebooks",
               detalle: error.message
          });
     }
});


// ===============================
// LEER UNA NOTEBOOK POR ID
// GET /notebooks/1
// ===============================
router.get("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [notebooks] = await pool.execute(
               `SELECT * FROM notebooks WHERE id_notebook = ?`,
               [id]
          );

          if (notebooks.length === 0) {
               return res.status(404).json({
                    mensaje: "Notebook no encontrada"
               });
          }

          return res.status(200).json(notebooks[0]);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo obtener la notebook",
               detalle: error.message
          });
     }
});


// ===============================
// EDITAR UNA NOTEBOOK
// PUT /notebooks/1
// ===============================
router.put("/:id", async (req, res) => {
     const { id } = req.params;

     const {
          marca,
          empresa,
          num_serie,
          estado
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `UPDATE notebooks
                SET marca = ?, empresa = ?, num_serie = ?, estado = ?
                WHERE id_notebook = ?`,
               [
                    marca,
                    empresa,
                    num_serie,
                    estado,
                    id
               ]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Notebook no encontrada"
               });
          }

          return res.status(200).json({
               mensaje: "Notebook actualizada correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo actualizar la notebook",
               detalle: error.message
          });
     }
});


// ===============================
// ELIMINAR UNA NOTEBOOK
// DELETE /notebooks/1
// ===============================
router.delete("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [resultado] = await pool.execute(
               `DELETE FROM notebooks WHERE id_notebook = ?`,
               [id]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Notebook no encontrada"
               });
          }

          return res.status(200).json({
               mensaje: "Notebook eliminada correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo eliminar la notebook",
               detalle: error.message
          });
     }
});


module.exports = router;