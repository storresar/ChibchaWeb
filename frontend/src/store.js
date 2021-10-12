import { createStore } from 'vuex'

const apiBase = 'http://127.0.0.1:8000/api/'

const authHeaders = new Headers()
// Create a new store instance.
const store = createStore({
  state () {
    return {
      user : undefined,
    }
  },
  getters: {
    getToken: () => {
      return window.localStorage.getItem('token');
    },
    getUser: (state) => {
      return state.user;
    }
  },
  mutations: {
    setToken: value => {
      window.localStorage.setItem('token', value)
    },
    setUser: (state, user) => {
      state.user = user
      window.localStorage.setItem('userRol', user.rol)
    }
  },
  actions: {
    async retrieveUser(context, id){
      var res = await fetch(`${apiBase}usuarios/${id}/`)
      if (res.ok) {
        var data = await res.json()
        context.commit('setUser', data)
      } else throw 'Error del servidor, intentelo mas tarde'
    },
    async authenticate(context, credentials) {
      const {username, password} = credentials;
      var res = await fetch(`${apiBase}token-auth/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "username": username,
          "password": password,
        })
      })
      if (res.ok) {
        const {token, user_id} = await res.json()
        await context.dispatch('retrieveUser', user_id)
        context.commit('setToken', token)
      } else throw 'Las credenciales son invalidas'
    }
  }
})


export default store;