import { useForm } from "react-hook-form";
import api from "../api/axios";

export default function CrearJugador() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();

  const onSubmit = async (data) => {
    try {
      await api.post("players/", data);
      reset();
      alert("¡Jugador creado!");
    } catch (error) {
      alert("Error al crear jugador");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 400, margin: "2rem auto" }}>
      <h2>Registrar Jugador</h2>
      <div>
        <label>Nombre:</label>
        <input {...register("first_name", { required: "El nombre es obligatorio" })} />
        {errors.first_name && <span>{errors.first_name.message}</span>}
      </div>
      <div>
        <label>Apellido:</label>
        <input {...register("last_name", { required: "El apellido es obligatorio" })} />
        {errors.last_name && <span>{errors.last_name.message}</span>}
      </div>
      <div>
        <label>Fecha de nacimiento:</label>
        <input type="date" {...register("birth_date", { required: "La fecha es obligatoria" })} />
        {errors.birth_date && <span>{errors.birth_date.message}</span>}
      </div>
      <div>
        <label>Posición:</label>
        <input {...register("position", { required: "La posición es obligatoria" })} />
        {errors.position && <span>{errors.position.message}</span>}
      </div>
      <div>
        <label>ID del equipo:</label>
        <input type="number" {...register("team", { required: "El equipo es obligatorio" })} />
        {errors.team && <span>{errors.team.message}</span>}
      </div>
      <button type="submit">Crear</button>
      {isSubmitSuccessful && <p>¡Jugador registrado!</p>}
    </form>
  );
}