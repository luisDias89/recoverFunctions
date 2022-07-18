var palavra1 ="OLA"
var palavra2="1221t2"
var palavra3="124"

function validaPlaca(stringTeste, nNumeros){
    var valido = false;
    if(!(stringTeste.length > nNumeros) && !isNaN(stringTeste))
    {
        valido=true
    }
    return valido;
 }

 console.log("Is a Number? " + validaPlaca(palavra1, 3));
 console.log("Is a Number? " + validaPlaca(palavra2, 3));
 console.log("Is a Number? " + validaPlaca(palavra3, 3));


    //
    //var pattern = /[a-z]/g;
    //console.log(entradaValor.matches(pattern));
    //console.log(!testeEntrada.substring(0, 3).matches("[A-Z]*"))



    /*if(testeEntrada.length >= 3){
       valido = false;
    }
    if(!testeEntrada.substring(0, 3).matches("[A-Z]*")){
       valido = false;
    }
    if(!testeEntrada.substring(3).matches("[0-9]*")){
       valido = false;
    }*/
 /*
    testeEntrada=String(testeEntrada);
    console.log(testeEntrada)
    valido=false
    
    var pattern = /[a-z,A-Z]/g;
    var result = testeEntrada.match(pattern);
    console.log("Teste de String: " + result)
    */

    // Testa se tem menos de 3 caracteres e se é um numero
