<template>
    <div class="md:grid md:grid-cols-4 h-screen">
        <Menu class="md:col-span-1 md:col-start-1 flex"/>
        <router-view class="md:col-span-3 bg-gray-300"></router-view>
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
