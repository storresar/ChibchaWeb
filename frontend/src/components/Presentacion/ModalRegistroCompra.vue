<template>
<div class="w-full max-w-xs">
  <form class="bg-red-1000 bg-opacity-90 shadow-md rounded px-8 pt-6 pb-8 mb-4">
    <div class="mb-4">
      <label class="block text-white text-sm font-bold mb-2" for="username">
        Usuario
      </label>
      <input
      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
      id="username" type="text" placeholder="Usuario" v-model="username">
    </div>
    <div class="mb-6">
      <label class="block text-white text-sm font-bold mb-2" for="password">
        Contraseña
      </label>
      <input
      class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
      id="password" type="password" placeholder="********" v-model="password">
      <p class="text-white text-xs italic">Entre su contraseña.</p>
    </div>
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
    <div class="flex items-center justify-start gap-4">
      <button
      class="bg-white hover:bg-red-50 text-black font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition-colors duration-200 hover:text-white"
      type="button" @click="login">
        Inicia sesion
      </button>
    </div>
  </form>
  <p class="text-center text-gray-500 text-xs">
    &copy;ChibchaWeb derechos reservados
  </p>
</div>
</template>


<script>
import { closeModal } from "jenesius-vue-modal";
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
    ...mapActions(["authenticate"]),
    login() {
      if (this.captchaVerified) this.authenticate({username: this.username, password: this.password})
      .then(() => {
        this.$swal.fire('Inicio de sesión exitoso!')
        closeModal()
      })
    },
    recaptchaVerified(response) {
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