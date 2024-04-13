<script setup>
import { RouterLink, RouterView } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
</script>

<template>
  <Suspense>
    <template #default>
      <RouterView />
    </template>
  </Suspense>
</template>

