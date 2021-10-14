<template>
    <div class="bg-gray-300 rounded shadow flex flex-col h-full">
        <div class="bg-gray-200 mb-1 p-3 text-base font-sans text-gray-800 font-bold">LISTA DE USUARIOS</div>
        <div class="flex flex-col">
            <div class="px-4 py-2">
                <h4 class="text-xl">Usuarios Registados</h4>
                <div class="flex gap-2">
                    <button class="my-2 inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700">Agregar nuevo usuario</button>
                </div>
            </div>
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