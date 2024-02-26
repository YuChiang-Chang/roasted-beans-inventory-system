<template>
  <div id="app">
    <CoffeeBeanForm></CoffeeBeanForm>
    <CoffeeBeansList></CoffeeBeansList>
  </div>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import CoffeeBeanForm from './components/CoffeeBeanForm.vue'
import CoffeeBeansList from './components/CoffeeBeansList.vue';

export default {
  name: 'App',
  components: {
    // HelloWorld,
    CoffeeBeanForm,
    CoffeeBeansList,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
