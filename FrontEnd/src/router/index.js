import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('../views/test.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/xuanke',
    name: 'xuanke',
    component: () => import('../views/XuanKe.vue')
  },
  {
    path: '/luntan',
    name: 'luntan',
    component: () => import('../views/LunTan.vue')
  },
  {
    path: '/rili',
    name: 'rili',
    component: () => import('../views/RiLi.vue')
  },
  {
    path: '/fudao',
    name: 'fudao',
    component: () => import('../views/FuDao/FuDao.vue')
  },
  {
    path: '/pingjiao',
    name: 'pingjiao',
    component: () => import('../views/PingJiao.vue')
  },
  {
    path: '/fudao/teacherlist',
    name: 'teacherlist',
    component: () => import('../views/FuDao/TeacherList.vue')
  },
  {
    path: '/fudao/appointmentlist',
    name: 'appointmentlist',
    component: () => import('../views/FuDao/AppointmentList.vue')
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
