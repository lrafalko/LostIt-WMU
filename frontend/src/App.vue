<script setup>
import { ref } from 'vue'
import loginForm from './components/loginForm.vue'
import signupForm from './components/signupForm.vue'

const currentComponent = ref(loginForm) // 기본값: Login.vue

const changeComponent = (newComponent) => {
  currentComponent.value = newComponent
}
</script>

<template>
  <div>
    <component :is="currentComponent" @switchComponent="changeComponent" />
  </div>
</template>

<style scoped>
</style>
