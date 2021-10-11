import { createStore } from 'vuex'

const apiBase = 'http://127.0.0.1:8000/api/'
// Create a new store instance.
const store = createStore({
  state () {
    return {
      user : undefined,
    }
  },
  mutations: {
    increment (state) {
      state.count++
    }
  },
  actions: {
    async retrieveUser(id){
      var res = await fetch(`${apiBase}usuarios/${id}/`)
      var data = await res.json()
      console.log(data)
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
      var data = await res.json()
      console.log(data);
    }
  }
})

export default store;