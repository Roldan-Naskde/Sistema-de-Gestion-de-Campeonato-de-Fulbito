import { useForm } from "react-hook-form";
import api from "../api/axios";

export default function CrearSede() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();

  const onSubmit = async (data) => {
    try {
      await api.post("venues/", data);
      reset();
      alert("¡Sede creada!");
    } catch (error) {
      alert("Error al crear sede");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 400, margin: "2rem auto" }}>
      <h2>Registrar Sede</h2>
      <div>
        <label>Nombre:</label>
        <input {...register("name", { required: "El nombre es obligatorio" })} />
        {errors.name && <span>{errors.name.message}</span>}
      </div>
      <div>
        <label>Dirección:</label>
        <input {...register("address")} />
      </div>
      <div>
        <label>Ciudad:</label>
        <input {...register("city")} />
      </div>
      <div>
        <label>Capacidad:</label>
        <input type="number" {...register("capacity")} />
      </div>
      <button type="submit">Crear Sede</button>
      {isSubmitSuccessful && <p>¡Sede registrada!</p>}
    </form>
  );
}