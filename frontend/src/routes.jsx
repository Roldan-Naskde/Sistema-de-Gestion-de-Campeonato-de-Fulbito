import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Equipos from './pages/Equipos';
import Jugadores from './pages/Jugadores';
import Calendario from './pages/Calendario';
import TablaPosiciones from './pages/TablaPosiciones';
import CrearEquipo from './pages/CrearEquipo';
import CrearJugador from './pages/CrearJugador';
import CrearPartido from './pages/CrearPartido';
import CrearEventoPartido from './pages/CrearEventoPartido';
import EventosPartido from './pages/EventosPartido';
import CrearTorneo from './pages/CrearTorneo';
import CrearFase from './pages/CrearFase';
import CrearGrupo from './pages/CrearGrupo';
import CrearSede from './pages/CrearSede';
import CrearArbitro from './pages/CrearArbitro';
import Torneos from './pages/Torneos';
import EditarTorneo from './pages/EditarTorneo';
import Login from './pages/Login';
import PrivateRoute from './components/PrivateRoute';
import AdminPanel from './pages/AdminPanel'; // O el componente que quieras proteger
import Navbar from './components/Navbar';

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Navbar />
      {/* Aquí puedes agregar más componentes comunes como Footer, etc. */}
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/equipos" element={<Equipos />} />
        <Route path="/jugadores" element={<Jugadores />} />
        <Route path="/calendario" element={<Calendario />} />
        <Route path="/tabla-posiciones" element={<TablaPosiciones />} />
        <Route path="/equipos/crear" element={<CrearEquipo />} />
        <Route path="/jugadores/crear" element={<CrearJugador />} />
        <Route path="/partidos/crear" element={<CrearPartido />} />
        <Route path="/eventos/crear" element={<CrearEventoPartido />} />
        <Route path="/eventos" element={<EventosPartido />} />
        <Route path="/torneos/crear" element={<CrearTorneo />} />
        <Route path="/fases/crear" element={<CrearFase />} />
        <Route path="/grupos/crear" element={<CrearGrupo />} />
        <Route path="/sedes/crear" element={<CrearSede />} />
        <Route path="/arbitros/crear" element={<CrearArbitro />} />
        <Route path="/torneos" element={<Torneos />} />
        <Route path="/torneos/editar/:id" element={<EditarTorneo />} />
        <Route path="/login" element={<Login />} />
        <Route path="/admin" element={
          <PrivateRoute>
            <AdminPanel />
          </PrivateRoute>
        } />
        {/* Agrega más rutas según sea necesario */}
      </Routes>
    </BrowserRouter>
  );
}