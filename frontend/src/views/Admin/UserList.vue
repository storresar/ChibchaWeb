<template>
    <div class="md:m-4 bg-gray-300 rounded shadow flex flex-col">
        <div class="bg-gray-200 mb-1 p-3 text-base font-sans text-gray-800 font-bold">LISTA DE USUARIOS</div>
        <suspense>
            <DataTable/>
        </suspense>
    </div>
</template>

<script>
import DataTable from '../../components/Admin/DataTable.vue'

export default {
    components: {DataTable},

}
</script>