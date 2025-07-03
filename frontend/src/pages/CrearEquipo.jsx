import { useForm } from "react-hook-form";
import api from "../api/axios";
import { TextField, Button, Box, Typography, Paper, Alert, Snackbar } from "@mui/material";
import { useState } from "react";

export default function CrearEquipo() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();
  const [success, setSuccess] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  const onSubmit = async (data) => {
    try {
      await api.post("teams/", data);
      reset();
      setSuccess(true);
      setErrorMsg("");
    } catch (error) {
      setErrorMsg("Error al crear equipo. Verifica los datos o intenta más tarde.");
    }
  };

  return (
    <Paper elevation={3} sx={{ maxWidth: 400, margin: "2rem auto", p: 3 }}>
      <Typography variant="h5" gutterBottom>Registrar Equipo</Typography>
      <Box component="form" onSubmit={handleSubmit(onSubmit)} noValidate>
        <TextField
          label="Nombre"
          fullWidth
          margin="normal"
          {...register("name", {
            required: "El nombre es obligatorio",
            minLength: { value: 3, message: "El nombre debe tener al menos 3 caracteres" }
          })}
          error={!!errors.name}
          helperText={errors.name?.message}
        />
        <TextField
          label="Coach"
          fullWidth
          margin="normal"
          {...register("coach_name", {
            pattern: { value: /^[A-Za-z ]*$/, message: "Solo letras y espacios" }
          })}
          error={!!errors.coach_name}
          helperText={errors.coach_name?.message}
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Crear
        </Button>
      </Box>
      <Snackbar open={success} autoHideDuration={3000} onClose={() => setSuccess(false)}>
        <Alert severity="success" sx={{ width: '100%' }}>¡Equipo registrado exitosamente!</Alert>
      </Snackbar>
      {errorMsg && (
        <Alert severity="error" sx={{ mt: 2 }}>{errorMsg}</Alert>
      )}
    </Paper>
  );
}