const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router();


// ===============================
// AGREGAR UN USUARIO
// POST /usuario
// ===============================
router.post("/", async (req, res) => {
     const {
          nombre_usuario,
          contrasena,
          rol,
          id_persona
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `INSERT INTO usuario
               (nombre_usuario, contrasena, rol, id_persona)
               VALUES (?, ?, ?, ?)`,
               [
                    nombre_usuario,
                    contrasena,
                    rol,
                    id_persona
               ]
          );

          return res.status(201).json({
               mensaje: "Usuario agregado correctamente",
               id: resultado.insertId
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo agregar el usuario",
               detalle: error.message
          });
     }
});


// ===============================
// LEER TODOS LOS USUARIOS
// GET /usuario
// ===============================
router.get("/", async (req, res) => {
     try {
          const [usuarios] = await pool.execute(
               `SELECT * FROM usuario`
          );

          return res.status(200).json(usuarios);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudieron obtener los usuarios",
               detalle: error.message
          });
     }
});


// ===============================
// LEER UN USUARIO POR ID
// GET /usuario/1
// ===============================
router.get("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [usuarios] = await pool.execute(
               `SELECT * FROM usuario
                WHERE id_usuario = ?`,
               [id]
          );

          if (usuarios.length === 0) {
               return res.status(404).json({
                    mensaje: "Usuario no encontrado"
               });
          }

          return res.status(200).json(usuarios[0]);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo obtener el usuario",
               detalle: error.message
          });
     }
});


// ===============================
// EDITAR UN USUARIO
// PUT /usuario/1
// ===============================
router.put("/:id", async (req, res) => {
     const { id } = req.params;

     const {
          nombre_usuario,
          contrasena,
          rol,
          id_persona
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `UPDATE usuario
                SET nombre_usuario = ?,
                    contrasena = ?,
                    rol = ?,
                    id_persona = ?
                WHERE id_usuario = ?`,
               [
                    nombre_usuario,
                    contrasena,
                    rol,
                    id_persona,
                    id
               ]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Usuario no encontrado"
               });
          }

          return res.status(200).json({
               mensaje: "Usuario actualizado correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo actualizar el usuario",
               detalle: error.message
          });
     }
});


module.exports = router;