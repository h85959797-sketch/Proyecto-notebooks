const express = require("express");
const pool = require("./bd/conexion")
const notebooksRouter = require("./rutas/notebooks")
const loginRouter = require("./rutas/login")
const cargadoresRouter = require("./rutas/cargadores")
const personasRouter = require("./rutas/personas")

const app=express();
const PORT =3000;

app.use(express.json());

app.use("/api/notebooks", notebooksRouter);
app.use("/api/login", loginRouter)
app.use("/api/cargadores", cargadoresRouter)
app.use("/api/personas", personasRouter)

async function probarConexion(){
    try {
         await pool.query("SELECT 1");
         console.log("Conexion exitosa")
    } catch (error) {
        console.log("Error en la conexion")
        console.log(error.message)
    }
}

app.listen(PORT, async () => {
    console.log(`Servidor ejecutable en http://localhost:${PORT}`)
    await probarConexion()
})
