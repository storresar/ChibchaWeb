<template>
  <form class="w-full max-w-md max-h-96 md:max-h-full  bg-red-1000 bg-opacity-90 p-4 rounded-sm overflow-auto" @submit.prevent="sendForm">
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0"  >
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-first-name">
          NOMBRE
        </label>
        <input v-model="datos.firstName"
        @blur="vldate.firstName.$touch"
        class="appearance-none block w-full bg-gray-200 transition-colors duration-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
        :class="vldate.firstName.$error ? 'border-red-500' : 'border-gray-200'"
        type="text" placeholder="Jane">
        <p v-show="vldate.firstName.$error" class="text-red-500 text-xs italic">El nombre debe contener solo caracteres alfabeticos</p>
      </div>
      <div class="w-full md:w-1/2 px-3">
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-last-name">
          APELLIDO
        </label>
        <input v-model="datos.lastName"
        @blur="vldate.lastName.$touch"
        class="appearance-none block w-full bg-gray-200 text-gray-700 border transition-colors duration-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        :class="vldate.lastName.$error ? 'border-red-500' : 'border-gray-200'"
        id="grid-last-name" type="text" placeholder="Doe">
        <p v-show="vldate.lastName.$error" class="text-red-500 text-xs italic">El apellido debe contener solo caracteres alfabeticos</p>
      </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3">
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-password">
          NOMBRE DE USUARIO
        </label>
        <input v-model="datos.username"
        @blur="vldate.username.$touch"
        class="appearance-none block w-full bg-gray-200 border transition-colors duration-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        :class="vldate.username.$error ? 'border-red-500' : 'border-gray-200'"
        type="text"
        :placeholder="datos.firstName.substring(0,1) + datos.lastName">
        <p v-show="vldate.username.$error" class="text-red-50 text-xs italic">El usuario solo puede contener caracteres alfanumericos y debe tener entre 8 a 12 caracteres</p>
      </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3">
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-password">
          CORREO ELECTRONICO
        </label>
        <input v-model="datos.email"
        @blur="vldate.email.$touch"
        :class="vldate.email.$error ? 'border-red-500' : 'border-gray-200'"
        class="appearance-none block w-full bg-gray-200 border transition-colors duration-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        placeholder="jane.doe@company.com">
        <p v-show="vldate.email.$error" class="text-red-50 text-xs italic">Ingrese un correo valido</p>
      </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3">
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-password">
          CONTRASEÑA
        </label>
        <input v-model="datos.password"
        @blur="vldate.password.$touch"
        class="appearance-none block w-full bg-gray-200 border transition-colors duration-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        :class="vldate.password.$error ? 'border-red-500' : 'border-gray-200'"
        id="grid-password" type="password" placeholder="******">
        <p v-show="vldate.password.$error" class="text-red-50 text-xs italic">La clave de contener más de 8 caracteres alfabeticos y al menos 1 numero</p>
      </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3">
        <label class="block uppercase tracking-wide text-white text-xs font-bold mb-2" for="grid-confirm-password">
          CONFIRME LA CONTRASEÑA
        </label>
        <input v-model="datos.confirmPassword"
        @blur="vldate.confirmPassword.$touch"
        :class="vldate.confirmPassword.$error ? 'border-red-500' : 'border-gray-200'"
        class="appearance-none block w-full bg-gray-200 border transition-colors duration-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        id="grid-confirm-password" type="password" placeholder="******">
        <p v-show="vldate.confirmPassword.$error" class="text-red-50 text-xs italic">Las claves no coinciden</p>
      </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6 place-items-center">
      <div class="w-full px-3">
        <button type="submit"
        class="inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-deep-purple-accent-100 hover:text-black focus:shadow-outline focus:outline-none">REGISTRATE</button>
      </div>
    </div>
  </form>
</template>

<script>
import { reactive, computed, inject } from "vue";
import useVuelidate from "@vuelidate/core";
import { required, email, sameAs, minLength, maxLength, alphaNum } from "@vuelidate/validators";
import { useStore } from 'vuex';

export default {
  setup() {

    const swal = inject('$swal')
    const store = useStore()

    const tildeMatch = value => {
      const pattern = new RegExp(/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/)
      return pattern.test(value)
    }

    const hasNum = value => {
        const pattern = new RegExp(/\d/);
        return pattern.test(value)
    }

    const datos = reactive({
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    });

    const passwordRef = computed(() => datos.password)

    const rules = {
      firstName: { required, tildeMatch },
      lastName: { required, tildeMatch },
      username: { required, alphaNum, minLength: minLength(8), maxLength: maxLength(12) },
      email: { required, email: email },
      password: { required, minLength: minLength(8), hasNum, alphaNum},
      confirmPassword: { required, sameAsPassword: sameAs(passwordRef) }
    };

    const vldate = useVuelidate(rules, datos)



    const sendForm = async () => {
      const result = await vldate.value.$validate()
      if (result){
        const user = {
          username: datos.username,
          password: datos.password,
          first_name: datos.firstName,
          last_name: datos.lastName,
          email: datos.email,
          rol: 3,
          date_joined: new Date(),
          intentos_loggeo: 0,
          is_active: true
        }
        swal.fire({
          title: 'Espere un momento',
          html: 'estamos registrandolo en el sistema',
          allowOutsideClick: false,
          didOpen: () => {
            swal.showLoading()
          }
        });
        store.dispatch('createUser', {usuario:user, cliente: {cod_usuario : -1}})
        .then(() => swal.fire({title: 'Exito en registro :3', icon:'success'}))
        .catch(() => swal.fire({title: 'Error en el registo :c', icon:'error'}))
      }
      
    }

    return { datos, vldate, sendForm }
  }
};

</script>

