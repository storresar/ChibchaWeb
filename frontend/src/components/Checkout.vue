<template>
  <div>
    <stripe-checkout
      ref="checkoutRef"
      mode="subscription"
      :pk="publishableKey"
      :line-items="lineItems"
      :success-url="successURL"
      :cancel-url="cancelURL"
      @loading="(v) => (loading = v)"
    />
    <button
      @click="submitMonth"
      class="
        inline-flex
        items-center
        justify-center
        w-full
        h-12
        px-6
        mt-6
        font-medium
        tracking-wide
        text-white
        transition
        duration-200
        bg-gray-800
        rounded
        shadow-md
        hover:bg-gray-900
        focus:shadow-outline focus:outline-none
      "
    >
    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
    </svg>
      Comprar plan mensual
    </button>
    <button
      @click="submitYear"
      class="
        inline-flex
        items-center
        justify-center
        w-full
        h-12
        px-6
        mt-6
        font-medium
        tracking-wide
        text-white
        transition
        duration-200
        bg-gray-800
        rounded
        shadow-md
        hover:bg-gray-900
        focus:shadow-outline focus:outline-none
      "
    >
    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
    </svg>
      Comprar plan anual
    </button>
  </div>
</template>

<script>
import { StripeCheckout } from "@vue-stripe/vue-stripe";
import { mapGetters, mapActions } from "vuex";
import {openModal} from "jenesius-vue-modal";
import ModalRegistroCompra from "./Presentacion/ModalRegistroCompra.vue"

export default {
  props: {
    priceMonth: String,
    priceYear: String,
    id: String,
  },
  components: {
    StripeCheckout,
  },
  data() {
    this.publishableKey =
      "pk_test_51Jksy9KBVmtCgeqMaCppWGxZAzPzzFLgJcO9pYLYpIDGXDUlY28mySvYzSRjCyttwvvqBq7p7O1IHXIGHR8x2kXl00PeoDcN5T";
    return {
      loading: false,
      lineItems: [],
      lineItemsM: [
        {
          price: this.priceMonth, // The id of the recurring price you created in your Stripe dashboard
          quantity: 1,
        },
      ],
      lineItemsY: [
        {
          price: this.priceYear, // The id of the recurring price you created in your Stripe dashboard
          quantity: 1,
        },
      ],
      successURL: process.env.NODE_ENV == 'development' ? 
      "http://localhost:8080/client/success/" : 'https://chibcha-web.vercel.app/client/success',
      cancelURL: process.env.NODE_ENV == 'development' ? 
      "http://localhost:8080/" : 'https://chibcha-web.vercel.app/',
    };
  },
  computed: {
    ...mapGetters(["getUser", "getClient"]),
  },
  methods: {
    ...mapActions(['retrieveClient']),
    submitMonth() {
      if (this.getUser) {
        if (this.getUser.rol == 3) {
          localStorage.setItem('SuscriptionId', parseInt(this.id)*2)
          this.retrieveClient(this.getUser.id)
          .then(() => {
            if (!this.getClient.has_plan) {
              this.lineItems = this.lineItemsM;
              this.$refs.checkoutRef.redirectToCheckout();
            } else this.$swal.fire('Error', 'No puede adquirir otro plan. Usted ya esta suscrito a uno ', 'warning')
          }).catch(() => this.$swal.fire('Error', 'Error de autenticacion del cliente', 'error'))
          
        } else this.$swal.fire('Error', 'Debe estar registrado como cliente para adquirir un dominio', 'error')
      } else {
        openModal(ModalRegistroCompra)
      }
    },
    submitYear() {
      if (this.getUser) {
        if (this.getUser.rol == 3) {
          localStorage.setItem('SuscriptionId', (parseInt(this.id)*2)-1)
          this.retrieveClient(this.getUser.id)
          .then(() => {
            if (!this.getClient.has_plan) {
              this.lineItems = this.lineItemsY;
              this.$refs.checkoutRef.redirectToCheckout();
            } else this.$swal.fire('Error', 'No puede adquirir otro plan. Usted ya esta suscrito a uno ', 'warning')
          })
        } else this.$swal.fire('Error', 'Debe estar registrado como cliente para adquirir un dominio', 'error')
      } else {
        openModal(ModalRegistroCompra)
      }
    },
  },
};
</script>