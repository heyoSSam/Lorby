<template lang="">
    <div class="grid grid-cols-2 h-screen">
        <ImageBox/>
        
        <VerifyBox/>
    </div>
</template>
<script>
import ImageBox from '@/components/ImageBox.vue'
import VerifyBox from '@/components/VerifyBox.vue'
export default {
    components:{
        ImageBox,
        VerifyBox
    }
}
</script>
<style lang="">
    
</style>