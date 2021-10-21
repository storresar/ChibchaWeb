<template>
    <div class="bg-gray-300 rounded shadow flex flex-col h-full">
        <div class="bg-gray-200 mb-1 p-3 text-base font-sans text-gray-800 font-bold">AUDITORIA DEL SISTEMA</div>
        <div class="flex flex-col">
            <suspense>
                <DataTableAuditoria/>
            </suspense>
        </div>
    </div>
</template>

<script>
import DataTableAuditoria from '../../components/Admin/DataTableAuditoria.vue'

export default {
    components: {
        DataTableAuditoria,
    }
}
</script>