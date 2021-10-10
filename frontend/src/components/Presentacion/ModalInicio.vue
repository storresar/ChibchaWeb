<template>
<div class="w-full max-w-xs">
  <form class="bg-red-1000 bg-opacity-90 shadow-md rounded px-8 pt-6 pb-8 mb-4">
    <div class="mb-4">
      <label class="block text-white text-sm font-bold mb-2" for="username">
        Usuario
      </label>
      <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Usuario">
    </div>
    <div class="mb-6">
      <label class="block text-white text-sm font-bold mb-2" for="password">
        Contraseña
      </label>
      <input class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="********">
      <p class="text-white text-xs italic">Entre su contraseña.</p>
    </div>
    <div class="flex items-center justify-start gap-4">
      <button class="bg-white hover:bg-red-50 text-black font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition-colors duration-200 hover:text-white" type="button">
        Inicia sesion
      </button>
     <div class=" flex flex-col-reverse" >
          <a class="inline-block align-baseline font-bold text-sm text-white hover:text-red-50 transition-colors duration-200" href="#">
        Olvide mi clave
      </a>
      <a class="inline-block align-baseline font-bold text-sm text-white hover:text-red-50 transition-colors duration-200" @click="registro">
        Registrarse
      </a>
     </div>
    </div>
  </form>
  <p class="text-center text-gray-500 text-xs">
    &copy;ChibchaWeb derechos reservados
  </p>
</div>
</template>


<script>
import {openModal} from "jenesius-vue-modal";
import ModalRegistro from "./ModalRegistro.vue"
export default {
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    registro(){
      openModal (ModalRegistro)
      this.isMenuOpen = false
    }
  }
};
</script>