<template>
  <form
    class="max-w-md w-120 max-h-96 md:max-h-full  bg-red-1000 bg-opacity-90 p-4 rounded-sm overflow-auto"
    @submit.prevent="sendForm"
  >
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3 mb-6 md:mb-0">
        <label
          class="block uppercase tracking-wide text-white text-xs font-bold mb-2"
          for="grid-first-description"
        >
          Descripción del problema
        </label>
        <div
          class="bg-gray-200  overflow-y-auto break-words h-22 transition-colors text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
        >
          {{ datos.desc_problema }}
        </div>
      </div>

      <div v-if="datos.desc_solucion !== 'Sin respuesta.'">
        <div class="w-full px-3 mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-white text-xs font-bold mb-2"
            for="grid-first-answer"
          >
            Respuesta al problema previamente hecha
          </label>
          <div
            class="bg-gray-200 overflow-y-auto break-words h-22 transition-colors text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
          >
            {{ datos.desc_solucion }}
          </div>
        </div>
      </div>
      <div v-if="!datos.is_respondido">
        <div class="px-3 w-full flex flex-col mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-white text-xs font-bold mb-2"
            for="grid-first-answer2"
          >
            Respuesta del ticket
          </label>
          <div
            class="
             bg-gray-200 w-full break-words transition-colors text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
          >
            <textarea class="w-full"
              v-model="answer"
              required
              placeholder="Escribe tu respuesta aquí..."
            />
          </div>
        </div>
      </div>
    </div>
    <div v-if="!datos.solucionado">
      <div v-if="datos.is_respondido === false">
        <button
          @click="answerTicket(datos)"
          class="ml-2  inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700"
        >
          Responder
        </button>
      </div>
      
      <button
        @click="solveTicket(datos)"
        class="ml-2 inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700"
      >
        Marcar como solucionado
      </button>
    </div>
  </form>
</template>

<script>
/* eslint-disable no-unused-vars */
import { reactive, ref } from "vue";
import { useStore } from "vuex";

export default {
  props: {
    tickets_filter: Object,
  },
  setup(props) {
    const store = useStore();
    console.log(props);
    let answer = ref("");
    const datos = reactive({
      id: props.tickets_filter.id,
      desc_problema: props.tickets_filter.desc_problema,
      nivel: props.tickets_filter.nivel,
      desc_solucion: props.tickets_filter.desc_solucion,
      solucionado: props.tickets_filter.solucionado,
      vendedor: props.tickets_filter.cod_vendedor,
      cod_cliente: props.tickets_filter.cod_cliente,
      is_respondido: props.tickets_filter.is_respondido,
    });

    const answerTicket = async (ticket) => {
      ticket["desc_solucion"] = answer;
        let ticket2 = {
            id: ticket.id,
            desc_problema: ticket.desc_problema,
            desc_solucion: ticket.desc_solucion,
            nivel: ticket.nivel,
            solucionado: ticket.solucionado,
            cod_cliente: ticket.cod_cliente,
            cod_vendedor: ticket.cod_vendedor,
            is_respondido: true,
        }
      console.log(ticket2);
      await store.dispatch('updateTicket', ticket2)
    }

    const solveTicket = async (ticket) => {
      ticket["solucionado"] = true;
        let ticket2 = {
            id: ticket.id,
            desc_problema: ticket.desc_problema,
            desc_solucion: ticket.desc_solucion,
            nivel: ticket.nivel,
            solucionado: ticket.solucionado,
            cod_cliente: ticket.cod_cliente,
            cod_vendedor: ticket.cod_vendedor,
            is_respondido: true,
        }
      console.log(ticket2);
      await store.dispatch('updateTicket', ticket2)
    }

    return { datos, answer, answerTicket, solveTicket };
  },
};
</script>

<style></style>
