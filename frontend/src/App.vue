<template>
  <div>
    <router-view/>
    <widget-container-modal />
  </div>
  

</template>

<style>
html {
  scroll-behavior: smooth;
}
</style>
<script>
    import {container} from "jenesius-vue-modal";

    export default {
        components: {WidgetContainerModal: container},
        name: "App"
    }
</script>
