# 📦 Sistema de Gestión de Inventario

Sistema de gestión de inventario desarrollado en **Python**, utilizando **SQLite** como base de datos y **Colorama** para mejorar la visualización en consola.

El proyecto permite administrar productos de forma simple y persistente, simulando un sistema real de inventario con operaciones CRUD y control de stock.

---

## 🚀 Funcionalidades

- ✅ Registrar productos
- 📋 Mostrar todos los productos
- ✏️ Actualizar productos existentes
- 🗑️ Eliminar productos
- 🔍 Buscar productos por ID
- ⚠️ Reportar productos con stock mínimo
- 🎨 Interfaz en consola con colores usando Colorama
- 💾 Persistencia de datos con SQLite

---

## 🧠 Tecnologías utilizadas

- **Python 3**
- **SQLite3**
- **Colorama**

---

## 📁 Estructura de la base de datos

Tabla `productos`:

| Campo | Tipo |
|-----|------|
| id | INTEGER (PK) |
| nombre | TEXT |
| descripcion | TEXT |
| cantidad | INTEGER |
| precio | REAL |
| categoria | TEXT |

---

