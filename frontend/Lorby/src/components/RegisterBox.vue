<template lang="">
    <Back @click="$router.push('/login')" class="fixed top-0 right-1/2"/>
    <div class="m-auto" style="width:343px">
        
        <h1 class="text-center " style="font-size:32px">Создать аккаунт</h1>

        <h1 class="text-center " style="font-size:32px">Lorby</h1>

        <div class="text-center">

                <div class="mt-12 mb-4 flex-1">
                <LorbyInput class="mb-2" v-model="email" pholder='Введи адрес почты'/>

                <LorbyInput class="mb-2" v-model="login" pholder='Придумайте логин'/>

                <LorbyInput class="mb-2" v-model="pass1" pholder='Создай пароль'/>

                <LorbyInput class="mb-2" v-model="pass2" pholder='Повтори пароль'/>

                <div class="validation" v-for="error in errors['_value']" :key="error">
                    <p class="text-rose text-center">{{error}}</p>
                </div>

                </div>
                
    
                <LorbyButton @click="register" class="mb-16">Дальше</LorbyButton>
        
        </div>
    </div>
</template>
<script>
import Back from '@/components/Back.vue'
import {ref} from 'vue'
import axios from 'axios'
export default {
    components:{
        Back
    },
    async setup(){
        let email = ref(), login = ref(), pass1 = ref(), pass2 = ref(), errors = ref([])

        function pass_checker(){
            
            if(pass1['_value'] === pass2['_value']){
                errors = []
                console.log('here')
                return true
            } else{
                return false
            }
        }
        async function register(){
            if(pass_checker())
                await axios.post('http://127.0.0.1:8000/api/register', {'login':login['_value'], 'email' : email['_value'], 'password':pass1['_value']})
            else{
                errors['_value'].push("passwords don't match")
                console.log(errors['_value'])
            }
        }
        return {
            login,
            email,
            pass1,
            pass2,
            register,
            errors
        }
    }
}
</script>
<style lang="">
    
</style>