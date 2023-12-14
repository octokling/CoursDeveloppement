<?php
    function bonjour(){
        echo "Bonjour\n";
    }
    bonjour();

    function fonction1($a){
        echo $a + 10 . "\n";
    }
    fonction1(9);

    function function2($a, $b){
        echo $a + $b . "\n";
    }
    function2(10, 11);

    function doubleFunc($var){
        if(gettype($var) == "string"){
            echo $var . $var . "\n";
        }else if(gettype($var) != "array"){
            echo $var + $var . "\n";
        }else{
            echo "Ne peux pas avoir de double\n";
        }
    }
    doubleFunc(52);

    function perimetre($rayon){
        echo "Le pérmiètre du cercle de rayon $rayon est de " . 2 * pi() * $rayon . "\n";
    }
    perimetre(20);

    function tableMult($nb){
        for($i = 0; $i <= 10; $i++){
            echo "$nb x $i = " . $nb * $i . "\n";
        }
    }
    tableMult(5);
    
?>