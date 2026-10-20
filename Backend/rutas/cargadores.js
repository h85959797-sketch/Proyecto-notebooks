const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router();


// ===============================
// AGREGAR UN CARGADOR
// POST /cargadores
// ===============================
router.post("/", async (req, res) => {
     const {
          num,
          estado,
          observaciones,
          id_notebook
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `INSERT INTO cargadores (num, estado, observaciones, id_notebook)
                VALUES (?, ?, ?, ?)`,
               [
                    num,
                    estado,
                    observaciones,
                    id_notebook
               ]
          );

          return res.status(201).json({
               mensaje: "Cargador agregado correctamente",
               id: resultado.insertId
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo agregar el cargador",
               detalle: error.message
          });
     }
});


// ===============================
// LEER TODOS LOS CARGADORES
// GET /cargadores
// ===============================
router.get("/", async (req, res) => {
     try {
          const [cargadores] = await pool.execute(
               `SELECT * FROM cargadores`
          );

          return res.status(200).json(cargadores);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudieron obtener los cargadores",
               detalle: error.message
          });
     }
});


// ===============================
// LEER UN CARGADOR POR ID
// GET /cargadores/1
// ===============================
router.get("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [cargadores] = await pool.execute(
               `SELECT * FROM cargadores WHERE id_cargador = ?`,
               [id]
          );

          if (cargadores.length === 0) {
               return res.status(404).json({
                    mensaje: "Cargador no encontrado"
               });
          }

          return res.status(200).json(cargadores[0]);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo obtener el cargador",
               detalle: error.message
          });
     }
});


// ===============================
// EDITAR UN CARGADOR
// PUT /cargadores/1
// ===============================
router.put("/:id", async (req, res) => {
     const { id } = req.params;

     const {
          num,
          estado,
          observaciones,
          id_notebook
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `UPDATE cargadores
                SET num = ?,
                    estado = ?,
                    observaciones = ?,
                    id_notebook = ?
                WHERE id_cargador = ?`,
               [
                    num,
                    estado,
                    observaciones,
                    id_notebook,
                    id
               ]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Cargador no encontrado"
               });
          }

          return res.status(200).json({
               mensaje: "Cargador actualizado correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo actualizar el cargador",
               detalle: error.message
          });
     }
});


// ===============================
// ELIMINAR UN CARGADOR
// DELETE /cargadores/1
// ===============================
router.delete("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [resultado] = await pool.execute(
               `DELETE FROM cargadores WHERE id_cargador = ?`,
               [id]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Cargador no encontrado"
               });
          }

          return res.status(200).json({
               mensaje: "Cargador eliminado correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo eliminar el cargador",
               detalle: error.message
          });
     }
});


module.exports = router;