<template lang="">
    <div class="grid grid-cols-2 h-screen">
        <ImageBox/>

        <LoginBox/>

    </div>
</template>
<script>
import LoginBox from '@/components/LoginBox.vue'
import ImageBox from '@/components/ImageBox.vue'
export default {
    components:{
        LoginBox,
        ImageBox,
    }
}
</script>
<style lang="">
    
</style>