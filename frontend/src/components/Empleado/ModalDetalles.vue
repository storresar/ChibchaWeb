<template>
  <form class="w-full max-w-md max-h-96 md:max-h-full  bg-red-1000 bg-opacity-90 p-4 rounded-sm overflow-auto" @submit.prevent="sendForm">
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0"  >
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-first-name">
          Descripción del problema
        </label>
        <input v-model="datos.desc_problema"
        class="appearance-none block w-full bg-gray-200 transition-colors duration-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
        type="text">
      </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3">
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-password">
          Nivel de prioridad
        </label>
        <input v-model="datos.nivel"
        class="appearance-none block w-full bg-gray-200 border transition-colors duration-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        type="text">
      </div>
      <div>
      </div>
    </div>
  </form>
</template>

<script>
import { reactive } from "vue";

export default {
  props: {
      tickets_filter: Object,
  },
  setup(props) {
    console.log(props)
    const datos = reactive({
      desc_problema: props.tickets_filter.desc_problema,
      nivel: props.tickets_filter.nivel,
      desc_solucion: props.tickets_filter.desc_solucion,
      solucionado: props.tickets_filter.solucionado,
      vendedor: props.tickets_filter.vendedor,
      cod_cliente: props.tickets_filter.id,
    });

    return { datos }
  }
};

</script>

<style>


</style>