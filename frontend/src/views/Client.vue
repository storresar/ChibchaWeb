<template>
    <div class="md:grid md:grid-rows-1 md:grid-cols-4 lg:grid-cols-6 h-screen" style="background-image:url('https://source.unsplash.com/1L71sPT5XKc'); background-size:cover">
        <Menu class="md:col-span-1 md:col-start-1 flex"/>
        <suspense>
          <router-view class="md:col-span-3 md:col-start-2 lg:col-start-2 lg:col-span-5"></router-view>
        </suspense>
    </div>
</template>

<script>
import Menu from "../components/Cliente/Menu.vue";

export default {
  components: {
    Menu,
  },
};
</script>