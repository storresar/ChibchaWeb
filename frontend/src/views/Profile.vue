<template>
    <div>
        <div class="font-sans antialiased text-gray-900 leading-normal tracking-wider bg-cover" >
        <div class="max-w-4xl flex items-center h-auto lg:h-screen flex-wrap mx-auto my-32 lg:my-0">
            
            <!--Main Col-->
            <div id="profile" class="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0">
            
                <div class="p-4 md:p-12 text-center lg:text-left">
                    <!-- Image for mobile view-->
                    <div class="block lg:hidden rounded-full shadow-xl mx-auto -mt-16 h-48 w-48 bg-cover bg-center" style="background-image: url('https://source.unsplash.com/MP0IUfwrn0A')"></div>
                    
                    <h1 class="text-3xl font-bold pt-8 lg:pt-0">{{user.first_name}} {{user.last_name}}</h1>
                    <div class="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-red-500 opacity-25"></div>
                    <div class="pt-4 text-lg text-gray-600" v-if="user.rol === 3">Cliente</div>
                    <div class="pt-4 text-gray-600" v-else-if="user.rol === 2">Empleado</div>
                    <div class="pt-4 text-gray-600" v-else-if="user.rol === 1">Admin</div>
                    <p class="pt-4 text-gray-600 flex items-center justify-center lg:justify-start"><svg class="h-4  fill-current text-red-50 pr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14.5 14.5"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/></svg>{{user.username}}</p>
                    <p class="pt-2 text-gray-600 text-xs lg:text-sm flex items-center justify-center lg:justify-start"><svg class="h-4 fill-current text-red-50 pr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 20a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm7.75-8a8.01 8.01 0 0 0 0-4h-3.82a28.81 28.81 0 0 1 0 4h3.82zm-.82 2h-3.22a14.44 14.44 0 0 1-.95 3.51A8.03 8.03 0 0 0 16.93 14zm-8.85-2h3.84a24.61 24.61 0 0 0 0-4H8.08a24.61 24.61 0 0 0 0 4zm.25 2c.41 2.4 1.13 4 1.67 4s1.26-1.6 1.67-4H8.33zm-6.08-2h3.82a28.81 28.81 0 0 1 0-4H2.25a8.01 8.01 0 0 0 0 4zm.82 2a8.03 8.03 0 0 0 4.17 3.51c-.42-.96-.74-2.16-.95-3.51H3.07zm13.86-8a8.03 8.03 0 0 0-4.17-3.51c.42.96.74 2.16.95 3.51h3.22zm-8.6 0h3.34c-.41-2.4-1.13-4-1.67-4S8.74 3.6 8.33 6zM3.07 6h3.22c.2-1.35.53-2.55.95-3.51A8.03 8.03 0 0 0 3.07 6z"/></svg>{{user.email}}</p>
                    <p class="pt-2 text-gray-600 text-xs lg:text-sm flex items-center justify-center lg:justify-start"><svg class="h-4 text-red-50 pr-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>{{date}}</p>
                    <p class="pt-8 text-sm"></p>

                    <div class="pt-12 pb-8">
                        <button @click="modifyUser(user)" class="bg-red-50 hover:bg-deep-purple-accent-100 text-white font-bold py-2 px-4 rounded-full">
                        Modificar perfil
                        </button> 
                    </div>
                </div>

            </div>
            <!--Img Col-->
            <div class="w-full lg:w-2/5">
                <!-- Big profile image for side bar (desktop) -->
                <img src="https://source.unsplash.com/MP0IUfwrn0A" class="rounded-none lg:rounded-lg shadow-2xl hidden lg:block">
                <!-- Image from: http://unsplash.com/photos/MP0IUfwrn0A -->
            </div>
        </div>
        </div>
    </div>
</template>

<script>

import { useStore } from 'vuex';
import { openModal } from 'jenesius-vue-modal'
import ModalModificar from '../components/Admin/ModalModificar.vue'

export default{
    name: "Profile",
    setup() {
        
        const store = useStore();
        const user = store.getters.getUser;
        const date = user.date_joined.slice(0,10);

        const modifyUser = (user => {
            if (user.rol === 2) {
                store.dispatch('retrieveEmployee', user.id)
                .then(() => {
                    console.log(user);
                    openModal(ModalModificar, {user, employee: store.getters.getEmployee})
                })
            } else openModal(ModalModificar, {user})

        })

        return { user, date, modifyUser }
    },
}
</script>

<style>

</style>