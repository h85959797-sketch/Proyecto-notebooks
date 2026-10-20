const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router();


// ===============================
// AGREGAR UN PRÉSTAMO
// POST /prestamosydevoluciones
// ===============================
router.post("/", async (req, res) => {
     const {
          dia,
          hora_prestamo,
          hora_devolucion,
          estado_devolucion,
          materia,
          observacion,
          id_persona,
          id_notebook
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `INSERT INTO prestamosydevoluciones
               (dia, hora_prestamo, hora_devolucion, estado_devolucion,
                materia, observacion, id_persona, id_notebook)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
               [
                    dia,
                    hora_prestamo,
                    hora_devolucion,
                    estado_devolucion,
                    materia,
                    observacion,
                    id_persona,
                    id_notebook
               ]
          );

          return res.status(201).json({
               mensaje: "Préstamo agregado correctamente",
               id: resultado.insertId
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo agregar el préstamo",
               detalle: error.message
          });
     }
});


// ===============================
// LEER TODOS LOS PRÉSTAMOS
// GET /prestamosydevoluciones
// ===============================
router.get("/", async (req, res) => {
     try {
          const [prestamos] = await pool.execute(
               `SELECT * FROM prestamosydevoluciones`
          );

          return res.status(200).json(prestamos);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudieron obtener los préstamos",
               detalle: error.message
          });
     }
});


// ===============================
// LEER UN PRÉSTAMO POR ID
// GET /prestamosydevoluciones/1
// ===============================
router.get("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [prestamos] = await pool.execute(
               `SELECT * FROM prestamosydevoluciones
                WHERE id_prestamo = ?`,
               [id]
          );

          if (prestamos.length === 0) {
               return res.status(404).json({
                    mensaje: "Préstamo no encontrado"
               });
          }

          return res.status(200).json(prestamos[0]);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo obtener el préstamo",
               detalle: error.message
          });
     }
});


// ===============================
// EDITAR UN PRÉSTAMO
// PUT /prestamosydevoluciones/1
// ===============================
router.put("/:id", async (req, res) => {
     const { id } = req.params;

     const {
          dia,
          hora_prestamo,
          hora_devolucion,
          estado_devolucion,
          materia,
          observacion,
          id_persona,
          id_notebook
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `UPDATE prestamosydevoluciones
                SET dia = ?,
                    hora_prestamo = ?,
                    hora_devolucion = ?,
                    estado_devolucion = ?,
                    materia = ?,
                    observacion = ?,
                    id_persona = ?,
                    id_notebook = ?
                WHERE id_prestamo = ?`,
               [
                    dia,
                    hora_prestamo,
                    hora_devolucion,
                    estado_devolucion,
                    materia,
                    observacion,
                    id_persona,
                    id_notebook,
                    id
               ]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Préstamo no encontrado"
               });
          }

          return res.status(200).json({
               mensaje: "Préstamo actualizado correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo actualizar el préstamo",
               detalle: error.message
          });
     }
});


module.exports = router;u