<script setup>
import { ref } from 'vue'
defineProps({
  msg: String,
})

const count = ref(0)

import sideBar from './sideBar.vue';
</script>

<template>
    <body class="main-body">
        <div class="menu-icon-container">
            <a class="menu-icon">☰</a>
        </div>
        <sideBar class="fade-in"/>    
        
    <!-- 메인 콘텐츠 -->
    <div class="main-container">
        
        <!-- 제목 -->
         <div class="logo-container">
            <img src="../assets/wmu_logo.png" alt="" class="lostnfound-logo">
            <img src="../assets/lostnfound_logo.png" alt="" class="lostnfound-logo">
        </div>  

        <!-- 검색창 -->
        <div class="search-bar">
            <input type="text" class="search-input">
            <button class="search-button">SEARCH</button>
        </div>

        <!-- LOST ITEMS -->
        <h2>LOST ITEMS</h2>
        <!-- 아이템 목록 -->
        <div class="list-container">
            <div class="item-container">
                <li class="items-info"></li>
                <li class="items-info"></li>
                <li class="items-info"></li>
                <li class="items-info"></li>
                <li class="items-info"></li>
                <li class="items-info"></li>
            </div>
            
        </div>
        <p class="discribe-text">See More</p>

        <h2>FIND REQUESTS</h2>
        <div class="list-container">
            <div class="item-container">
                <li class="request-info"></li>
                <li class="request-info"></li>
                <li class="request-info"></li>
                <li class="request-info"></li>
                <li class="request-info"></li>
                <li class="request-info"></li>
            </div>
            
        </div>
        <p class="discribe-text">See More</p>
    </div>
    </body>

</template>

<style scoped></style>
