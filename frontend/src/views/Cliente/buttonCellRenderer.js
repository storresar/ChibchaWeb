export default {
    template: `
        <span>
              <span>{{ cellValue }}</span>
              <button id="buttonSelect" @click="buttonClicked()">Seleccionar</button>
          </span>
    `,
    setup(props) {
        const cellValue = props.params.valueFormatted ? props.params.valueFormatted : props.params.value;
        const target_copy = Object.assign({}, props.params.data);

        const buttonClicked = () => {
            alert(`¡Valores obtenidos!`);
            console.log(target_copy)
        } 

        // props.params contains the cell & row information and is made available to this component at creation time
        // see ICellRendererParams for more details
        return {
            cellValue,
            buttonClicked
        }
    }
};