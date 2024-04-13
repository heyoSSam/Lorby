<template >
        <div class="m-auto" style="width:343px">
            <h1 class="text-center " style="font-size:32px">Вэлком бэк!</h1>
    
            <div class="text-center">
                <form>
                    <div class="my-12 flex-1">
                    <LorbyInput v-model="login" class="mb-2" pholder='Введи логин'/>
    
                    <LorbyInput v-model="pass" pholder='Введи пароль'/>
    
                    </div>
                    
                    <LorbyButton class="mb-16">Войти</LorbyButton>
    
                    <a href="/register">
                        <p class="text-center">
                            У меня еще нет аккаунта
                        </p>
                    </a>
                </form>
            </div>
        </div>
</template>
<script>
import {ref} from 'vue'
export default {
    setup(){
        let login = ref(), pass = ref()

        return {
            login,
            pass
        }
    }
}
</script>
<style lang="">
    
</style>