<template>
    <div class="md:grid md:grid-cols-4 h-screen">
        <Menu class="md:col-span-1 md:col-start-1 flex"/>
        <transition name="fade">
          <router-view class="md:col-span-3 bg-gray-300"></router-view>
        </transition>
    </div>
</template>

<script>
import Menu from "../components/Admin/Menu.vue";

export default {
  components: {
    Menu,
  },
};
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
