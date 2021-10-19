<template>
    <div class="flex flex-col overflow-x-auto overflow-y-hidden ">
        <div class="">
            <div class="py-2 align-middle inline-block min-w-full lg:px-4">
            <div class=" overflow-hidden border rounded shadow border-gray-200">
                <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Usuario
                    </th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Nombre
                    </th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Correo
                    </th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Rol
                    </th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Es activo
                    </th>
                    
                    <th scope="col" class="relative px-6 py-3">
                        <span class="sr-only">Opciones</span>
                    </th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="user in users" :key="user">
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="flex items-center">
                        <div class="ml-4">
                            <div class="text-sm font-medium text-gray-900">
                            {{user.username}}
                            </div>
                        </div>
                        </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="text-sm text-gray-500">{{user.first_name}} {{user.last_name}}</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="text-sm text-gray-500">{{user.email}}</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        <div v-if="user.rol == 1">Admin</div>
                        <div v-else-if="user.rol == 2">Empleado</div>
                        <div v-else>Cliente</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        <div v-if="user.is_active">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-400" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                            </svg>
                        </div>
                        <div v-else>
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-50" viewBox="0 0 20 20" fill="currentColor">
                               <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                            </svg>
                        </div>
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
                                    <button @click="modifyUser(user)"
                                    class="px-4 py-2 text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none">
                                        Modificar
                                    </button>
                                    <button @click="deleteUser(user.id)"
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
import { computed, inject } from 'vue'
import { useStore } from 'vuex'
import { openModal } from 'jenesius-vue-modal'
import ModalModificar from './ModalModificar.vue'

export default {

    async setup() {
        const swal = inject('$swal')
        const store = useStore()
        await store.dispatch('getUserList')
        const users = computed(() => store.getters.getUsers)

        const deleteUser = (userId => {
            swal.fire({
            title: 'Espere un momento',
            html: 'Estamos eliminando el usuario :3',
            allowOutsideClick: false,
            didOpen: () => {
                swal.showLoading()
                }
            });
            store.dispatch('deleteUser', userId)
            .then(() => swal.fire({title: 'Usuario eliminado', icon:'success'}))
            .catch(() => swal.fire({title: 'Error en el sistema', icon:'error'}))
        })

        const modifyUser = (user => {
            openModal(ModalModificar, {user})

        })
        return {
            users, deleteUser, modifyUser
        }

    },
}
</script>