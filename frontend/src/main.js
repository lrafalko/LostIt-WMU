import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App).mount('#app')

document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.querySelector(".sidebar");
    const arrowBtn = document.querySelector(".arrow-btn");
    const menuBtn = document.getElementById("menu-btn");

    menuBtn.addEventListener("click", () => {
        side-bar.classList.add("open");
    });

    arrowBtn.addEventListener("click", () => {
        side-bar.classList.remove("open");
    });
});
