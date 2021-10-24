<template>
  <div
    class="sticky top-0 left-0 z-10 px-4 py-5 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8
    rounded-md" style="background-color:rgba(33, 33, 33, .95)"
  >
    <div class="flex items-center justify-between">
      <a
        href="#Home"
        aria-label="Chibcha Web"
        title="Chibcha Web"
        class="inline-flex items-center"
      >
        <img src="chibchaoro.png" alt="" class="w-16 md:w-16 m-auto" >
        <span v-if="!user" class="ml-2 text-xl font-bold tracking-wide text-white uppercase">ChibchaWeb</span>
        <span v-else class="ml-2 text-xl font-bold tracking-wide text-white uppercase">Bienvenido {{user.username}}</span>
      </a>
      <ul class="flex items-center hidden space-x-8 lg:flex ">
        <li>
          <a
            href="#HeaderInfo"
            aria-label="Our product"
            title="Our product"
            class="flex font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50"
            ><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>Inicio</a
          >
        </li>
        <li>
          <a 
            href="#Pricing"
            aria-label="Product pricing"
            title="Product pricing"
            class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex"
            >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
            Planes
            </a
          >
        </li>
        <li>
          <a
            href="#About"
            aria-label="About us"
            title="About us"
            class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex"
            >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Quienes somos</a
          >
        </li>
        <li>
          <a
            v-if="!user"
            @click="abrirModal"
            class="cursor-pointer inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
            aria-label="Sign up"
            title="Sign up"
          >
            Inicia Sesión
          </a>
          <div v-else class="flex justify gap-4">
            <a
            @click="goToDashBoard"
            class="cursor-pointer inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
            aria-label="Sign up"
            title="Ir al dashboard"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              Dashboard
            </a>
            <a
            @click="logout"
            class="cursor-pointer inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
            aria-label="Sign up"
            title="Ir al dashboard"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              Cerrar Sesión  
            </a>
          </div>
        </li>
      </ul>
      <div class="lg:hidden">
        <button
          aria-label="Open Menu"
          title="Open Menu"
          class="p-2 -mr-1 transition duration-200 rounded focus:outline-none focus:shadow-outline hover:bg-red-50 focus:bg-red-50"
          @click="isMenuOpen = true"
        >
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
        <div v-if="isMenuOpen" class="absolute bg-black top-0 left-0 w-full z-10">
          <div class="p-5 rounded shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div>
                <a
                  aria-label="RoboCol"
                  title="RoboCol"
                  class="inline-flex items-center"
                >
                  <img src="chibchaoro.png" alt="" class="w-16 md:w-16 m-auto" >
                  <span v-if="!user" class="ml-2 text-xl font-bold tracking-wide text-white uppercase">ChibchaWeb</span>
                  <span v-else class="ml-2 text-xl font-bold tracking-wide text-white uppercase">Bienvenido {{user.username}}</span>
                </a>
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
                <li>
                  <a
                    href="#HeaderInfo"
                    @click="isMenuOpen = false"
                    aria-label="Our product"
                    title="Our product"
                    class="flex font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex"
                    >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                    </svg>
                    Inicio</a
                  >
                </li>
                <li>
                  <a
                    href="#Pricing"
                    @click="isMenuOpen = false"
                    aria-label="Product pricing"
                    title="Product pricing"
                    class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50"
                    >Planes</a
                  >
                </li>
                <li>
                  <a
                    href="#About"
                    @click="isMenuOpen = false"
                    aria-label="About us"
                    title="About us"
                    class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50 flex"
                    >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    Quienes Somos</a
                  >
                </li>
                <li>
                  <a
                  v-if="!user"
                  @click="abrirModal"
                  class="cursor-pointer inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
                  aria-label="Sign up"
                  title="Sign up"
                >
                  Inicia Sesión
                </a>
                <div v-else class="flex flex-col justify gap-4 px-10">
                  <a
                  @click="goToDashBoard"
                  class="inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
                  aria-label="Sign up"
                  title="Ir al dashboard"
                  >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                    Dashboard
                  </a>
                  <a
                  @click="logout"
                  class="inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
                  aria-label="Sign up"
                  title="Ir al dashboard"
                  >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                    </svg>
                    Cerrar Sesión
                  </a>
                </div>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {openModal} from "jenesius-vue-modal";
import ModalInicio from "./ModalInicio.vue"
import { useStore } from 'vuex';
import { computed } from 'vue'

export default {
  data() {
    const store = useStore()
    const user = computed(() => store.getters.getUser)
    const goToDashBoard = () => {
      const rol = user.value.rol
      let ruta = ''
      switch (rol) {
        case 1:
          ruta = '/admin/userlist/'
          break
        case 2:
          ruta = '/employee/profile'
          break
        case 3:
          ruta = '/client'
          break
      }
      this.$router.push(ruta)
      window.location.href = ruta
    }

    const logout = () => {
      store.commit('logoutUser')
      this.$router.push('')
    }

    return {
      user,
      isMenuOpen: false,
      goToDashBoard,
      logout
    };
  },
  methods: {
    abrirModal(){
      openModal (ModalInicio)
      this.isMenuOpen = false
    },
  }
};
</script>