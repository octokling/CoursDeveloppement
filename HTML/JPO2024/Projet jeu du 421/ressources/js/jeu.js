function randomDice() {
    return Math.floor((Math.random() * 6) + 1);
}

function tirerUnNombre() {
    alert(randomDice());
}

function lancerDice() {
    var images = document.querySelectorAll('[class=diceImg]');

    result = [];

    images.forEach(function(image) {

        var face = randomDice();
        result.push(face);
        image.src = "./ressources/images/dice" + face + ".png";

    })

    console.log(result);
}

function lancerDiceChoisi(){
    var checkboxs = document.querySelectorAll('[class=imgCheck]');

    result = [];

    checkboxs.forEach(function(checkbox) {
        if (checkbox.checked) {
            var id = checkbox.id;
            console.log(id);
            var img = checkboxs = document.querySelector('[name=img' + id + ']');

            img.src = "./ressources/images/dice" + randomDice() + ".png";
        }
    })
}