<template>
  <div>
    <div class="form-wrapper cf">
      <input
        id="message"
        placeholder="Busca aquí tu dominio..."
        required
        v-model="message"
      />
      <button @click="search">Buscar</button>
    </div>
    <div id="welcomeDiv" style="display:none;">
      <center>
        <ag-grid-vue
          style="width: 700px; height: 110px; cellStyle: {textAlign: 'center'}"
          class="ag-theme-material"
          :columnDefs="columnDefs"
          :rowData="[result_final]"
        >
        </ag-grid-vue>
        <ag-grid-vue
          id="relatedDomains"
          style="width: 700px; height: 250px; cellStyle: {textAlign: 'center'}"
          class="ag-theme-material"
          :columnDefs="columnRelated"
          :rowData="related_domains"
          headerHeight="5"
        >
        </ag-grid-vue>
      </center>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";
import ButtonCellRenderer from "./buttonCellRenderer.js";
import { AgGridVue } from "ag-grid-vue3";

export default {
  name: "SearchDomain",
  setup() {
    const message = ref("");
    let result_final = ref();
    let related_domains = ref();

    const search = async () => { 
      await searchDomainInfo(message.value);
      await generateRelatedDomains(message.value);
      showDiv();
    };

    const cellClassRules2 = {
      "cell-available": (params) => params.value === "Disponible",
      "cell-unavailable": (params) => params.value === "No disponible",
    };

    let columnDefs = [
      {
        headerName: "Dominio",
        field: "DomainName",
      },
      {
        headerName: "Disponibilidad",
        field: "DomainAvailability",
        cellClassRules: cellClassRules2,
      },
      {
        headerName: "Acción",
        cellRendererFramework: "buttonCellRenderer",
        minWidth: 175,
      },
    ];

    let columnRelated = [
      {
        headerName: "",
        field: "DomainName",
      },
      {
        headerName: "",
        field: "DomainAvailability",
        cellClassRules: cellClassRules2,
      },
      {
        headerName: "",
        cellRendererFramework: "buttonCellRenderer",
        minWidth: 175,
      },
    ];

    /////////////// functions //////////////////
    async function searchDomainInfo(domain_name) {
      let api_key_whois = "at_0F3Q7V5e2DGzIFTo9YDZj6iVZb2TF";
      let base_provider = `https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=${api_key_whois}&domainName=${domain_name}&outputFormat=JSON&da=1`;

      const response_raw_whois = await fetch(base_provider);
      if (response_raw_whois.ok) {
        var data = await response_raw_whois.json();
        console.log(data);
      } else {
        return console.log("Error API respuesta.");
      }

      let createdDate = data.WhoisRecord.audit.createdDate;
      let domainAvailability = data.WhoisRecord.domainAvailability;
      let domainNameExt = data.WhoisRecord.domainNameExt;
      let registrarName = data.WhoisRecord.registrarName;
      let expiresDate = data.WhoisRecord.registryData.expiresDate;

      if (expiresDate !== undefined) {
        if (expiresDate.includes("sponsoring")) {
          expiresDate = undefined;
        }
      }

      if (domainAvailability === "UNAVAILABLE") {
        domainAvailability = "No disponible";
      } else if (domainAvailability === "AVAILABLE") {
        domainAvailability = "Disponible";
      }

      let price = "";

      if (domainAvailability === "No disponible") {
        price = "No disponible";
      } else {
        price = parseFloat(generateRandomPriceUSD(1, 100)) + " USD";
      }

      var result = {
        DomainName: domain_name,
        DomainNoExt: domain_name.split(".", 1).toString(),
        DomainAvailability: domainAvailability,
        CompanyName: registrarName,
        DateRegister: createdDate,
        ExpiresDate: expiresDate,
        ExtDomain: domainNameExt,
        Price: price,
      };

      result_final.value = result;
    }

    async function generateRelatedDomains(domain_name) {
      let api_key_whois = "at_0F3Q7V5e2DGzIFTo9YDZj6iVZb2TF";
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
      ];
      const shuffled = list_extensions.sort(() => Math.random() - 0.5);
      domain_name = domain_name.split(".", 1).toString();
      let result_list = [];
      let domain_name_fixed = "";
      for (let i = 0; i < 5; i++) {
        domain_name_fixed = `${domain_name}.${shuffled[i]}`;
        let base_provider = `https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=${api_key_whois}&domainName=${domain_name_fixed}&outputFormat=JSON&da=1`;
        const response_raw_whois = await fetch(base_provider);
        if (response_raw_whois.ok) {
          var data = await response_raw_whois.json();
          console.log(data);
        } else {
          return console.log("Error API respuesta.");
        }

        let domainAvailability = data.WhoisRecord.domainAvailability;
        let domainNameExt = data.WhoisRecord.domainNameExt;

        if (domainAvailability === "UNAVAILABLE") {
          domainAvailability = "No disponible";
        } else if (domainAvailability === "AVAILABLE") {
          domainAvailability = "Disponible";
        }
        let price = "";
        if (domainAvailability === "No disponible") {
          price = "No disponible";
        } else {
          price = parseFloat(generateRandomPriceUSD(1, 100)) + " USD";
        }

        let result = {
          DomainName: domain_name_fixed,
          DomainNoExt: domain_name_fixed.split(".", 1).toString(),
          DomainAvailability: domainAvailability,
          ExtDomain: domainNameExt,
          Price: price,
        };

        result_list.push(result);
      }

      console.log(result_list);
      related_domains.value = result_list;
      return result_list;
    }

    function generateRandomPriceUSD(min, max) {
      return Math.floor(Math.random() * (max - min + 1) + min) - 0.1 + "9";
    }

    return {
      message,
      search,
      result_final,
      related_domains,
      columnDefs,
      columnRelated,
    };

    function showDiv() {
      document.getElementById("welcomeDiv").style.display = "block";
    }
  },
  components: {
    AgGridVue,
    buttonCellRenderer: ButtonCellRenderer,
  },
};
</script>

<style>

.cell-unavailable {
  background-color: lightcoral;
}

.cell-available {
  background-color: lightgreen;
}

.ag-header-cell-label {
  justify-content: center;
  font-weight: bold;
}

.ag-row .ag-cell {
  display: flex;
  justify-content: center; /* align horizontal */
  align-items: center;
}

html CSSResult Skip Results iframe body {
  background: #555
    url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAB9JREFUeNpi/P//PwM6YGLAAuCCmpqacC2MRGsHCDAA+fIHfeQbO8kAAAAASUVORK5CYII=);
  font: 13px "Lucida sans", Arial, Helvetica;
  color: #eee;
  text-align: center;
}

a {
  color: #ccc;
}

/*-------------------------------------*/

.cf:before,
.cf:after {
  content: "";
  display: table;
}

.cf:after {
  clear: both;
}

.cf {
  zoom: 1;
}

/*-------------------------------------*/

.form-wrapper {
  width: 470px;
  padding: 15px;
  margin: 30px auto 50px auto;
  background: #444;
  background: rgba(0, 0, 0, 0.2);
  -moz-border-radius: 10px;
  -webkit-border-radius: 10px;
  border-radius: 10px;
  -moz-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.4) inset,
    0 1px 0 rgba(255, 255, 255, 0.2);
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.4) inset,
    0 1px 0 rgba(255, 255, 255, 0.2);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.4) inset,
    0 1px 0 rgba(255, 255, 255, 0.2);
}

.form-wrapper input {
  width: 330px;
  height: 40px;
  padding: 10px 5px;
  float: left;
  font: bold 15px "lucida sans", "trebuchet MS", "Tahoma";
  border: 0;
  background: #eee;
  -moz-border-radius: 3px 0 0 3px;
  -webkit-border-radius: 3px 0 0 3px;
  border-radius: 3px 0 0 3px;
}

.form-wrapper input:focus {
  outline: 0;
  background: #fff;
  -moz-box-shadow: 0 0 2px rgba(0, 0, 0, 0.8) inset;
  -webkit-box-shadow: 0 0 2px rgba(0, 0, 0, 0.8) inset;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.8) inset;
}

.form-wrapper input::-webkit-input-placeholder {
  color: #999;
  font-weight: normal;
  font-style: italic;
}

.form-wrapper input:-moz-placeholder {
  color: #999;
  font-weight: normal;
  font-style: italic;
}

.form-wrapper input:-ms-input-placeholder {
  color: #999;
  font-weight: normal;
  font-style: italic;
}

.form-wrapper button {
  overflow: visible;
  position: relative;
  float: right;
  border: 0;
  padding: 0;
  cursor: pointer;
  height: 40px;
  width: 110px;
  font: bold 15px/40px "lucida sans", "trebuchet MS", "Tahoma";
  color: #fff;
  text-transform: uppercase;
  background: #fa1e4e;
  -moz-border-radius: 0 3px 3px 0;
  -webkit-border-radius: 0 3px 3px 0;
  border-radius: 0 3px 3px 0;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.3);
}

.form-wrapper button:hover {
  background: #e54040;
}

.form-wrapper button:active,
.form-wrapper button:focus {
  background: #c42f2f;
}

.form-wrapper button:before {
  content: "";
  position: absolute;
  border-width: 8px 8px 8px 0;
  border-style: solid solid solid none;
  border-color: transparent #fa1e4e transparent;
  top: 12px;
  left: -6px;
}

.form-wrapper button:hover:before {
  border-right-color: #fa1e4e;
}

.form-wrapper button:focus:before {
  border-right-color: #fa1e4e;
}

.form-wrapper button::-moz-focus-inner {
  border: 0;
  padding: 0;
}
.byline p {
  text-align: center;
  color: #c6c6c6;
  font: bold 18px Arial, Helvetica, Sans-serif;
  text-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
}

.byline p a {
  color: #fa1e4e;
  text-decoration: none;
}
</style>
