<template>
  <div class="bg-gray-900" id="Home">
    <Menu/>
    <HeaderInfo/>
    <Pricing id="Pricing"/> 
    <About id="About"/>
  </div>
</template>

<script>
import Pricing from "../components/Presentacion/Pricing.vue";
import Menu from "../components/Presentacion/Menu.vue";
import About from "../components/Presentacion/About.vue";
import HeaderInfo from "../components/Presentacion/HeaderInfo.vue"

export default {
  components: {
    Pricing,
    Menu,
    About,
    HeaderInfo,
  },

  setup() {
    
  },
}
</script>