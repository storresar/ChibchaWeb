<template>
    <div class="bg-brown-400 w-64 h-32">
        <p class="text-white text-xl">
            Felicidades el pago ha sido completado exitosamente
        </p>
    </div>
</template>

<script>
import { useStore } from 'vuex'

export default {
    setup() {

        const store = useStore()

        var cliente, facturacion;

        console.log(store.getters.getUser.id)

        store.dispatch('retrieveClient', store.getters.getUser.id)
        .then(() => {
            cliente = store.getters.getClient;

            console.log(store.getters.getClient);


            facturacion = {
                valor_total: 0,
                dominios_disponibles: 0,
                cod_cliente: cliente.id,
                fecha_cancelacion: new Date(),
                cod_plan: localStorage.getItem('SuscriptionId')
            }

            store.dispatch('suscribirse', facturacion)
            .then(() => this.$swal('Exito!', 'Se ha suscrito exitosamente a nuestros servicios :3', 'success'))
            .catch((error) => {
                console.error(error)
                this.$swal('Error', error.toString(), 'error')
            })

        })

        
    },
}
</script>