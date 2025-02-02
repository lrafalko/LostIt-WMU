import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App).mount('#app')

document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.querySelector(".sidebar");
    const arrowBtn = document.querySelector(".arrow-btn");
    const menuBtn = document.querySelector(".menu-btn");

    menuBtn.addEventListener("click", () => {
        sidebar.classList.add("open");
    });

    arrowBtn.addEventListener("click", () => {
        sidebar.classList.remove("open");
    });
});
