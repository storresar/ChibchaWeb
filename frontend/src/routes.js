import Home from './views/Home.vue'
import NotFound from './views/NotFound.vue'
import Admin from './views/Admin.vue'
import MainStats from './views/Admin/MainStats.vue'
import UserList from './views/Admin/UserList.vue'
import { createRouter, createWebHistory } from 'vue-router'
import { useStore } from 'vuex'



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
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.meta.authRequired) {
    if (to.meta.adminRequired && window.localStorage.getItem('userRol') == 1) next()
    else if (to.meta.employeeRequired && window.localStorage.getItem('userRol') == 2) next()
    else if (to.meta.clientRequired && window.localStorage.getItem('userRol') == 3) next()
    else next('')
  } else next()
})

export default router;