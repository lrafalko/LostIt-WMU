<script setup>
import { ref } from 'vue'
defineProps({
  msg: String,
})

const count = ref(0)

</script>

<template>
    <body>
    <!-- Sidebar -->
    <div class="side-bar">

        
        <!-- Logo -->
        <div class="logo-container">
            <img src="../assets/wmu-stacked-digital.svg" alt="">
        </div>

        <!-- Profile Picture -->
        <div class=".profile-container">
            <img src="../assets/vue.svg" alt="">
        </div>

        <!-- Name & Status -->
        <div class="text-container">
            <p class="name">NAME</p>
            <p class="status">Status: --</p>
        </div>

        <!-- Expand Button -->
        <button class="expand-button">
            <i class="expand-icon"></i>
        </button>

        <!-- Camera Button -->
        <div class="camera-button">
            <i class="camera-icon"></i>
        </div>

        <!-- Buttons -->
        <div class="flex flex-col w-full space-y-2">
            <button class="custom-button">MY ITEMS</button>
            <button class="custom-button">SETTING</button>
            <button class="custom-button">LOGOUT</button>
        </div>

    </div>

    </body>
</template>

<style scoped></style>
