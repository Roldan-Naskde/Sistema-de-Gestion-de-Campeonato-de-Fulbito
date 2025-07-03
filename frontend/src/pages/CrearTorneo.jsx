import { useForm } from "react-hook-form";
import api from "../api/axios";

export default function CrearTorneo() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();

  const onSubmit = async (data) => {
    try {
      await api.post("tournaments/", data);
      reset();
      alert("¡Torneo creado!");
    } catch (error) {
      alert("Error al crear torneo");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 500, margin: "2rem auto" }}>
      <h2>Registrar Torneo</h2>
      <div>
        <label>Nombre:</label>
        <input {...register("name", { required: "El nombre es obligatorio" })} />
        {errors.name && <span>{errors.name.message}</span>}
      </div>
      <div>
        <label>Año/Temporada:</label>
        <input {...register("season_year", { required: "El año es obligatorio" })} />
        {errors.season_year && <span>{errors.season_year.message}</span>}
      </div>
      <div>
        <label>Descripción:</label>
        <input {...register("description")} />
      </div>
      <div>
        <label>Fecha de inicio:</label>
        <input type="date" {...register("start_date", { required: "La fecha es obligatoria" })} />
        {errors.start_date && <span>{errors.start_date.message}</span>}
      </div>
      <div>
        <label>Fecha de fin:</label>
        <input type="date" {...register("end_date", { required: "La fecha es obligatoria" })} />
        {errors.end_date && <span>{errors.end_date.message}</span>}
      </div>
      <button type="submit">Crear Torneo</button>
      {isSubmitSuccessful && <p>¡Torneo registrado!</p>}
    </form>
  );
}