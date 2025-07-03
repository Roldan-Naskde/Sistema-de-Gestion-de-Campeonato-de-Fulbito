import { useForm } from "react-hook-form";
import api from "../api/axios";
import { useState } from "react";
import { TextField, Button, Box, Typography, Paper, Alert } from "@mui/material";

export default function Login({ onLogin }) {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [errorMsg, setErrorMsg] = useState("");

  const onSubmit = async (data) => {
    try {
      const res = await api.post("token/", data); // endpoint de SimpleJWT
      localStorage.setItem("token", res.data.access);
      setErrorMsg("");
      if (onLogin) onLogin();
    } catch (error) {
      setErrorMsg("Credenciales incorrectas");
    }
  };

  return (
    <Paper elevation={3} sx={{ maxWidth: 400, margin: "2rem auto", p: 3 }}>
      <Typography variant="h5" gutterBottom>Iniciar Sesión</Typography>
      <Box component="form" onSubmit={handleSubmit(onSubmit)} noValidate>
        <TextField
          label="Usuario"
          fullWidth
          margin="normal"
          {...register("username", { required: "El usuario es obligatorio" })}
          error={!!errors.username}
          helperText={errors.username?.message}
        />
        <TextField
          label="Contraseña"
          type="password"
          fullWidth
          margin="normal"
          {...register("password", { required: "La contraseña es obligatoria" })}
          error={!!errors.password}
          helperText={errors.password?.message}
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Ingresar
        </Button>
      </Box>
      {errorMsg && (
        <Alert severity="error" sx={{ mt: 2 }}>{errorMsg}</Alert>
      )}
    </Paper>
  );
}