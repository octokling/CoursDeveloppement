<?php

    $jsonTxt = file_get_contents("../concessionnaire.json");
    $table = json_decode($jsonTxt, true);

    $marque = "Peugeot";
    $idTable = 1;

    echo "$marque " . $table[$marque][$idTable]["modele"] . " : <ul>";
    foreach($table[$marque][$idTable] as $cle => $info){
        printInfo($cle, $info);
    }

    function printInfo($key, $value){
        if(gettype($value) == "array"){
            echo "<li>$key:</li>";
            echo "<ul>";
            foreach($value as $cleArray => $infoArray){
                printInfo($cleArray, $infoArray);
            }
            echo "</ul>";
        }else{
            echo "
                <li>$key: " . $value . "</li>
            ";
        }
    }
    echo "</ul><br>";

?>