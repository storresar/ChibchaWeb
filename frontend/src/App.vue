<template>
  <div>
    <router-view v-slot="{ Component }">
          <transition name="fade">
            <component :is="Component" />
          </transition>
        </router-view>
    <widget-container-modal />
  </div>
  

</template>
<style>
html {
  scroll-behavior: smooth;
}
</style>
<style scoped>

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
<script>
    import {container} from "jenesius-vue-modal";
    import { useStore } from "vuex";

    export default {
        components: {WidgetContainerModal: container},
        name: "App",

        setup() {
          if (window.localStorage.getItem('token') && window.localStorage.getItem('userId')) {
            const store = useStore()
            store.dispatch("retrieveUser", window.localStorage.getItem('userId'))
          }
        }
    }
</script>
