<script setup>
import login from './components/login.vue'
</script>

<template>
  <
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap');
@import url('main.js');

html {
  scrollbar-width: none; /* Firefox */
}
body::-webkit-scrollbar {
  display: none; /* Chrome, Safari */
}


body {
    background-color: #e7e7e7;
    font-family: "Rubik", sans-serif;
    margin: 0;
    padding: 0;
}

.card-login{
    display: flex;
    width: 40%;
    margin: 0 auto;
    margin-top: 10%;
    background-color: rgb(255, 255, 255);
    align-items: center;
    flex-direction: column;
    border-radius: 25px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

.circle-logo-wmu{
    max-width: 80px;
    padding: 20px;
}

.lostnfound-logo{
    max-width: 200px;
    padding-bottom: 20px;
}

.login-field a{
  padding-bottom: 5px;
  padding-top: 5px;
}

.label-text{
    font-family: "Rubik", serif;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: normal;
    font-size: 25px;
}

.forget-text{
    font-family: "Rubik", serif;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: italic;
    font-size: 15px;
    padding-bottom: 5px;
    padding-top: 5px;
    text-decoration: none;
    color: black;
    opacity: .75;
}

.login-field{
    display: flex;
    align-items: start;
    flex-direction: column;
    width: 60%;
    margin-left: 20%;
    margin-right: 20%;
    margin-bottom: 30px;
}

.login-field .forget-field{
    width: 100%;
    text-align: right;
}

.login-field input{
    height: 30px;
    width: 100%;
    border-radius: 5px;
}

.input-field{
  width: 100%;
}

.spacer{
    padding-bottom: 10px;
    padding-top: 10px;
}

.login-button-field{
    display: flex;
    align-items: center;
    flex-direction: column;
    width: 100%;
    margin-left: 20%;
    margin-right: 20%;
    margin-bottom: 30px;
}

.login-button{
    font-family: "Rubik", serif;
    font-optical-sizing: auto;
    font-weight: bold;
    font-style: normal;
    font-size: 15px;

    width: 60%;
    height: 45px;
    margin-left: 20%;
    margin-right: 20%;
    border-radius: 5px;
    background-color: #F1C500;
    color: #532E1F;
    font-weight: 300;
    font-size: 20px;
    
}

.register-text{
    font-family: "Rubik", serif;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: italic;
    font-size: 15px;
    padding-bottom: 5px;
    padding-top: 5px;
    text-decoration: none;
    color: black;
    opacity: .75;
}

/* main-page.html */
.search-bar {
  display: flex;
  max-width: 32rem;
  width: 100%;
  align-items: center;
  margin-top: 1rem;
}

.background-bar-left{
  display: flex;
  padding-top: 1rem;
  padding-bottom: 1rem;
  background-color: rgb(234 179 8 / var(--tw-bg-opacity, 1));
  width: 10rem;
  align-items: flex-start;
  justify-content: center;
}

.background-bar-left button{
  font-size: 2rem;
  line-height: 2rem;
  cursor: pointer;
  padding-top: 2rem;
}

.background-bar-right{
  display: flex;
  padding-top: 1rem;
  padding-bottom: 1rem;
  background-color: rgb(234 179 8 / var(--tw-bg-opacity, 1));
  width: 12rem;
  align-items: flex-start;
  justify-content: center;
}

.item-images{
  background-color: rgb(209 213 219 / var(--tw-bg-opacity, 1));
  border-radius: .5rem;
  width: 10rem;
  height: 10rem;
}

/* 메인 페이지 */
.main-body {
  display: flex;
  height: 100vh;
  background-image: url("assets/wmu-login-photo.jpg");
}

.search-bar {
  display: flex;
  max-width: 32rem;
  width: 100%;
  align-items: center;
  margin-top: 1rem;
}

.background-bar-left,
.background-bar-right {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 1rem 0;
  background-color: rgba(234, 179, 8, var(--tw-bg-opacity, 1));
}

.background-bar-right {
  width: 12rem;
}

.item-images {
  width: 10rem;
  height: 10rem;
  background-color: rgba(209, 213, 219, var(--tw-bg-opacity, 1));
  border-radius: 0.5rem;
}

.search-button {
  font-style: italic;
  font-weight: 700;
  padding: 0.5rem 1.5rem;
  background-color: rgba(234, 179, 8, var(--tw-bg-opacity, 1));
  border-radius: 0 9999px 9999px 0;
  cursor: pointer;
}

.main-body h2{
  font-style: italic;
  font-weight: 700;
  font-size: 1.25rem;
  line-height: 1.75rem;
  margin-top: 2rem;

}

.item-container{
  gap: 1rem;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  display: grid;
  margin-top: 1rem;
}

.search-input{
  padding-top: .5rem;
  padding-bottom: .5rem;
  padding-left: 1rem;
  padding-right: 1rem;
  border-color: rgb(156 163 175 / var(--tw-border-opacity, 1));
  border-top-left-radius: 9999px;
  border-bottom-left-radius: 9999px;
  border-width: 1px;
  width: 100%;
}

.main-container{
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity, 1));
  overflow: auto;
  align-items: center;
  flex-direction: column;
  flex: 1 1 0%;
  display: flex;
}

.discribe-text{
  color: rgb(107 114 128 / var(--tw-text-opacity, 1));
  font-style: italic;
  margin-top: 1rem;
}

.side-bar{
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 1rem 0;
  background-color: rgba(234, 179, 8, var(--tw-bg-opacity, 1));
  width: 10rem;
}

.side-bar.open{
  border-radius: 0 3rem 3rem 0;
}

.manu-btn{
  font-size: 3rem;
}
</style>
