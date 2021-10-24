<template>
    <div class="flex flex-col ">
        <div class="overflow-x-auto overflow-y-hidden">
            <div class="py-2 align-middle inline-block min-w-full lg:px-4">
                <div class=" overflow-hidden border rounded shadow border-gray-200">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                        <tr>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Nombre de dominio
                        </th>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            URL de dominio
                        </th>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Distribuidor
                        </th>
                        <th scope="col" class="relative px-6 py-3">
                            <span class="sr-only">Opciones</span>
                        </th>
                        </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">
                            <tr v-for="dominio in paginated" :key="dominio">
                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="flex items-center">
                                <div class="ml-4">
                                    <div class="text-sm font-medium text-gray-900">
                                    {{dominio.nom_dominio}}
                                    </div>
                                </div>
                                </div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="text-sm text-gray-500">{{dominio.link_dominio}}</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                <div class="text-sm text-gray-500">{{dominio.cod_facturacion}}</div>
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                <Popper placement="left">
                                    <button>
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-800 hover:text-gray-500 transition-colors duration-200" viewBox="0 0 20 20" fill="currentColor">
                                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z" clip-rule="evenodd" />
                                        </svg>
                                    </button>
                                    <template #content>
                                        <div class=" flex flex-col gap-2 rounded-md py-2 px-4">
                                            <button @click="deleteDomain(dominio.id)"
                                            class="px-4 py-2 text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none">
                                                Eliminar
                                            </button>
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
import { useStore } from "vuex";
import { computed,ref,inject } from "vue";
export default {
  async setup() {
    const store = useStore()
    const swal = inject('$swal')
    await store.dispatch("retrieveClient", store.getters.getUser.id)
    await store.dispatch("retrieveDatosPlan", store.getters.getClient.id)
    await store.dispatch("retrieveDominios", store.getters.getDatosPlan.id)
    const datosDominios = computed(() => store.getters.getDominios)
    console.log(datosDominios)
    const nPages = 5;
    const begin = ref(0);
    const end = ref(nPages);
    const paginated = computed(() =>
      datosDominios.value.slice(begin.value, end.value)
    );
    const backPage = () => {
      if (begin.value !== 0) begin.value -= nPages;
      else begin.value = 0;
      end.value = begin.value + nPages;
    };
    const fowardPage = () => {
      if (
        begin.value >= 0 &&
        begin.value + nPages <= datosDominios.value.length
      ) {
        begin.value += nPages;
      } else {
        begin.value = 0;
      }
      end.value = begin.value + nPages;
    };
    const deleteDomain = (domainId => {
            swal.fire({
            title: 'Espere un momento',
            html: 'Estamos eliminando el dominio',
            allowOutsideClick: false,
            didOpen: () => {
                swal.showLoading()
                }
            });
            store.dispatch('deleteDomain', {domainId: domainId, cod_factura: store.getters.getDatosPlan.id})
            .then(() => swal.fire({title: 'Dominio eliminado', icon:'success'}))
            .catch(() => swal.fire({title: 'Error en el sistema', icon:'error'}))
        })
    return {
      datosDominios,
      paginated,
      backPage,
      fowardPage,
      begin,
      end,
      deleteDomain,
    };
  },
};
</script>
