1)
<?php
    $a = 85;
    $b = 52;

    $couleur = "vert";

    if($a > $b){
        echo "Bonjour tout le monde\n";
    }

    if($a != $b){
        echo "Bonjour tout le monde\n";
    }

    if($a == $b){
        echo "Oui\n";
    }
    else
    {
        echo "Non\n";
    }

    if($a == $b){
        echo "1\n";
    }
    else if($a > $b){
        echo "2\n";
    }
    else{
        echo "3\n";
    }

    switch($couleur){
        case "rouge":
            echo "Bonjour\n";
            break;
        case "vert":
            echo "bienvenue\n";
            break;
        default:
            echo "Les goûts et mes couleurs, ça ne se discute pas\n";
            break;
    }

    if($couleur == "rouge"){
        echo "Bonjour\n";
    }
    else if($couleur == "vert"){
        echo "bienvenue\n";
    }
    else{
        echo "Les goûts et mes couleurs, ça ne se discute pas\n";
    }
    echo "\n";
?>

2)
<?php
    $a = 0;
    $b = 20;
    $c = 100;
    $d = 1;
    while ($a <= 10){
        echo "$a";
        $a++;
    }

    echo "\n";
    
    while ($b > 6){
        echo "$b";
        $b--;
    }

    echo "\n";

    while($c > 20){
        echo "$c";
        $c = $c / 10;
    }

    echo "\n";

    while($d < 1000){
        echo "$d";
        $d = $d * 100;
    }
    echo "\n";
?>

3)
<?php
    $e = 0;
    $f = 20;
    $g = 100;
    $h = 1;
    do {
        echo "$e";
        $e++;
    }
    while($e <= 10);

    echo "\n";
    
    do{
        echo "$f";
        $f--;
    }
    while ($f > 6);

    echo "\n";

    do{
        echo "$g";
        $g = $g / 10;
    }
    while ($g > 20);

    echo "\n";

    do{
        echo "$h";
        $h = $h * 100;
    }
    while($h < 1000);
    echo "\n";
?>

4)
<?php
    for($i = 1; $i <=10; $i++){
        echo "Résultat: " . $i * 10 . "\n";
    }
    
    for($i = 1; $i <=10; $i++){
        echo "3 x ". $i . " = " . $i * 3 . "\n";
    }
    echo "\n";
?>

5)
<?php
    $jours = array("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche");
    foreach($jours as $jour){
        echo $jour . "\n";
    }

    echo "\n";

    $planetes = array("Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune");
    foreach($planetes as $planete){
        echo $planete . "\n";
    }

    echo "\n";

    $mois = array("Janvier"=>"31","Février"=>"28","Mars"=>"31","Avril"=>"30","Mai"=>"31","Juin"=>"30","Juillet"=>"31","Août"=>"31","Septembre"=>"30","Octobre"=>"31","Novembre"=>"30","Décembre"=>"31");
    foreach($mois as $nameMois => $nbjours){
        echo "Le mois de " . $nameMois . " Contient " . $nbjours . " jours\n";
    }
    
    echo "\n";

    $planetesWithDistances = array("Mercure"=>"57 909 050", "Vénus"=>"108 208 475", "Terre"=>"149 598 023", "Mars"=>"227 939 200", "Jupiter"=>"778 340 821", "Saturne"=>"1 426 666 422", "Uranus"=>"2 870 658 186", "Neptune"=>"4 498 396 441");
    foreach($planetesWithDistances as $namePlanete => $distance){
        echo $namePlanete . " est à " . $distance . " km du Soleil\n";
    }
?>