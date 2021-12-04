{
    let localVariable = "The Coding Team" //only exists within bracket
    var globalVariable = 0; // will exists everywhere on an html page

    globalVariable = "made the int into a string" + 'strings can also be in single quote' //weakly typed
    globalVariable = function (x) { // you can even do this
        console.log(x) //this is how you print
    }

    globalVariable("hello " + "world"); // you add strings normally
    globalVariable(`We are the ${localVariable}`); //can also do this!
}
console.log(localVariable) // variable does not exists anymore :(
console.log(globalVariable) // this exists