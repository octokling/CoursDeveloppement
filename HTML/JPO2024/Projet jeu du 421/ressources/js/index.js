function changeImage(){
    var image = document.querySelector('[name=img1]');

    var id = Math.floor((Math.random() * 6)+1);
    console.log(id);

    image.src = "./ressources/images/dice" + id + ".png";
}