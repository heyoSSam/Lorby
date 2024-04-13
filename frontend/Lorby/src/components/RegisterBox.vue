<template lang="">
    <Back @click="$router.push('/login')" class="fixed top-0 right-1/2"/>
    <div class="m-auto" style="width:343px">
        
        <h1 class="text-center " style="font-size:32px">Создать аккаунт</h1>

        <h1 class="text-center " style="font-size:32px">Lorby</h1>

        <div class="text-center">
            <form>
                <div class="mt-12 mb-4 flex-1">
                <LorbyInput class="mb-2" pholder='Введи адрес почты'/>

                <LorbyInput class="mb-2" pholder='Придумайте логин'/>

                <LorbyInput class="mb-2" pholder='Создай пароль'/>

                <div class="validation">

                </div>

                <LorbyInput class="mb-2" pholder='Повтори пароль'/>

                </div>
                
    
                <LorbyButton @click="$router.push('/verify')" class="mb-16">Дальше</LorbyButton>
            </form>
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
        let email = ref(), login = ref(), pass1 = ref(), pass2 = ref()

        return {
            redirect,
            login,
            email,
            pass1,
            pass2
        }
    }
}
</script>
<style lang="">
    
</style>