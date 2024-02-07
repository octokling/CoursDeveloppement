<?php

    $jsonTxt = file_get_contents("../concessionnaire.json");
    $table = json_decode($jsonTxt, true);

    foreach($table as $marque => $voitures){
        foreach($voitures as $voiture => $infos){
            echo $infos["modele"] . " : <ul><li>" . $infos["immatriculation"] . "</li><li>" . $infos["kilometrage"] . "km</li></ul> <br>";
        }
    }

?>