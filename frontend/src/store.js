import { createStore } from 'vuex'

const apiBase = 'http://127.0.0.1:8000/api/'

function parseToFormData(data) {
  const formData = new FormData();

  for(const name in data) {
    formData.append(name, data[name]);
  }
  return formData
}


// Create a new store instance.
const store = createStore({
  state () {
    return {
      user : undefined,
      users : undefined,
      tickets : undefined,
      ticket : undefined,
      client : undefined,
      employee : undefined,
      audit : undefined,
      datosPlan: undefined,
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
    getEmployee: state =>{
      return state.employee;
    },
    getAudit: state =>{
      return state.audit;
    },
    getDatosPlan: state => {
      console.log(state.datosPlan);
      return state.datosPlan
    }
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
    loginEmployee: (state, employee) => {
      state.employee = employee
    },
    logoutUser: (state) => {
      window.localStorage.clear()
      state.user = undefined
    },
    storeUsers: (state, users) => {
      if (state.user) {
        state.users = users.filter(obj => obj.id != state.user.id)
      } else {
        state.users = users
      }
    },
    storeTickets: (state, tickets) =>{
      state.tickets = tickets
    },
    storeEmployee: (state, employee) => {
      state.employee = employee
    },
    storeAudit: (state, audit) => {
      state.audit = audit
    },
    storeDatosPlan: (state, datosPlan) => {
      state.datosPlan = datosPlan
    },
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
    async getAudit(context) {
      var res = await fetch(`${apiBase}auditoria/`)
      if (res.ok) {
        const audit = await res.json()
        context.commit('storeAudit', audit)
      } else throw 'Error del servidor'
    },
    async retrieveClient(context, id) {
      var res = await fetch(`${apiBase}clientes/?cod_usuario=${id}`)
      if (res.ok) {
        const client = await res.json()
        context.commit('loginClient', client[0])
      } else throw 'Error del servidor'
    },
    async retrieveEmployee(context, id) {
      var res = await fetch(`${apiBase}empleados/?cod_usuario=${id}`)
      if (res.ok) {
        const employee = await res.json()
        context.commit('loginEmployee', employee[0])
      } else throw 'Error del servidor'
    },
    async createUser(context, user) {
      const {usuario, empleado, cliente} = user
      var res = await fetch(`${apiBase}usuarios/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(usuario)
      })
      if (res.ok) {
        if (context.getters.getToken) context.dispatch('getUserList')
        const {id} = await res.json()
        if (empleado){
          empleado.cod_usuario = id
          await context.dispatch('createEmpleado', empleado)
        } else if (cliente) {
          cliente.cod_usuario = id
          await context.dispatch('createCliente', cliente)
        }
        return 'Exito'
      } else throw 'Error en el registro. Intentelo más tarde'
    },
    async deleteUser(context, userID) {
      var res = await fetch(`${apiBase}usuarios/${userID}/`, {
        method: 'DELETE',
      })
      if (res.ok) {
        if (context.getters.getToken) context.dispatch('getUserList')
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
    async createCliente(context, cliente) {
      var res = await fetch(`${apiBase}clientes/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(cliente)
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
          'Content-Type': 'multipart/form-data',
        },
        body: parseToFormData(ticket)
      })
      if (res.ok) {
        if (context.getters.getToken) context.dispatch('getTicketsList')
        return 'Exito'
      } else throw 'Error en el registro. Intentelo más tarde'
    },
    async updateUser(context, data) {
      const {user, employee} = data
      const dataForm = parseToFormData(user)
      dataForm.delete('date_joined')
      var res = await fetch(`${apiBase}usuarios/${user.id}/`, {
        method: 'PATCH',
        body: dataForm
      })
      if (res.ok) {
        if (employee) await context.dispatch('updateEmployee', employee)
        if (user.id == context.getters.getUser.id) await context.dispatch('retrieveUser', user.id)
        await context.dispatch('getUserList')
        return 'Exito'
      } else throw 'Error al editar el usuario. Intentelo más tarde'
    },
    async updateEmployee(context, employee) {
      console.log(employee);
      var res = await fetch(`${apiBase}empleados/${employee.id}/`, {
        method: 'PATCH',
        body: parseToFormData(employee)
      })
      if (res.ok) {
        return 'Exito'
      } else throw 'Error al editar el empleado. Intentelo más tarde'
    },
    async suscribirse(context, data) {
      console.log(data);
      var res = await fetch(`${apiBase}facturacion/`, {
        method: 'POST',
        body: parseToFormData(data)
      })
      if (res.ok) {
        return 'Exito'
      } else throw 'Error al registrar el pago'
    },
    async verificarCaptcha (context, captcha) {
      var res = await fetch(`${apiBase}verificar_captcha/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(captcha)
      })
      if (!res.ok) throw 'Error en el captcha'
    },
    async retrieveDatosPlan (context, clienteId) {
      var res = await fetch(`${apiBase}facturacion/?cod_cliente=${clienteId}`)
      if (res.ok){
        const datos = await res.json()
        context.commit('storeDatosPlan', datos[0])
      }
    },
  }
})
export default store;