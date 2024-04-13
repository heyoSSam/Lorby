<template>
    <div>
        <input 
        :placeholder="pholder" 
        :value="modelValue"
        type="text"
        class=""> 
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