import Vue from "vue"
import VueRouter from "vue-router"
import Home from '@/views/Home'
import About from '@/views/About'
import Dashboard from '@/views/Dashboard'
import Team from '@/views/Team'

Vue.use(VueRouter)

export default new Router({
mode:'history',
base:'process.env.BASE_URL',
routes: [
  {
    path:'/',
    name: 'home',
    component: Home
  },
  {
    path:'/views/about',
    name: 'about',
    component: About //()=> import(/* webpackchunckName: "about" */ './views/About')
  },
  {
    path:'/',
    name: 'dashboard',
    component: Dashboard 
  },
  {
    path:'/',
    name: 'team',
    component: Team 
  },
  
      {
        path:'/views/Cards/Card1',
        name: 'Card1',
        component: Card1
      },
  
 ]
})
