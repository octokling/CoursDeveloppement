<?php
    $texte = "Coucou je suis une variable\n";

    function fonction1(){
        global $texte;
        echo $texte;
        $texte = "Rebonjour\n";

        static $a = 0;
        echo $a . "\n";
        $a++;
    }
    fonction1();
    fonction1();
    echo $texte;
?>
