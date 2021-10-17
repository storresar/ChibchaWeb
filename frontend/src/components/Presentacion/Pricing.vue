<template>
  <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
    <div class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12">
      <div>
        <p class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-white uppercase rounded-full bg-red-50">
          Nuestros Planes
        </p>
      </div>
      <h2 class="max-w-lg mb-6 font-sans text-3xl font-bold leading-none tracking-tight text-white sm:text-4xl md:mx-auto">
        <span class="relative inline-block">
          <svg viewBox="0 0 52 24" fill="currentColor" class="absolute top-0 left-0 z-0 hidden w-32 -mt-8 -ml-20 text-blue-gray-100 lg:w-32 lg:-ml-28 lg:-mt-10 sm:block">
            <defs>

            </defs>
            <rect fill="url(#7e5e8ff8-1960-4094-a63a-2a0c0f922d69)" width="52" height="24"></rect>
          </svg>
          <span class="relative">Escoge el plan</span>
        </span>
        que mas se te acomode.
      </h2>
      <p class="text-base text-white md:text-lg">
        A continuación podras ver cada caracteristica de nuestros planes
      </p>
    </div>
    <div class="grid max-w-md gap-10 row-gap-5 lg:max-w-screen-lg sm:row-gap-10 lg:grid-cols-3 xl:max-w-screen-lg sm:mx-auto">
      <div class="flex flex-col justify-between p-8 transition-shadow duration-300 bg-white border rounded shadow-sm sm:items-center hover:shadow">
        <div class="text-center">
          <img src="chibchaplata.png" alt="" class="w-56 md:w-60 m-auto" >
          <div class="text-lg font-semibold">Chibcha-Plata</div>
          <div class="flex items-center justify-center mt-2">
            <div class="mr-1 text-5xl font-bold">  $50000  </div><br>
            <div class="text-gray-700">Anual</div>
          </div>
          <div class="mt-2 space-y-3">
            <div class="text-gray-700">$5000 mensual</div>
            <div class="text-gray-700">50/Gb de almacenamiento</div>
            <div class="text-gray-700">Dos sitios web</div>
            <div class="text-gray-700">Dos cuentas de correo</div>
            <div class="text-gray-700">SSL gratis</div>
            <div class="text-gray-700">Dos bases de datos</div>
          </div>
        </div>
        <div>
          <Checkout :priceMonth="chibchaPlataMes" :priceYear="chibchaPlataAnual"/>
        </div>
      </div>
      <div class="relative flex flex-col justify-between p-8 transition-shadow duration-300 bg-white border rounded shadow-sm sm:items-center hover:shadow border-red-50">
        <div class="absolute inset-x-0 top-0 flex justify-center -mt-3">
          <div class="inline-block px-3 py-1 text-xs font-medium tracking-wider text-white uppercase rounded bg-red-50">
            Mas Popular
          </div>
        </div>
        <div class="text-center">
          <img src="chibchaoro.png" alt="" class="w-56 md:w-60 m-auto" >
          <div class="text-lg font-semibold">Chibcha-Oro</div>
          <div class="flex items-center justify-center mt-2">
            <div class="mr-1 text-5xl font-bold">  $100000  </div><br>
            <div class="text-gray-700">Anual</div>
          </div>
          <div class="mt-2 space-y-3">
            <div class="text-gray-700">$10000 mensual</div>
            <div class="text-gray-700">100/Gb de almacenamiento</div>
            <div class="text-gray-700">50 sitios web</div>
            <div class="text-gray-700">100 cuentas de correo</div>
            <div class="text-gray-700">SSL gratis</div>
            <div class="text-gray-700">Cinco bases de datos</div>
          </div>
        </div>
        <div>
          <Checkout :priceMonth="chibchaOroMes" :priceYear="chibchaOroAnual"/>
        </div>
      </div>
      <div class="flex flex-col justify-between p-8 transition-shadow duration-300 bg-white border rounded shadow-sm sm:items-center hover:shadow">
        <div class="text-center">
        <img src="chibchaplatino2.png" alt="" class="w-56 md:w-60 m-auto" >

          <div class="text-lg font-semibold">Platino</div>
          <div class="flex items-center justify-center mt-2">
            <div class="mr-1 text-5xl font-bold">$150000</div>
            <div class="text-gray-700">Anual</div>
          </div>
          <div class="mt-2 space-y-3">
            <div class="text-gray-700">15000 mensual</div>
            <div class="text-gray-700">200Gb de almacenamiento</div>
            <div class="text-gray-700">200 sitios web</div>
            <div class="text-gray-700">Correo ilimitado</div>
            <div class="text-gray-700">SSL gratis</div>
            <div class="text-gray-700">Bases de datos ilimitadas</div>
            <div class="text-gray-700">Copias de seguridad </div>
          </div>
        </div>
        <div>
          <Checkout :priceMonth="chibchaPlataMes" :priceYear="chibchaPlataAnual"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Checkout from '../Checkout.vue'

export default {
  components: {
    Checkout,
  },
  setup() {
    const chibchaPlataMes = 'price_1Jl1LXKBVmtCgeqMmZod5G3C'
    const chibchaPlataAnual = 'price_1JlI5eKBVmtCgeqM7jAxKVBs'
    const chibchaOroMes = 'price_1JlHq4KBVmtCgeqM9F0UZYGJ'
    const chibchaOroAnual = 'price_1JlI7qKBVmtCgeqMQKepGAvT'
    const chibchaPlatinoMes = 'price_1JlI99KBVmtCgeqMcDoKqXZV'
    const chibchaPlatinoAnual = 'price_1JlHsjKBVmtCgeqMefodMW1w'
    return {
      chibchaPlataMes,
      chibchaPlataAnual,
      chibchaOroMes,
      chibchaOroAnual,
      chibchaPlatinoMes,
      chibchaPlatinoAnual,
    }
  },
}
</script>