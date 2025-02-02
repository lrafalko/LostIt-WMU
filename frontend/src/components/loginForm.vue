<script setup>
import { ref } from 'vue'
defineProps({
  msg: String,
})

const count = ref(0)

import { defineEmits } from 'vue'
import signupForm from './signupForm.vue'

const emit = defineEmits(['switchComponent'])

const switchToSignup = () => {
  emit('switchComponent', signupForm)
}

</script>

<template>
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
                    
                    <div class="forget-field">
                        <a class="forget-text" href="/">Forget Your Email?</a>
                    </div>

                </div>

                <div class="login-field">

                    <div class="form-label">
                        <a class="label-text">Password:</a>
                    </div>

                    <div class="input-field">
                        <input type="password"></input>
                    </div>
                    
                    <div class="forget-field">
                        <a class="forget-text" href="/">Forget Your Password?</a>
                    </div>

                </div>

                

                <div class="login-button-field">
                    <button class="login-button">Log in</button>
                    <a class="register-text" @click="switchToSignup">Don't have Account?</a>
                </div>
                
            </div>
        </div>
    </body>
</template>

<style scoped></style>
