import { createStore } from 'vuex'

const apiBase = 'http://127.0.0.1:8000/api/'

// Create a new store instance.
const store = createStore({
  state () {
    return {
      user : undefined,
      users : undefined,
      tickets : undefined,
      ticket : undefined,
      client : undefined,
    }
  },
  getters: {
    getToken: () => {
      return window.localStorage.getItem('token');
    },
    getUser: state => {
      return state.user;
    },
    getUsers: state => {
      return state.users;
    },
    getTickets: state =>{
      return state.tickets;
    },
    getClient: state =>{
      return state.client;
    },
  },
  mutations: {
    setToken: value => {
      window.localStorage.setItem('token', value)
    },
    loginUser: (state, user) => {
      state.user = user
      window.localStorage.setItem('userRol', user.rol)
      window.localStorage.setItem('userId', user.id)
    },
    loginClient: (state, client) => {
      state.client = client
    },
    logoutUser: (state) => {
      window.localStorage.clear()
      state.user = undefined
    },
    storeUsers: (state, users) => {
      if (state.user) {
        state.users = users.filter(obj => obj.id != state.user.id)
        console.log(state.users);
      } else {
        state.users = users
      }
    },
    storeTickets: (state, tickets) =>{
      state.tickets = tickets
    }
  },
  actions: {
    async retrieveUser(context, id){
      var res = await fetch(`${apiBase}usuarios/${id}/`)
      if (res.ok) {
        var data = await res.json()
        context.commit('loginUser', data)
        return true
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
    },
    async getUserList(context) {
      var res = await fetch(`${apiBase}usuarios/`)
      if (res.ok) {
        const users = await res.json()
        context.commit('storeUsers', users)
      } else throw 'Error del servidor'
    },
    async retrieveClient(context, id) {
      var res = await fetch(`${apiBase}clientes/?cod_usuario=${id}`)
      if (res.ok) {
        const client = await res.json()
        context.commit('loginClient', client[0])
      } else throw 'Error del servidor'
    },
    async createUser(context, user) {
      const {usuario, empleado} = user
      console.log(usuario);
      var res = await fetch(`${apiBase}usuarios/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(usuario)
      })
      if (res.ok) {
        if (context.getters.getToken) context.dispatch('getUserList')
        if (empleado) await context.dispatch('createEmpleado', empleado)
        return 'Exito'
      } else throw 'Error en el registro. Intentelo más tarde'
    },
    async createEmpleado(context, empleado) {
      var res = await fetch(`${apiBase}empleados/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(empleado)
      })
      if (res.ok) {
        return 'Exito'
      } else throw 'Error en el registro. Intentelo más tarde'
    },
    async getTicketsList(context){
      var res = await fetch(`${apiBase}ticket/`)
      if (res.ok) {
        const ticketsList = await res.json()
        context.commit('storeTickets', ticketsList)
      } else throw 'Error del servidor'
    },
    async createTicket(context, ticket){
      var res = await fetch(`${apiBase}ticket/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(ticket)
      })
      if (res.ok) {
        if (context.getters.getToken) context.dispatch('getTicketsList')
        return 'Exito'
      } else throw 'Error en el registro. Intentelo más tarde'
    },
    async updateTicket(context, ticket){
      var res = await fetch(`${apiBase}ticket/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(ticket)
      })
      if (res.ok) {
        if (context.getters.getToken) context.dispatch('getTicketsList')
        return 'Exito'
      } else throw 'Error en el registro. Intentelo más tarde'
    }
  }
})


export default store;