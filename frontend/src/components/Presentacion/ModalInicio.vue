<template>
<div class="w-full max-w-xs">
  <form class="bg-red-1000 bg-opacity-90 shadow-md rounded px-8 pt-6 pb-8 mb-4">
    <div class="mb-2">
      <label class="block text-white text-sm font-bold" for="username">
        Usuario
      </label>
      <input
      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
      id="username" type="text" placeholder="Usuario" v-model="username">
    </div>
    <div class="mb-4">
      <label class="block text-white text-sm font-bold mb-1" for="password">
        Contraseña
      </label>
      <input
      class="shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
      id="password" type="password" placeholder="********" v-model="password">
    </div>
    <div class="flex justify-start mt-7">
      <vue-recaptcha siteKey="6Ld3Y-wcAAAAAJOH0wFvfqG53ob76ilO7B2TQHMZ"
      class="transform scale-[.84] -translate-x-6 -translate-y-3"
      size="normal"
      theme="light"
      :tabindex="0"
      @verify="recaptchaVerified"
      @expire="recaptchaExpired"
      @fail="recaptchaFailed"
      ref="vueRecaptcha">
      </vue-recaptcha>
    </div>
    <div class="flex items-center justify-start gap-4">
      <button
      class="bg-white hover:bg-red-50 text-black font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition-colors duration-200 hover:text-white"
      type="button" @click="login">
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
import { openModal, closeModal } from "jenesius-vue-modal";
import ModalRegistro from "./ModalRegistro.vue";
import { mapActions, mapGetters } from "vuex"
import vueRecaptcha from 'vue3-recaptcha2';

export default {
  components: {
    vueRecaptcha,
  },
  data() {
    return {
      captchaVerified: false,
      isMenuOpen: false,
      username: '',
      password: '',
    };
  },
  computed: {
    ...mapGetters(['getUser'])
  },
  methods: {
    ...mapActions(["retrieveUser", "authenticate", 'verificarCaptcha']),
    registro(){
      openModal(ModalRegistro)
      this.isMenuOpen = false
    },
    login() {
      if (this.captchaVerified) this.authenticate({username: this.username, password: this.password})
      .then(() => {
        closeModal()
        const rol = this.getUser.rol
        let ruta = ''
        switch (rol) {
          case 1:
            ruta = '/admin/userlist/'
            break
          case 2:
            ruta = '/empleado'
            break
          case 3:
            ruta = '/client'
            break
        }
        this.$router.push(ruta)
        window.location.href = ruta
      })
      .catch((err) => this.$swal.fire('Error', err.toString(), 'warning'))
    },
    recaptchaVerified(response) {
      console.log(response);
      this.verificarCaptcha({'g-recaptcha-response': response})
      .then(() => this.captchaVerified = true)
      .catch(() => {
        this.$swal('Error', 'Reintente la verificacion de captcha', 'error')
        this.recaptchaExpired()
      })
    },
    recaptchaExpired() {
      this.$refs.vueRecaptcha.reset();
    },
    recaptchaFailed() {
    },
  }
};
</script>