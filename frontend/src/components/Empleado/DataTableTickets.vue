<template>
  <div class="flex flex-col overflow-x-auto overflow-y-hidden ">
    <div id="tableMain" style="margin-left:auto;margin-right:auto" class="">
      <div
        class="margin-left:auto;margin-right:auto py-8 align-middle inline-block lg:px-20"
      >  <p>Nivel actual: {{employee.nivel_empleado}}</p>
        <div class="overflow-hidden border rounded shadow border-gray-200">
          <table class="divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Ticket
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Cliente
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Estado
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Nivel
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Opciones
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="ticket in tickets_filter" :key="ticket">
                  <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="ml-4">
                      <div class="text-sm font-small text-gray-800">
                        {{ `# ${ticket.id}` }}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="ml-4">
                      <div class="text-sm font-small text-gray-800">
                            {{filterName(ticket.cod_cliente)}}
                      </div>
                    </div>
                  </div>
                </td>
                <td
                  valign="middle"
                  align="center"
                  class="px-6 py-4 whitespace-nowrap text-sm  font-medium  text-gray-900"
                >
                  <div v-if="ticket.solucionado">
                    <p>Solucionado</p>
                  </div>
                  <div v-else>
                    <p>En espera</p>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="ml-4">
                      <div class="text-sm font-small text-gray-800">
                        {{ `${ticket.nivel}` }}
                      </div>
                    </div>
                  </div>
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                >
                  <Popper placement="left">
                    <button>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-5 w-5 text-gray-800 hover:text-gray-500 transition-colors duration-200"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                      >
                        <path
                          fill-rule="evenodd"
                          d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z"
                          clip-rule="evenodd"
                        />
                      </svg>
                    </button>
                    <template #content>
                      <div class=" flex flex-col gap-2 rounded-md py-2 px-4">
                        <button
                          @click="seeDetails(ticket)"
                          class="px-4 py-2 text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
                        >
                          Ver detalles
                        </button>
                        <div v-if="(ticket.nivel < 3 && !ticket.solucionado)">
                        <button
                          @click="upgradeLevel(ticket)"
                          class="px-4 py-2 text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
                        >
                          Aumentar nivel
                        </button>
                        </div>
                      </div>
                    </template>
                  </Popper>
                </td>
              
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-unused-vars */
import { computed } from "vue";
import { useStore } from "vuex";
import { openModal } from "jenesius-vue-modal";
import ModalDetalles from "../../components/Empleado/ModalDetalles.vue";

export default {
  async setup() {
    const store = useStore();
    await store.dispatch("retrieveUser", window.localStorage.getItem("userId"));
    let user = store.getters.getUser;
    await store.dispatch("retrieveEmployee", user.id);
    let employee = store.getters.getEmployee;
    await store.dispatch("getTicketsList");
    let tickets = computed(() => store.getters.getTickets);

    const tickets_filter = computed(() => 
    tickets.value.filter(ticket => ticket.nivel == employee.nivel_empleado)); 

    await store.dispatch("getUserList");
    let list_users = store.getters.getUsers;

    const filterName = (id_ticket_client) => {
        let list_users2 = list_users.filter((list_user) => list_user.id === id_ticket_client)
        let target_copy = JSON.parse(JSON.stringify(list_users2));
        let username_user;
        try {
            username_user = target_copy[0].username
        } catch (error) {
            username_user = 'No disponible'
        }
        return username_user;
    };
    
    const upgradeLevel = async(ticket) => {
        ticket["nivel"] = ticket.nivel + 1;
        ticket["cod_vendedor"] = employee.id;

        let ticket2 = {
            id: ticket.id,
            desc_problema: ticket.desc_problema,
            desc_solucion: ticket.desc_solucion,
            nivel: ticket.nivel,
            solucionado: ticket.solucionado,
            cod_cliente: ticket.cod_cliente,
            cod_vendedor: ticket.cod_vendedor,
            is_respondido: ticket.is_respondido,
        }
       
        await store.dispatch('updateTicket', ticket2)
    }

    const seeDetails = (tickets_filter) => {
        openModal(ModalDetalles, {tickets_filter})
    };

    return { seeDetails, user, employee, tickets_filter, upgradeLevel, filterName};
  },
};
</script>

<style>
</style>