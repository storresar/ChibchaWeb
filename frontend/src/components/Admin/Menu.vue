<template>
  <div class="flex md:flex-col justify-around md:justify-start bg-gray-900">
    <div v-if="isMenuOpen" class="absolute bg-black top-0 left-0 w-full z-10">
          <div class="p-5 rounded shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div class="inline-flex">
                  <img src="chibchaoro.png" alt="" class="w-16 md:w-16 m-auto" >
                  <span
                    class="ml-2 text-xl font-bold tracking-wide text-gray-800 uppercase"
                    >ChibchaWeb</span
                  >
              </div>
              <div>
                <button
                  aria-label="Close Menu"
                  title="Close Menu"
                  class="p-2 -mt-2 -mr-2 transition duration-200 rounded hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
                  @click="isMenuOpen = false"
                >
                  <svg class="w-5 text-gray-600" viewBox="0 0 24 24">
                    <path
                      fill="currentColor"
                      d="M19.7,4.3c-0.4-0.4-1-0.4-1.4,0L12,10.6L5.7,4.3c-0.4-0.4-1-0.4-1.4,0s-0.4,1,0,1.4l6.3,6.3l-6.3,6.3 c-0.4,0.4-0.4,1,0,1.4C4.5,19.9,4.7,20,5,20s0.5-0.1,0.7-0.3l6.3-6.3l6.3,6.3c0.2,0.2,0.5,0.3,0.7,0.3s0.5-0.1,0.7-0.3 c0.4-0.4,0.4-1,0-1.4L13.4,12l6.3-6.3C20.1,5.3,20.1,4.7,19.7,4.3z"
                    ></path>
                  </svg>
                </button>
              </div>
            </div>
            <nav>
              <ul class="space-y-4">
                <li class="text-white">GENERAL</li>
                <li>
                  <router-link @click="isMenuOpen = false" to="/admin/userlist" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 self-center" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
                    </svg>
                    <p>Lista de usuarios</p>
                  </router-link>
                </li>
                <li>
                  <router-link @click="isMenuOpen = false" to="/admin/stats" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 self-center" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z" />
                    <path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z" />
                  </svg>
                  <p>Estadisticas</p>
                  </router-link>
                </li>
                <li>
                  <router-link to="/admin/audit" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                    </svg>
                    <p>Auditoria</p>
                  </router-link>
                </li>
                <li class="text-white">CUENTA</li>
                <li>
                  <router-link to="/admin/profile" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
                    </svg>
                    <p>Ver perfil</p>
                  </router-link>
                </li>
                <li>
                  <button @click="logout"
                  class="ml-2 inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700">
                    Cerrar sesión
                  </button>
                </li>
              </ul>
            </nav>
          </div>
    </div>
    <div class="flex flex-col gap-4 p-5 items-start">
      <div class="flex">
          <img src="chibchaoro.png" alt="" class="w-16 md:w-16 m-auto" >
         
        <span class="ml-2 sm:text-xl md:text-base font-bold tracking-wide text-white uppercase self-center">
          ChibchaWeb
        </span>
      </div>
      <ul class="hidden md:flex md:flex-col gap-4 mt-4">
        <li class="text-white">GENERAL</li>
        <li>
          <router-link to="/admin/userlist" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 self-center" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
            </svg>
            <p>Lista de usuarios</p>
          </router-link>
        </li>
        <li>
          <router-link to="/admin/stats" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 self-center" viewBox="0 0 20 20" fill="currentColor">
              <path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z" />
              <path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z" />
            </svg>
            <p>Estadisticas</p>
          </router-link>
        </li>
        <li>
          <router-link to="/admin/audit" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
            </svg>
            <p>Auditoria</p>
          </router-link>
        </li>
        <li class="text-white">CUENTA</li>
        <li>
          <router-link to="/admin/profile" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
            </svg>
            <p>Ver perfil</p>
          </router-link>
        </li>
        <li>
          <button @click="logout"
          class="ml-2 inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700">
            Cerrar sesión
          </button>
        </li>
      </ul>
    </div>
    <div class="md:hidden grid place-self-center">
      <button
      aria-label="Close Menu"
      title="Close Menu"
      class="p-2 -mr-1 transition duration-200 rounded focus:outline-none focus:shadow-outline hover:bg-red-50 focus:bg-red-50"
      @click="isMenuOpen = true">
        <svg class="w-5 text-gray-600" viewBox="0 0 24 24">
          <path
            fill="currentColor"
            d="M23,13H1c-0.6,0-1-0.4-1-1s0.4-1,1-1h22c0.6,0,1,0.4,1,1S23.6,13,23,13z"
          ></path>
          <path
            fill="currentColor"
            d="M23,6H1C0.4,6,0,5.6,0,5s0.4-1,1-1h22c0.6,0,1,0.4,1,1S23.6,6,23,6z"
          ></path>
          <path
            fill="currentColor"
            d="M23,20H1c-0.6,0-1-0.4-1-1s0.4-1,1-1h22c0.6,0,1,0.4,1,1S23.6,20,23,20z"
          ></path>
        </svg>
      </button>

    </div>

    
  </div>
</template>

<script>
import {openModal} from "jenesius-vue-modal";
import { mapMutations } from 'vuex';
import {ModalInicio } from '../Presentacion/ModalInicio.vue'

export default {
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    ...mapMutations(['logoutUser']),
    abrirModal(){
      openModal (ModalInicio)
      this.isMenuOpen = false
    },
    logout(){
      this.logoutUser()
      this.$router.push("/")
    }
  }
};
</script>