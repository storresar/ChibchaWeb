<template>
    <div class="bg-brown-400 w-64 h-32">
        <p class="text-white text-xl">
            Felicidades el pago ha sido completado exitosamente
        </p>
    </div>
</template>

<script>
import { onUnmounted } from 'vue'
export default {
    setup() {
        
        onUnmounted(() => {
            alert(window.location.href.replace('/success', ''));
            window.location.href = window.location.href.replace('/success', '')
        })
    },
}
</script>