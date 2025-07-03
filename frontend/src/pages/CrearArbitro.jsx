import { useForm } from "react-hook-form";
import api from "../api/axios";

export default function CrearArbitro() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();

  const onSubmit = async (data) => {
    try {
      await api.post("referees/", data);
      reset();
      alert("¡Árbitro creado!");
    } catch (error) {
      alert("Error al crear árbitro");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 400, margin: "2rem auto" }}>
      <h2>Registrar Árbitro</h2>
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
        <label>Categoría:</label>
        <input {...register("category")} />
      </div>
      <button type="submit">Crear Árbitro</button>
      {isSubmitSuccessful && <p>¡Árbitro registrado!</p>}
    </form>
  );
}