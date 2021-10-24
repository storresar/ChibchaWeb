<template>
  <div class="flex md:flex-col justify-around md:justify-start bg-gray-900">
    <div v-if="isMenuOpen" class="absolute bg-black top-0 left-0 w-full z-10">
          <div class="p-5 rounded shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div class="inline-flex">
                  <img :src="`${publicPath}chibchaoro.png`" alt="" class="w-16 md:w-16 m-auto" >
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
                   <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                    <p>Lista de usuarios</p>
                  </router-link>
                </li>
                <li>
                  <router-link @click="isMenuOpen = false" to="/admin/stats" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                  <p>Estadisticas</p>
                  </router-link>
                </li>
                <li>
                  <router-link to="/admin/audit" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
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
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                    </svg>
                    Cerrar sesión
                  </button>
                </li>
              </ul>
            </nav>
          </div>
    </div>
    <div class="flex flex-col gap-4 p-5 items-baseline">
      <div class="flex md:flex-col w-full">
          <img :src="`${publicPath}chibchaoro.png`" alt="" class="w-16 md:w-20 m-auto flex justify-center" >
         
          <span class="ml-2 sm:text-xl lg:block lg:text-left font-bold tracking-wide text-white uppercase self-center justify-self-start">
            ChibchaWeb
          </span>
      </div>
      <ul class="hidden md:flex md:flex-col gap-4 mt-4">
        <li class="text-white">GENERAL</li>
        <li>
          <router-link to="/admin/userlist" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
            <p>Lista de usuarios</p>
          </router-link>
        </li>
        <li>
          <router-link to="/admin/stats" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            <p>Estadisticas</p>
          </router-link>
        </li>
        <li>
          <router-link to="/admin/audit" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
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
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
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
import { openModal } from "jenesius-vue-modal";
import { mapMutations } from 'vuex';
import { ModalInicio } from '../Presentacion/ModalInicio.vue'

export default {
  data() {
    return {
      isMenuOpen: false,
      publicPath: process.env.BASE_URL
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