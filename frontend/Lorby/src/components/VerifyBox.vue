<template lang="">
    <Back @click="$router.push('/register')" class="fixed top-0 right-1/2"/>
    <div class="m-auto" style="width:343px">
        
        <h1 class="text-center " style="font-size:32px">Введи 4-значный код,</h1>

        <h1 class="text-center " style="font-size:32px">высланный на</h1>

        <h1 class="text-center " style="font-size:32px">example@gmail.com</h1>

        <div class="text-center">
            <form>
                <div class="my-12 mb-4 flex">
                    <LorbyInput v-model="number1" class="mr-2" />

                    <LorbyInput v-model="number2" class="mr-2" />

                    <LorbyInput v-model="number3" class="mr-2" />

                    <LorbyInput v-model="number4" class="mr-2 mb-12" />

                </div>
                
    
                <LorbyButton @click="$router.push('/verify')" class="mb-6">Дальше</LorbyButton>
            </form>

            <p>Выслать код повторно</p>
        </div>
    </div>
</template>
<script>
import Back from '@/components/Back.vue'
import {ref} from 'vue'
export default {
    components:{
        Back
    },

    setup(){
        let number1 = ref(), number2 = ref(), number3 = ref(), number4 = ref()

        return {
            number1,
            number2,
            number3,
            number4
        }
    }
}
</script>
<style lang="">
    
</style>