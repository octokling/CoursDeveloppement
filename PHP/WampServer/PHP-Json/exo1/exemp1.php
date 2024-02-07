<?php
    $fichier = file_get_contents("../concessionnaire.json");
    $tableau = json_decode($fichier, true);
    print_r($tableau);
    
?>