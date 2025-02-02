<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)

import { defineEmits } from 'vue'
import loginForm from './loginForm.vue'

const emit = defineEmits(['switchComponent'])

const switchToLogin = () => {
  emit('switchComponent', loginForm)
}
</script>

<template>
    <head>
    <title>Home</title>
    <link rel="stylesheet" type="text/css" href="src/style.css">
</head>
<body>
    <div class="container">
        <div class="card-login">
            <a><img src="../assets/wmu_logo.png" class="circle-logo-wmu"></a>
            <a><img src="../assets/lostnfound_logo.png" class="lostnfound-logo"></a>

            <div class="login-field">
                
                <a class="label-text">Email:</a>
                
                <div class="input-field">
                    <input type="Email"></input>
                </div>

            </div>

            <div class="login-field">

                <div class="form-label">
                    <a class="label-text">Confirm Email:</a>
                </div>

                <div class="input-field">
                    <input type="Email"></input>
                </div>

            </div>

            <div class="login-field">

                <div class="form-label">
                    <a class="label-text">Password:</a>
                </div>

                <div class="input-field">
                    <input type="password"></input>
                </div>

            </div>

            

            <div class="login-button-field">
                <button class="login-button">Sign Up</button>
                <a class="login-text" @click="switchToLogin">Do you have Account?</a>
            </div>
            
            
        </div>
    </div>
</body>

</template>

<style scoped></style>
