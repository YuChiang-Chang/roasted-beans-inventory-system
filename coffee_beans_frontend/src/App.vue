<template>
  <div id="roasted-beans-inventory-system-app">
    <MainNavbar></MainNavbar>
    <div class="dashboard">
      <router-view></router-view>
    </div>
  </div>
  <div id="app">
    <!-- <nav v-if="isLoggedIn"> -->
      <!-- <router-link to="/">首頁</router-link> -->
      <!-- <router-link to="/login">Login</router-link> -->
      <!-- </nav> -->
    <!-- <CoffeeBeanForm></CoffeeBeanForm> -->
    <!-- <CoffeeBeansList></CoffeeBeansList> -->
  </div>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import MainNavbar from './components/MainNavbar.vue';

export default {
  name: 'App',
  components: {
    // HelloWorld,
    MainNavbar
    // CoffeeBeanForm,
    // CoffeeBeansList,
  },
}
</script>

<style lang="scss">
* {
  box-sizing: border-box;
  color: #322318;
  /* color: white; */
}

body {
    margin: 0;
    // left: 0;
    // right: 0;
    // top: 0;
    // bottom: 0;
    /* font-family: 'Arial', sans-serif; */
    /* background: #f0f0f0; */
    // display: flex;
    // justify-content: center;
    // align-items: center;
    min-height: 100vh;
    // overflow: hidden;
    // width: 100vw;
    background: linear-gradient(135deg, #b79471 30%, #875f42 90%);
    // background-attachment: fixed;
    /* background: linear-gradient(-45deg, #b79471 30%, #875f42 90%); */
    /* background: linear-gradient(45deg, #875f42 30%, #b79471 90%); */
    /* background: #b79471; */
    /* background: #875f42; */
  }
  
  input, select, textarea {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(5px);
    border: none;
    outline: none;
    border-radius: 0.3rem;
    padding: 0.3rem;
    margin: 0.2rem;
    box-shadow: inset 2px 5px 10px rgba(0,0,0,0.15);
    transition: 0.3s ease-in-out;

    &:focus {
      background-color: rgba(255, 255, 255, 0.2);
      transform: scale(1.05);
      box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1),
                  // -13px -13px 20px #aaaaaa;
    }
  }
  
  button {
    padding: 10px 20px;
    margin-top: 20px;
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(5px);
    border: 0;
    cursor: pointer;
    /* border-radius: 10px; */
    /* box-shadow: 5px 5px 25px rgba(0, 0, 0, 0.3), -5x -5px 25px rgba(255, 255, 255, 0.6); */
  }
  
  #app {
      // margin: 0;
      // margin-top: 50vh;
      // left: 0;
      display: grid;
      // flex-direction: column;
      justify-content: center;
      align-items: center;
      // height: 100vh;
      overflow: hidden;
    }
    
    #roasted-beans-inventory-system-app {
      /* font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px; */
      // justify-: center;
      // align-items: center;
      /* background: linear-gradient(-45deg, #875f42 30%, #b79471 90%),rgba(255, 255, 255, 0.1); */
      // margin: auto;
      // margin: 20px auto;
      // margin-top: 10rem;
      // overflow: hidden;
      // position: relative;
      // height: 90vh;
      /* 5px 5px 25px rgba(0, 0, 0, 0.3), -5px -5px 25px rgba(255, 255, 255, 0.6) */
      /* ; */
      /* border: 1px solid rgba(255, 255, 255, 0.3); */
      // &::after {
        //   padding: 10px;
        //   background: rgba(255, 255, 255, 0.1);
        // }
        
      }
      
      .dashboard {
        // width: 90vw;
        padding: 1rem;
        max-width: 1200px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        margin-top: 7rem;
        margin-bottom: 2rem;
        margin-left: 10px;
        margin-right: 10px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        align-items: flex-start;
        transition: 0.3s;
      }
      
</style>
