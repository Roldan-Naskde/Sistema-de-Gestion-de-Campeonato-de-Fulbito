import { useForm } from "react-hook-form";
import { useQuery } from "react-query";
import api from "../api/axios";

export default function CrearGrupo() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();
  const { data: fases } = useQuery('fases', async () => (await api.get('stages/')).data);

  const onSubmit = async (data) => {
    try {
      await api.post("groups/", data);
      reset();
      alert("¡Grupo creado!");
    } catch (error) {
      alert("Error al crear grupo");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 400, margin: "2rem auto" }}>
      <h2>Registrar Grupo</h2>
      <div>
        <label>Nombre:</label>
        <input {...register("name", { required: "El nombre es obligatorio" })} />
        {errors.name && <span>{errors.name.message}</span>}
      </div>
      <div>
        <label>Fase:</label>
        <select {...register("stage", { required: "Selecciona la fase" })}>
          <option value="">Selecciona...</option>
          {fases && fases.map(f => (
            <option key={f.id} value={f.id}>{f.name}</option>
          ))}
        </select>
        {errors.stage && <span>{errors.stage.message}</span>}
      </div>
      <button type="submit">Crear Grupo</button>
      {isSubmitSuccessful && <p>¡Grupo registrado!</p>}
    </form>
  );
}