import Home from './views/Home.vue'
import NotFound from './views/NotFound.vue'
import Admin from './views/Admin.vue'
import MainStats from './views/Admin/MainStats.vue'
import UserList from './views/Admin/UserList.vue'
import Audit from './views/Admin/Audit.vue'
import Client from './views/Client.vue'
import Plan from './views/Cliente/Plan.vue'
import Search from './views/Cliente/Search.vue'
import SuccessPayment from './views/Cliente/SuccessPayment.vue'
import Profile from './views/Profile.vue'
import GestionTickets from './views/Empleado/GestionTickets.vue'
import SoporteCliente from './views/Cliente/SoporteCliente.vue'
import Empleado from './views/Empleado.vue'
import MisDominios from './views/Cliente/MisDominios.vue'

import { createRouter, createWebHistory } from 'vue-router'
import {useModalRouter} from "jenesius-vue-modal";


/** @type {import('vue-router').RouterOptions['routes']} */
const routes = [
  { path: '/', component: Home, meta: { title: 'Home' } },
  { path: '/:path(.*)', component: NotFound },
  {
    path: '/admin',
    component: Admin,
    meta: {authRequired: true, adminRequired : true},
    children: [
      {
        path: 'stats',
        component: MainStats,
      },
      {
        path: 'userlist',
        component: UserList,
      },
      {
        path: 'audit',
        component: Audit,
      },
      {
        path: 'profile',
        component: Profile,
      },
    ]
  },
  {
    path: '/client',
    component: Client,
    meta: {authRequired: true, clientRequired : true},
    children: [
      {
        path: 'plan',
        component: Plan,
      },
      {
        path: 'success',
        component: SuccessPayment,
      },
      {
        path: 'search',
        component: Search,
      },
      {
        path: 'profile',
        component: Profile,
      },
      {
        path: 'soporte',
        component: SoporteCliente,
      },
      {
        path: 'myDomains',
        component: MisDominios,
      },
    ]
  },
  {
    path: '/empleado',
    component: Empleado,
    meta: {authRequired: true, employeeRequired : true},  
    children: [
      {
        path: 'profile',
        component: Profile,
      },
      {
        path: 'gestionTickets',
        component: GestionTickets,
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

useModalRouter.init(router);

router.beforeEach((to, from, next) => {
  if (to.meta.authRequired) {
    if (to.meta.adminRequired && window.localStorage.getItem('userRol') == 1) next()
    else if (to.meta.employeeRequired && window.localStorage.getItem('userRol') == 2) next()
    else if (to.meta.clientRequired && window.localStorage.getItem('userRol') == 3) next()
    else next('')
  } else next()
})

export default router;