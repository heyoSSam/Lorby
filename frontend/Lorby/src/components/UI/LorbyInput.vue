<template>
    <div>
        <input 
        :placeholder="pholder" 
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)" 
        type="text"
        class="py-3 px-4 rounded-xl bg-silver w-full border-none focus:outline-gray-200"> 
    </div>
</template>
<script>
export default {
    name : 'LorbyInput',
    props: {
        modelValue : String,
        pholder : String
    }
}
</script>
<style>
    
</style>