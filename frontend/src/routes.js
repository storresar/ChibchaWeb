import Home from './views/Home.vue'
import NotFound from './views/NotFound.vue'
import Admin from './views/Admin.vue'
import MainStats from './views/Admin/MainStats.vue'
import UserList from './views/Admin/UserList.vue'

/** @type {import('vue-router').RouterOptions['routes']} */
export const routes = [
  { path: '/', component: Home, meta: { title: 'Home' } },
  { path: '/:path(.*)', component: NotFound },
  {
    path: '/admin',
    component: Admin,
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
