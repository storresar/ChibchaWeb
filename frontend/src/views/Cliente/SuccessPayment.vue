<template>
    <div class="max-w-md md:h-96 py-4 px-8 bg-white shadow-lg rounded-lg my-20 m-auto">
        <div class="flex justify-center md:justify-end -mt-16">
            <img class="w-24 h-24 object-cover rounded-full border-none border-indigo-500" :src="`${publicPath}chibchaoro.png`">
        </div>
        <div>
            <h2 class="text-gray-800 text-3xl font-semibold">Felicidades</h2>
            <p class="mt-2 text-gray-600">Usted se ha suscrito exitosamente a nuestros servicios</p>
        </div>
        <img :src="`${publicPath}success.gif`" alt="" srcset="" class="my-4">
        <div class="flex justify-end mt-4">
            <p href="#" class="text-xl font-medium text-indigo-500">Equipo de ChichaWeb</p>
        </div>
    </div>
</template>

<script>
import { useStore } from 'vuex'
import { inject } from 'vue'
import { useRouter } from 'vue-router'

export default {
    setup() {
        const swal = inject('$swal')
        const store = useStore()
        const publicPath = process.env.BASE_URL
        const router = useRouter()
        var cliente, facturacion;

       
        router.push({path: '/client'})
        location.reload

        store.dispatch('retrieveUser', window.localStorage.getItem('userId'))
        .then(() => {
            store.dispatch('retrieveClient', store.getters.getUser.id)
            .then(() => {
                cliente = store.getters.getClient;

                facturacion = {
                    valor_total: 0,
                    dominios_disponibles: 0,
                    cod_cliente: cliente.id,
                    fecha_cancelacion: new Date(),
                    cod_plan: parseInt(localStorage.getItem('SuscriptionId'))
                }

                store.dispatch('suscribirse', facturacion)
                .then(() => {
                    swal('Exito!', 'Se ha suscrito exitosamente a nuestros servicios :3', 'success')
                    .then(() => {
                        router.push({path: '/client'})
                        location.reload
                    })
                })
                .catch((error) => {
                    console.error(error)
                })
                
            })
        })

        return {publicPath}
        
    },
}
</script>