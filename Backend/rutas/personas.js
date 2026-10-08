const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router();


// ===============================
// AGREGAR UNA PERSONA
// POST /personas
// ===============================
router.post("/", async (req, res) => {
     const {
          nombre,
          apellido,
          dni,
          tipo,
          email,
          curso
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `INSERT INTO personas 
               (nombre, apellido, dni, tipo, email, curso)
               VALUES (?, ?, ?, ?, ?, ?)`,
               [
                    nombre,
                    apellido,
                    dni,
                    tipo,
                    email,
                    curso
               ]
          );

          return res.status(201).json({
               mensaje: "Persona agregada correctamente",
               id: resultado.insertId
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo agregar la persona",
               detalle: error.message
          });
     }
});


// ===============================
// LEER TODAS LAS PERSONAS
// GET /personas
// ===============================
router.get("/", async (req, res) => {
     try {
          const [personas] = await pool.execute(
               `SELECT * FROM personas`
          );

          return res.status(200).json(personas);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudieron obtener las personas",
               detalle: error.message
          });
     }
});


// ===============================
// LEER UNA PERSONA POR ID
// GET /personas/1
// ===============================
router.get("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [personas] = await pool.execute(
               `SELECT * FROM personas WHERE id_persona = ?`,
               [id]
          );

          if (personas.length === 0) {
               return res.status(404).json({
                    mensaje: "Persona no encontrada"
               });
          }

          return res.status(200).json(personas[0]);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo obtener la persona",
               detalle: error.message
          });
     }
});


// ===============================
// EDITAR UNA PERSONA
// PUT /personas/1
// ===============================
router.put("/:id", async (req, res) => {
     const { id } = req.params;

     const {
          nombre,
          apellido,
          dni,
          tipo,
          email,
          curso
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `UPDATE personas
                SET nombre = ?,
                    apellido = ?,
                    dni = ?,
                    tipo = ?,
                    email = ?,
                    curso = ?
                WHERE id_persona = ?`,
               [
                    nombre,
                    apellido,
                    dni,
                    tipo,
                    email,
                    curso,
                    id
               ]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Persona no encontrada"
               });
          }

          return res.status(200).json({
               mensaje: "Persona actualizada correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo actualizar la persona",
               detalle: error.message
          });
     }
});


// ===============================
// ELIMINAR UNA PERSONA
// DELETE /personas/1
// ===============================
router.delete("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [resultado] = await pool.execute(
               `DELETE FROM personas WHERE id_persona = ?`,
               [id]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Persona no encontrada"
               });
          }

          return res.status(200).json({
               mensaje: "Persona eliminada correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo eliminar la persona",
               detalle: error.message
          });
     }
});


module.exports = router;