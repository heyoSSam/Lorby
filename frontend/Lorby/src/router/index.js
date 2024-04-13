import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import VerifyView from '@/views/VerifyView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },

    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },

    {
      path: '/verify',
      name: 'verify',
      component: VerifyView
    }
    
  ]
})

export default router
