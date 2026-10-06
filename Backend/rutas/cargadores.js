const express = require("express");
const pool = require("../bd/conexion");

const router = express.Router();


// ===============================
// AGREGAR UN CLIENTE
// POST /clientes
// ===============================
router.post("/", async (req, res) => {
     const {
          nombre,
          apellido,
          dni,
          email,
          telefono
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `INSERT INTO clientes (nombre, apellido, dni, email, telefono)
                VALUES (?, ?, ?, ?, ?)`,
               [
                    nombre,
                    apellido,
                    dni,
                    email,
                    telefono
               ]
          );

          return res.status(201).json({
               mensaje: "Cliente agregado correctamente",
               id: resultado.insertId
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo agregar el cliente",
               detalle: error.message
          });
     }
});


// ===============================
// LEER TODOS LOS CLIENTES
// GET /clientes
// ===============================
router.get("/", async (req, res) => {
     try {
          const [clientes] = await pool.execute(
               `SELECT * FROM clientes`
          );

          return res.status(200).json(clientes);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudieron obtener los clientes",
               detalle: error.message
          });
     }
});


// ===============================
// LEER UN CLIENTE POR ID
// GET /clientes/1
// ===============================
router.get("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [clientes] = await pool.execute(
               `SELECT * FROM clientes WHERE id_cliente = ?`,
               [id]
          );

          if (clientes.length === 0) {
               return res.status(404).json({
                    mensaje: "Cliente no encontrado"
               });
          }

          return res.status(200).json(clientes[0]);

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo obtener el cliente",
               detalle: error.message
          });
     }
});


// ===============================
// EDITAR UN CLIENTE
// PUT /clientes/1
// ===============================
router.put("/:id", async (req, res) => {
     const { id } = req.params;

     const {
          nombre,
          apellido,
          dni,
          email,
          telefono
     } = req.body;

     try {
          const [resultado] = await pool.execute(
               `UPDATE clientes
                SET nombre = ?, apellido = ?, dni = ?, email = ?, telefono = ?
                WHERE id_cliente = ?`,
               [
                    nombre,
                    apellido,
                    dni,
                    email,
                    telefono,
                    id
               ]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Cliente no encontrado"
               });
          }

          return res.status(200).json({
               mensaje: "Cliente actualizado correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo actualizar el cliente",
               detalle: error.message
          });
     }
});


// ===============================
// ELIMINAR UN CLIENTE
// DELETE /clientes/1
// ===============================
router.delete("/:id", async (req, res) => {
     const { id } = req.params;

     try {
          const [resultado] = await pool.execute(
               `DELETE FROM clientes WHERE id_cliente = ?`,
               [id]
          );

          if (resultado.affectedRows === 0) {
               return res.status(404).json({
                    mensaje: "Cliente no encontrado"
               });
          }

          return res.status(200).json({
               mensaje: "Cliente eliminado correctamente"
          });

     } catch (error) {
          return res.status(500).json({
               error: "No se pudo eliminar el cliente",
               detalle: error.message
          });
     }
});


module.exports = router;

