<script setup>
import { ref } from 'vue'
defineProps({
  msg: String,
})

const count = ref(0)

export default {
  name: 'dashboardPage',
  props: {
    username: String,
  },
};
</script>

<template>
    <body class="main-body">

    <!-- 왼쪽 노란색 사이드 -->
    <div class="side-bar">
        <button class="menu-btn" id="menu-btn">☰</button>
    </div>

    <!-- 메인 콘텐츠 -->
    <div class="main-container">
        
        <!-- 제목 -->
        <img src="src/assets/lostnfound_logo.png" alt="" class="lostnfound-logo">

        <!-- 검색창 -->
        <div class="search-bar">
            <input type="text" class="search-input">
            <button class="search-button">SEARCH</button>
        </div>

        <!-- LOST ITEMS -->
        <h2>LOST ITEMS</h2>
        <!-- 아이템 목록 -->
        <div class="item-container">
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
        </div>
        <!-- MORE ITEMS -->
        <p class="discribe-text">MORE ITEMS</p>
        
        <!-- LOST ITEMS -->
        <h2>LOST ITEMS</h2>
        <!-- 아이템 목록 -->
        <div class="item-container">
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
        </div>
        <!-- MORE ITEMS -->
        <p class="discribe-text">MORE ITEMS</p>
        
        <!-- LOST ITEMS -->
        <h2>LOST ITEMS</h2>
        <!-- 아이템 목록 -->
        <div class="item-container">
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
            <div class="item-images"></div>
        </div>
        <!-- MORE ITEMS -->
        <p class="discribe-text">MORE ITEMS</p>
        
    </div>

    <!-- 오른쪽 노란색 사이드 -->
    <div class="background-bar-right"></div>
    <script type="module" src="main.js"></script>

    </body>

</template>

<style scoped></style>
