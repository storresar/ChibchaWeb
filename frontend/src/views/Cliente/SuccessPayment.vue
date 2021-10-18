<template>
    <div class="bg-brown-400 w-64 h-32">
        <p class="text-white text-xl">
            Felicidades el pago ha sido completado exitosamente
        </p>
    </div>
</template>

<script>
import { onBeforeUnmount } from 'vue'
import { useRouter  } from 'vue-router'
export default {
    setup() {
        const router = useRouter()
        

        onBeforeUnmount(() => {
            router.push('/client')
        })
    },
}
</script>