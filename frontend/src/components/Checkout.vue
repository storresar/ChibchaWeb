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
      successURL: "http://localhost:8080/client/success/",
      cancelURL: "http://localhost:8080/",
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