import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{
      background: "#222",
      color: "#fff",
      padding: "1rem",
      display: "flex",
      flexWrap: "wrap",
      gap: "1rem"
    }}>
      <Link to="/" style={{ color: "#fff" }}>Dashboard</Link>
      <Link to="/torneos" style={{ color: "#fff" }}>Torneos</Link>
      <Link to="/equipos" style={{ color: "#fff" }}>Equipos</Link>
      <Link to="/jugadores" style={{ color: "#fff" }}>Jugadores</Link>
      <Link to="/calendario" style={{ color: "#fff" }}>Calendario</Link>
      <Link to="/tabla-posiciones" style={{ color: "#fff" }}>Tabla de posiciones</Link>
      <Link to="/eventos" style={{ color: "#fff" }}>Eventos</Link>
      <Link to="/admin" style={{ color: "#fff" }}>Admin</Link>
      <Link to="/login" style={{ color: "#fff" }}>Login</Link>
    </nav>
  );
}