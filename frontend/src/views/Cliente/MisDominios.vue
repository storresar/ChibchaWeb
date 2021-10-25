<template>
    <div class="bg-gray-300 rounded shadow flex flex-col h-full">
        <div class="bg-gray-200 mb-1 p-3 text-base font-sans text-gray-800 font-bold">LISTA DE MIS DOMINIOS</div>
        <div class="flex flex-col">
            <div class="px-4 py-2">
                <p>Aqui se pueden visualizar sus dominios</p>
            </div>
        </div>
        <suspense>
            <DataTableDominios/>
        </suspense>
        </div>
</template>

<script>
    import DataTableDominios from '../../components/Cliente/DataTableDominios.vue'
    export default{
        components:{DataTableDominios},
        setup(){

        }
    }
</script>
