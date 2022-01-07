<template >
 
  <v-app>
     <Navbar id="Navbar"/>
    
    
    <v-main >
      <transition name="view">
      <router-view></router-view>
      </transition>
    </v-main>

    <BottomNavbar/>
   
   
  </v-app>


</template>

<script>
//page qui permet un rendu commun
import Navbar from '@/components/Navbar'
import BottomNavbar from './components/BottomNavbar.vue';

export default {
  name: 'App',
  components: {Navbar, BottomNavbar},
  data: () => ({
     name: 'app',
  }),
};
</script>

<style>

Page{
  display:block;
  margin: 0 auto;
}

body{
  margin:0;
  padding:0;
  font-family: Times, serif;

}

#app{
font-family: "Noto Sans JP";
color: Black;
}


.v-main{
      
background-color: white;
}


.view-enter-active, .view-leave-active{ 
transition: opacity 0.4s ease-in-out, transform 0.4s ease-in-out;
}


.view-enter-active{
  transition-delay: 0.4s;
}

 /* when the animation starts*/
.view-enter, .view-leave-to{
opacity: 0;

}

/* when it ends, view-leave (1)-> view-leave(0) to en 0.5s vice versa pour enter */
.view-enter-to, .view-leave{
  opacity: 1;

}
</style>