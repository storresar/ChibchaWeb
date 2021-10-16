<template>
  <div>
    <stripe-checkout
      ref="checkoutRef"
      mode="subscription"
      :pk="publishableKey"
      :line-items="lineItems"
      :success-url="successURL"
      :cancel-url="cancelURL"
      @loading="v => loading = v"
    />
    <button @click="submit">Subscribe!</button>
  </div>
</template>

<script>
import { StripeCheckout } from '@vue-stripe/vue-stripe';
export default {
  components: {
    StripeCheckout,
  },
  data () {
    this.publishableKey = 'pk_test_51Jksy9KBVmtCgeqMaCppWGxZAzPzzFLgJcO9pYLYpIDGXDUlY28mySvYzSRjCyttwvvqBq7p7O1IHXIGHR8x2kXl00PeoDcN5T';
    return {
      loading: false,
      lineItems: [
        {
          price: 'price_1Jl1LXKBVmtCgeqMmZod5G3C', // The id of the recurring price you created in your Stripe dashboard
          quantity: 1,
        },
      ],
      successURL: 'http://localhost:3000/',
      cancelURL: 'http://localhost:3000/',
    };
  },
  methods: {
    submit () {
      this.$refs.checkoutRef.redirectToCheckout();
    },
  },
};
</script>