<template>
    <div class="md:m-4 bg-gray-300 rounded shadow flex flex-col h-full">
        <div class="bg-gray-200 mb-1 p-3 text-base font-sans text-gray-800 font-bold">LISTA DE USUARIOS</div>
        <div class="grid grid-rows-6">
            <div>Usuarios Registados</div>

            <suspense>
                <DataTable/>
            </suspense>
        </div>
    </div>
</template>

<script>
import DataTable from '../../components/Admin/DataTable.vue'

export default {
    components: {DataTable},

}
</script>