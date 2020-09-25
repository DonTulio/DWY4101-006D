// alert("Hola Mundo!! con JS");
// let variable = "hola";
// console.log(variable);
// variable = 1234;
// console.log(variable);
// variable = 123.00;
// console.log(variable);
// variable = new Date();
// console.log(variable);
// aqui pasa a ser global
// function hola(){
//     let variableHola = "Soy una variable protegida xD";
//     console.log("Dentro del HOLA", variableHola);
// }
// // hola();
// // console.log(variableHola);
// console.log("Soy un 1");
// console.log("Soy un 2");
// setTimeout(function(){
//     console.log("Soy un 3");
// },3000);
// console.log("Soy un 4");
// console.log("Soy un 5");
// let contador = 0;
// function nombreDeLaFunction(){
//     // alert("Apretado Niah!!");
//     contador = contador + 1; // contador += 1;
//     let nuevoElemento = document.createElement("p");
//     nuevoElemento.innerText = "Elemento número " + contador;

//     const padreDeTodos = document.getElementsByTagName("body")[0];
//     padreDeTodos.appendChild(nuevoElemento);

// }

(function(d,w){
    d.onreadystatechange = function(){
        if(d.readyState === "interactive"){
            iniciar();
        }
    }

    // Datos
    const datos = Array();

    function iniciar(){
        let formulario = d.querySelector("form");
        formulario.addEventListener("submit",funcionFormulario)
    }

    function funcionFormulario(parametro){
        let formulario = d.querySelector("form");
        parametro.preventDefault();
        let nombreIngresado = formulario.nombre.value;
        let edadIngresada = formulario.edad.value;
        let fechaIngresada = formulario.fecha.value;
        let genero = formulario.genero.value;
        const nuevoIngreso = {
            nombre: nombreIngresado,
            edad: edadIngresada,
            fecha: fechaIngresada,
            genero: genero
        }
        datos.push(nuevoIngreso);
        anadirATabla(nuevoIngreso);
    }

    function anadirATabla(objeto){
        const tr = d.createElement("tr");
        // hijos
        const tdNombre = d.createElement("td");
        tdNombre.innerText = objeto.nombre;
        const tdEdad = d.createElement("td");
        tdEdad.innerText = objeto.edad;
        const tdFecha = d.createElement("td");
        tdFecha.innerText = objeto.fecha;
        const tdGenero = d.createElement("td");
        tdGenero.innerText = objeto.genero;
        // Añadir al padre
        tr.appendChild(tdNombre);
        tr.appendChild(tdEdad);
        tr.appendChild(tdFecha);
        tr.appendChild(tdGenero);
        // Insertando en el padre
        const padre = d.querySelector("table tbody");
        padre.appendChild(tr);
    }
})(document,window);
