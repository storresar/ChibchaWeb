<template>
    <div>
      <div class="form__group search-wrapper cf">
    <div class="form__group field">
      <form onsubmit="return false">
      <input type="input" class="form__field" placeholder="Busca tu dominio aquí..." required v-model="input"/>
      <button @click="search">Buscar</button>
      </form>
    </div>

      </div>       
        <div class="flex flex-col overflow-x-auto overflow-y-hidden ">
        <div id="tableMain" style="margin-left:auto;margin-right:auto;display:none;" class="">
            <div class="py-2 align-middle inline-block lg:px-4">
            <div class=" overflow-hidden border rounded shadow border-gray-200">
                <table class="divide-y divide-gray-200">
                <thead class="bg-gray-50">  
                    <tr>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Dominios
                    </th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Disponibilidad
                    </th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Opciones
                    </th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="domain in result_related" :key="domain">
                    <td class="px-6 py-4 whitespace-nowrap">
                        <div class="flex items-center">
                        <div class="ml-4">
                            <div class="text-sm font-medium text-gray-900">
                            {{domain.DomainName}}
                            </div>
                        </div>
                        </div>
                    </td>
                    <td valign="middle" align="center" class="px-6 py-4 whitespace-nowrap text-sm   text-gray-500">
                        <div v-if="domain.DomainAvailability">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5  text-green-400" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                            </svg>
                        </div>
                        <div v-else>
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5  text-red-50" viewBox="0 0 20 20" fill="currentColor">
                               <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                            </svg>
                        </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                      <button @click="selectDomain(domain) " 
                      class="ml-2 inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-red-50 hover:bg-purple-accent-700"
                      :class="domain.DomainAvailability ? '':'bg-gray-600 hover:bg-gray-600'">
                        <div v-if="domain.DomainAvailability">Adquirir dominio</div>
                        <div v-else-if="!domain.DomainAvailability">No disponible</div>
                      </button>             
                    </td>
                    </tr>                        
                </tbody>
                </table>
            </div>         
            </div>
        </div>
        <div id= "loadingbar" style="margin-left:auto;margin-right:auto;display:none;" class="loadingio-spinner-bars-6l5cl3fv6vo"><div class="loadingbar">
       <div></div><div></div><div></div><div></div>
      </div></div> 
    </div>
    </div>
</template>

<script>
  import { ref,inject } from "vue";
  import { useStore } from "vuex";
  
  export default {
    name: "SearchDomain",
    async setup() {
    let input = ref("");
    let result_related = ref();

    // Functions used in template
    // Main button for search domains 
    const search = async () => { 
      
      if (input.value.length === 0){
        console.log('No hay texto.')
      }else{
        showDiv();
        await searchRelatedDomains(input.value);
        hideDiv();
      }
    };
    const store = useStore()
    const swal = inject('$swal')
    await store.dispatch("retrieveClient", store.getters.getUser.id)
    await store.dispatch("retrieveDatosPlan", store.getters.getClient.id)
    const list_distributors = ['NameCheap', 'GoDaddy', 'HostGator', 'Neolo', 'Hostinger', 'Webcolombia']
    console.log(Math.random() * (list_distributors.length - 0) + 0)
    console.log(list_distributors[0])
    const selectDomain = (domain => {
      const dominio = {
          nom_dominio: domain.DomainNoExt,
          link_dominio: domain.DomainName,
          cod_facturacion: store.getters.getDatosPlan.id,
          cod_distribuidor: list_distributors[parseInt(Math.random() * (list_distributors.length - 0) + 0)]
        }
      if(store.getters.getDatosPlan.esta_activo == true){
        console.log(domain.DomainName);
        swal.fire({
            title: 'Espere un momento',
            html: 'estamos registrandolo en el sistema',
            allowOutsideClick: false,
            didOpen: () => {
              swal.showLoading()
            }
          });
          store.dispatch('pushDomain', dominio)
          .then(() => swal.fire({title: 'Exito en registro', icon:'success'}))
          .catch(error => {
            swal.fire({title: 'Error en el registo', icon:'error'})
            console.error(error);
          })
      }else{
        swal.fire({
          title: 'SU PLAN NO ESTÁ ACTIVO',
          icon:'error'
        });
      }
        console.log(dominio)
    })

    async function searchRelatedDomains(domain_name) {
      let api_key_whois = process.env.VUE_APP_WHOIS;
      let list_extensions = [
        "com",
        "net",
        "xyz",
        "art",
        "digital",
        "uk",
        "pro",
        "cc",
        "mx",
        "fm",
        "edu",
        "info",
        "org",
        "es",
      ];
      let shuffled = list_extensions.sort(() => Math.random() - 0.5);
      let input_final = domain_name.split(".");
      
      domain_name = input_final[0];
      let domain_ext = ''
      domain_ext = input_final[1];

      let end = 0;
      if(domain_ext != undefined){
        shuffled.unshift(domain_ext)
        end = 6;
      }else{
        end = 5;
      }

      console.log(input_final)
      console.log(domain_name+' ---- '+domain_ext);

      let result_list = [];
      let domain_name_fixed = "";
      for (let i = 0; i < end; i++) {
        domain_name_fixed = `${domain_name}.${shuffled[i]}`;
        let base_provider = `https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=${api_key_whois}&domainName=${domain_name_fixed}&outputFormat=JSON&da=1`;
        
        const res = await fetch(base_provider);
        // Verify response success and data
        if (res.ok) {
          var data = await res.json();
          console.log(data);
        } else {
          return console.log("Error API respuesta.");
        }

        // Data acquired from API WhoIs
        let domainAvailability = data.WhoisRecord.domainAvailability;
        let domainNameExt = data.WhoisRecord.domainNameExt;

        // Validations 
        if (domainAvailability === "UNAVAILABLE") {
          domainAvailability = false;
        } else if (domainAvailability === "AVAILABLE") {
          domainAvailability = true;
        }

        // Results required from API to a result dictionary
        let result = {
          DomainName: domain_name_fixed,
          DomainNoExt: domain_name_fixed.split(".", 1).toString(),
          DomainAvailability: domainAvailability,
          ExtDomain: domainNameExt,
        };
        result_list.push(result);
      }
      console.log(result_list);
      // Storing dictionary in order to use it outside
      result_related.value = result_list;
      return result_list;
    }

    // functions to hide divs from table and loading bars
    function showDiv() {
      document.getElementById("tableMain").style.display = "none";
      document.getElementById("loadingbar").style.display = "block";
    }
    function hideDiv() {
      document.getElementById("loadingbar").style.display = "none";
      document.getElementById("tableMain").style.display = "block";
    }

      
    // Returning variables to template in order to use it there
    return { result_related, input, search, selectDomain }
  }
}
</script>

<style>



@keyframes loadingbar {
  0% { opacity: 1 }
  50% { opacity: .5 }
  100% { opacity: 1 }
}
.loadingbar div {
  position: absolute;
  width: 26px;
  height: 80px;
  top: 60px;
  animation: loadingbar 1s cubic-bezier(0.5,0,0.5,1) infinite;
}.loadingbar div:nth-child(1) {
  transform: translate(27px,0);
  background: #a00d1e;
  animation-delay: -0.6s;
}.loadingbar div:nth-child(2) {
  transform: translate(67px,0);
  background: #be5960;
  animation-delay: -0.4s;
}.loadingbar div:nth-child(3) {
  transform: translate(107px,0);
  background: #c27a7f;
  animation-delay: -0.2s;
}.loadingbar div:nth-child(4) {
  transform: translate(147px,0);
  background: #d69293;
  animation-delay: -1s;
}
.loadingio-spinner-bars-6l5cl3fv6vo {
  width: 200px;
  height: 200px;
  display: inline-block;
  overflow: hidden;
  background: none;
}
.loadingbar {
  width: 100%;
  height: 100%;
  position: relative;
  transform: translateZ(0) scale(1);
  backface-visibility: hidden;
  transform-origin: 0 0; /* see note above */
}
.loadingbar div { box-sizing: content-box; }
/* generated by https://loading.io/ */

.cf:before, .cf:after{
    content:"";
    display:table;
}
 
.cf:after{
    clear:both;
}
 
.cf{
    zoom:1;
}    

 /* Form wrapper styling */
.search-wrapper {
width: 422px;
margin: 45px auto 50px auto;
box-shadow: 0 1px 1px rgba(0, 0, 0, .4) inset, 0 1px 0 rgba(255, 255, 255, .2);
}
 
/* Form text input */
.search-wrapper input {
width: 350px;
height: 40px;
padding: 10px 5px;
float: left;
font: bold 15px 'lucida sans', 'trebuchet MS', 'Tahoma';
border: 0;
background: #EEE;
border-radius: 3px 0 0 3px;
}
 
.search-wrapper input:focus {
    outline: 0;
    background: #fff;
    box-shadow: 0 0 2px rgba(0,0,0,.8) inset;
}
 
.search-wrapper input::-webkit-input-placeholder {
   color: #999;
   font-weight: normal;
   font-style: italic;
}
 
.search-wrapper input:-moz-placeholder {
    color: #999;
    font-weight: normal;
    font-style: italic;
}
 
.search-wrapper input:-ms-input-placeholder {
    color: #999;
    font-weight: normal;
    font-style: italic;
}    
 
/* Form submit button */
.search-wrapper button {
overflow: visible;
position: relative;
float: right;
border: 0;
padding: 0;
cursor: pointer;
height: 40px;
width: 72px;
font: bold 15px/40px 'lucida sans', 'trebuchet MS', 'Tahoma';
color: white;
text-transform: uppercase;
background: #D83C3C;
border-radius: 0 3px 3px 0;
text-shadow: 0 -1px 0 rgba(0, 0, 0, .3);
}
   
.search-wrapper button:hover{     
    background: #e54040;
}   
   
.search-wrapper button:active,
.search-wrapper button:focus{   
    background: #c42f2f;
    outline: 0;   
}
 
.search-wrapper button:before { /* left arrow */
    content: '';
    position: absolute;
    border-width: 8px 8px 8px 0;
    border-style: solid solid solid none;
    border-color: transparent #d83c3c transparent;
    top: 12px;
    left: -6px;
}
 
.search-wrapper button:hover:before{
    border-right-color: #e54040;
}
 
.search-wrapper button:focus:before,
.search-wrapper button:active:before{
        border-right-color: #c42f2f;
}      
 
.search-wrapper button::-moz-focus-inner { /* remove extra button spacing for Mozilla Firefox */
    border: 0;
    padding: 0;
}    
</style>