(function(d,w){
    // Evento para ver si el DOM esta listo
    d.onreadystatechange = function(){
        if(d.readyState === "interactive"){
            // podemos empezar a cargar funciones con el dom
            init();
        }
    }  
    // cambos a validar
    const validacion = {
        nombre:{
            largoMaximo:10,
            largoMinimo:2,
            requerido:true
        },
        password:{
            largoMaximo: 6,
            largoMinimo: 2,
            requerido: true
        },
        edad:{
            minimo:18,
            maximo:70,
            requerido: true
        }
    }
    // eventos a tomar de la pagina
    function init(){
        const formulario = d.querySelector("form");
        formulario.addEventListener("submit",manejarElFormulario)
    }
    // función para manejar el formulario
    function validar(elemento,clase){
        elemento.classList.add(clase);
    }
    function manejarElFormulario(evento){
        evento.preventDefault();
        const inputs = d.querySelectorAll("input[name]");
        let valido = true;
        for(const temp of inputs){
            let atributoName = temp.getAttribute("name");
            let tipo = temp.getAttribute("type");
            let valor = temp.value.trim();
            let vali = validacion[atributoName];
            if(tipo === "number"){
                // Validación para numeros
                if(!Number.isNaN(valor) && valor.length>0){
                    let aNumero = Number.parseInt(valor);
                    if(aNumero < vali.minimo || aNumero>vali.maximo){
                        console.log("Esta fuera de rango el numero");
                        valido = false;
                        validar(temp,"invalido");
                    }
                }else{
                    console.log("No es un numero :c");
                    valido = false;
                    validar(temp,"invalido");
                }
            }
            else{
                // validación para los demas
                if(valor.length>0){
                    if(valor.length < vali.largoMinimo || valor.length > vali.largoMaximo){
                        console.log("El largo esta fuera de rango");
                        valido = false;
                        validar(temp,"invalido");
                    }
                }else{
                    console.log("Campo es requerido");
                    valido = falso;
                    validar(temp,"invalido");
                }
            }
        }
        if(valido){
            console.log("Formulario valido");
        }else{
            console.log("Formulario invalido");
        }

    }
})(document,window);