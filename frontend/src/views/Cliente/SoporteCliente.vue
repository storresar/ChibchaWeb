<template>
  <div class="grid justify-self-center">
    <div
      class="font-sans antialiased text-gray-900 leading-normal tracking-wider bg-cover"
    >
      <div
        class="grid justify-self-center max-w-4xl items-center h-auto lg:h-screen flex-wrap mx-auto my-32 lg:my-0"
      >
        <!--Main Col-->
        <div
          id="profile"
          class=" grid justify-self-center w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-lg shadow-2xl bg-white opacity-80 mx-6 lg:mx-0"
        >
          <dl class="responsive-tabs">
            <dt id="formulario" class="active">Solicitud de soporte</dt>
            <dd>
              <div class="container">
                <form @submit.prevent="sendForm">
                  <label for="subject">Descripción del problema</label>
                  <textarea
                    v-model="data.desc_problema"
                    id="subject"
                    required
                    name="subject"
                    placeholder="Escribe aquí tu problema..."
                    style="height:200px"
                  ></textarea>
                  <input type="submit" value="Enviar" />
                </form>
              </div>
            </dd>
            <dt id="historial" class="" @click="tabChanger">
              Historial de tickets
            </dt>
            <dd>
              <suspense>
                <DataTableTickets />
              </suspense>
            </dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-unused-vars */
import DataTableTickets from "../../components/Cliente/DataTableTickets.vue";
import { computed, inject } from "vue";
import { useStore } from "vuex";

export default {
  setup() {
    const store = useStore();
    const swal = inject("$swal");
    const user = store.getters.getUser;
    const data = computed(() => ({
      desc_problema: "",
      nivel: 1,
      desc_solucion: "Sin respuesta.",
      solucionado: false,
      vendedor: null,
      cod_cliente: user.id,
      is_respondido: false,
    }));

    function tabChanger() {
      var $ = function(selector, context) {
        return [].slice.call((context || document).querySelectorAll(selector));
      };
      $(".responsive-tabs").forEach(function(tabs) {
        // Store active tab
        var active = $("dt", tabs)[0];

        // Click handler
        tabs.addEventListener("click", function(e) {
          if (e.target.nodeName.toLowerCase() === "dt") {
            active.classList.remove("active");

            e.target.classList.add("active");
            active = e.target;
          }
        });
      });
    }

    function sendForm() {
      swal.fire({
        title: "Espere un momento",
        html: "Enviando ticket...",
        allowOutsideClick: false,
        didOpen: () => {
          swal.showLoading();
        },
      });

      store
        .dispatch("createTicket", data.value)
        .then(() => {
          swal.fire({ title: "¡Ticket enviado!", icon: "success" });
        })
        .catch(() =>
          swal.fire({ title: "Error en el sistema", icon: "error" })
        );
    }

    return { tabChanger, sendForm, data };
  },
  components: {
    DataTableTickets,
  },
};
</script>

<style>
/* Style inputs with type="text", select elements and textareas */
input[type="text"],
select,
textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
input[type="submit"] {
  background-color: #fa1e4e;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
input[type="submit"]:hover {
  background-color: #7b1fa2;
}

/* Add a background color and some padding around the form */
.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
.responsive-tabs {
}
.responsive-tabs dt {
  padding: 0.5em;
  cursor: pointer;
}
.responsive-tabs dt ~ dt {
  border-top: 1px solid #fa1e4e;
}
.responsive-tabs .active {
  background-color: #fa1e4e;
  color: #fff;
}
.responsive-tabs dd {
  display: none;
  margin-left: 0;
  padding: 0.5em;
}
.responsive-tabs .active + dd {
  display: block;
}
.responsive-tabs img {
  max-width: 100%;
}

@media only screen and (min-width: 868px) {
  .responsive-tabs {
    display: flex;
    flex-wrap: wrap;
  }
  .responsive-tabs dt {
    flex-grow: 1;
    border-bottom: 1px solid #fa1e4e;
    text-align: center;
  }
  .responsive-tabs dt ~ dt {
    border-top: 0;
  }
  .responsive-tabs dd {
    order: 2;
  }
}
</style>
