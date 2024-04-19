<template>
  <div id="roasted-beans-inventory-system-app">
    <MainNavbar></MainNavbar>
    <div class="dashboard">
      <router-view></router-view>
    </div>
  </div>
  <div id="app">
  </div>
</template>

<script>
import MainNavbar from './components/MainNavbar.vue';

export default {
  name: 'App',
  components: {
    MainNavbar
  },
}
</script>

<style lang="scss">
* {
  box-sizing: border-box;
  color: #322318;
}

body {
    margin: 0;
    min-height: 100vh;
    background: linear-gradient(135deg, #b79471 30%, #875f42 90%);
}
  
input, select, textarea {
  background: rgba(255, 255, 255, 0.1);
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
  }
}

button {
  padding: 10px 20px;
  margin-top: 20px;
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(5px);
  border: 0;
  cursor: pointer;
}

#app {
    display: grid;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}
    
.dashboard {
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
