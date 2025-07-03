import { useQuery } from "react-query";
import api from "../api/axios";
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from "@mui/material";

export default function Equipos() {
  const { data, isLoading, error } = useQuery('equipos', async () => (await api.get('teams/')).data);

  if (isLoading) return <div>Cargando...</div>;
  if (error) return <div>Error al cargar equipos</div>;

  return (
    <TableContainer component={Paper} sx={{ maxWidth: 700, margin: "2rem auto" }}>
      <Typography variant="h6" sx={{ p: 2 }}>Equipos</Typography>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Nombre</TableCell>
            <TableCell>Coach</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map(equipo => (
            <TableRow key={equipo.id}>
              <TableCell>{equipo.name}</TableCell>
              <TableCell>{equipo.coach_name}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}