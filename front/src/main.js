import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import About from '@/views/About'
import Dashboard from '@/views/Dashboard'
import Team from '@/views/Team'

import Card1 from '@/views/Cards/Card1'




Vue.config.productionTip = false;

Vue.use(VueRouter);

Vue.use(vuetify);

const router = new VueRouter({
  routes: [
    {
      path:'/',
      name: 'home',
      component: Home
    },
    {
      path:'/views/about', //gotta be refered at least here to appear
    name: 'about',
    component: About //()=> import(/* webpackchunckName: "about" */ './views/About')
  },
    {
      path:'/views/dashboard',
      name: 'dashboard',
      component: Dashboard 
    },
    {
      path:'/views/Team',
      name: 'team',
      component: Team 
    },
    {
      path:'/views/Cards/Card1',
      name: 'Card1',
      component: Card1
    },
   
   ]
});

new Vue({
  vuetify,
  render: h => h(App),
  router,
}).$mount('#app');

