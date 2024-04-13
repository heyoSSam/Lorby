<template lang="">
    <div class="grid grid-cols-2 h-screen">
        <ImageBox/>
        
        <RegisterBox/>
    </div>
</template>
<script>
import ImageBox from '@/components/ImageBox.vue'
import RegisterBox from '@/components/RegisterBox.vue'
export default {
    components:{
        ImageBox,
        RegisterBox
    }
}
</script>
<style lang="">
    
</style>