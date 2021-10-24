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
                  <router-link to="/client/plan" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
                    </svg>
                    <p>Mi plan</p>
                  </router-link>
                </li>
                <li>
                  <router-link @click="isMenuOpen = false" to="/client/search" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 21h7a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v11m0 5l4.879-4.879m0 0a3 3 0 104.243-4.242 3 3 0 00-4.243 4.242z" />
                    </svg>
                    <p>Buscar dominios</p>
                  </router-link>
                </li>
              <li>
                <router-link to="/client/soporte" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <p>Soporte a cliente</p>
                </router-link>
              </li>
                <li class="text-white">CUENTA</li>
                <li>
                  <router-link to="/client/profile" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
                    </svg>
                    <p>Ver perfil</p>
                  </router-link>
                </li>
                <li>
                  <router-link @click="isMenuOpen = false" to="/client/myDomains" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
                  </svg>
                  <p>Mis dominios</p>
                  </router-link>
                </li>
                <div class="flex flex-col gap-4 px-4">
                  <li>
                    <button @click="logout"
                    class="ml-2 inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                      </svg>
                      Cerrar sesión
                    </button>
                  </li>
                  <li>
                    <router-link to="/"
                    class="flex ml-2 text-center inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                      </svg>
                      Página principal
                    </router-link>
                  </li>
                </div>
              </ul>
            </nav>
          </div>
    </div>
    <div class="flex flex-col gap-4 p-5 items-start">
      <div class="flex md:flex-col w-full">
          <img :src="`${publicPath}chibchaoro.png`" alt="" class="w-16 md:w-20 m-auto flex justify-center" >
         
          <span class="ml-2 sm:text-xl lg:block lg:text-left font-bold tracking-wide text-white uppercase self-center justify-self-start">
            ChibchaWeb
          </span>
      </div>
      <ul class="hidden md:flex md:flex-col gap-4 mt-4">
        <li class="text-white">GENERAL</li>
        <li>
          <router-link to="/client/plan" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
            <p>Mi plan</p>
          </router-link>
        </li>
        <li>
          <router-link @click="isMenuOpen = false" to="/client/search" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 21h7a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v11m0 5l4.879-4.879m0 0a3 3 0 104.243-4.242 3 3 0 00-4.243 4.242z" />
            </svg>
            <p>Buscar dominios</p>
          </router-link>
        </li>
          <li>
            <router-link to="/client/soporte" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
                  <p>Soporte a cliente</p>
                </router-link> 
          </li>
        <li class="text-white">CUENTA</li>
        <li>
          <router-link to="/client/profile" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
            </svg>
            <p>Ver perfil</p>
          </router-link>
        </li>
        <li>
          <router-link @click="isMenuOpen = false" to="/client/myDomains" class="ml-2 font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
          </svg>
          <p>Mis dominios</p>
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
        <li>
          <router-link to="/"
          class="flex ml-2 text-center inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            Página principal
          </router-link>
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
      publicPath: process.env.BASE_URL,
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
      this.$router.go(0)
    }
  }
};
</script>