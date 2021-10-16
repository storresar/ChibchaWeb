<template>
  <div
    class="sticky top-0 left-0 z-10 px-4 py-5 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8
    rounded-md"
  >
    <div class="flex items-center justify-between">
      <a
        href="#Home"
        aria-label="Chibcha Web"
        title="Chibcha Web"
        class="inline-flex items-center"
      >
        <svg
          class="w-8 text-red-50"
          viewBox="0 0 24 24"
          stroke-linejoin="round"
          stroke-width="2"
          stroke-linecap="round"
          stroke-miterlimit="10"
          stroke="currentColor"
          fill="none"
        >
          <rect x="3" y="1" width="7" height="12"></rect>
          <rect x="3" y="17" width="7" height="6"></rect>
          <rect x="14" y="1" width="7" height="6"></rect>
          <rect x="14" y="11" width="7" height="12"></rect>
        </svg>
        <span
          class="ml-2 text-xl font-bold tracking-wide text-white uppercase"
          >ChibchaWeb</span
        >
      </a>
      <ul class="flex items-center hidden space-x-8 lg:flex">
        
        <li>
          <a
            href="#HeaderInfo"
            aria-label="Our product"
            title="Our product"
            class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50"
            >Inicio</a
          >
        </li>
        <li>
          <a
            href="#Pricing"
            aria-label="Product pricing"
            title="Product pricing"
            class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50"
            >Planes</a
          >
        </li>
        <li>
          <a
            href="#About"
            aria-label="About us"
            title="About us"
            class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50"
            >Quienes somos</a
          >
        </li>
        <li>
          <a
            @click="abrirModal"
            class="inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none"
            aria-label="Sign up"
            title="Sign up"
          >
            Inicia Sesión
          </a>
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
                  <svg
                    class="w-8 text-red-50"
                    viewBox="0 0 24 24"
                    stroke-linejoin="round"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-miterlimit="10"
                    stroke="currentColor"
                    fill="none"
                  >
                    <rect x="3" y="1" width="7" height="12"></rect>
                    <rect x="3" y="17" width="7" height="6"></rect>
                    <rect x="14" y="1" width="7" height="6"></rect>
                    <rect x="14" y="11" width="7" height="12"></rect>
                  </svg>
                  <span
                    class="ml-2 text-xl font-bold tracking-wide text-white uppercase"
                    >CHIBCHA WEB</span
                  >
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
                    class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50"
                    >Inicio</a
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
                    class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-red-50"
                    >Quienes Somos</a
                  >
                </li>
                <li>
                  <a
                    @click="abrirModal"
                  
                    class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-red-50 focus:shadow-outline focus:outline-none"
                    aria-label="Inicia Sesion"
                    title="Inicia Sesion"
                  >
                    Iniciar Sesion
                  </a>
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
export default {
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    abrirModal(){
      openModal (ModalInicio)
      this.isMenuOpen = false
    }
  }
};
</script>