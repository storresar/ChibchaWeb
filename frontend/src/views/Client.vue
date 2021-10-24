<template>
    <div class="md:grid md:grid-rows-1 md:grid-cols-4 lg:grid-cols-6 h-screen" style="background-image:url('https://source.unsplash.com/1L71sPT5XKc'); background-size:cover">
        <Menu :has_plan="has_plan" class="md:col-span-1 md:col-start-1 flex"/>
        <suspense>
          <router-view class="md:col-span-3 md:col-start-2 lg:col-start-2 lg:col-span-5"></router-view>
        </suspense>
    </div>
</template>

<script>
import Menu from "../components/Cliente/Menu.vue";
import { mapGetters, mapActions } from 'vuex'

export default {
  components: {
    Menu,
  },
  data(){
    return{
      has_plan: false
    }
  },
  computed:{
    ...mapGetters(['getClient'])
  },
  methods: {
    ...mapActions(['retrieveClient'])
  },
  async created() {
    await this.retrieveClient(window.localStorage.getItem('userId'))
    if (this.getClient.has_plan) this.has_plan = true
  }
};
</script>