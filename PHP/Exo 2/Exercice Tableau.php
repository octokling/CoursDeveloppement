1)
<?php
    #Exercice 1 :
    $fibonacci = array(0,1,1,2,3,5,8,13,21,34,55,89,144,233,377);
    rsort($fibonacci);
    var_dump($fibonacci);
?>

2)
<?php
    #Exercice 2 :
    $mounth = array("Janvier"=>"31","Février"=>"28","Mars"=>"31","Avril"=>"30","Mai"=>"31","Juin"=>"30","Juillet"=>"31","Août"=>"31","Septembre"=>"30","Octobre"=>"31","Novembre"=>"30","Décembre"=>"31");
    
    echo "Les clées ont le nom des mois de l'année.\n";
    echo "Les valeurs sont les nombre de jours dans le mois\n\n";

    echo "Janvier\t: " . $mounth["Janvier"] . "\n";
    echo "Février\t: " . $mounth["Février"] . "\n";
    echo "Mars\t: " . $mounth["Mars"] . "\n";
    echo "Avril\t: " . $mounth["Avril"] . "\n";
    echo "Mai\t: " . $mounth["Mai"] . "\n";
    echo "Juin\t: " . $mounth["Juin"] . "\n";
    echo "Juillet\t: " . $mounth["Juillet"] . "\n";
    echo "Août\t: " . $mounth["Août"] . "\n";
    echo "Sept\t: " . $mounth["Septembre"] . "\n";
    echo "Octobre\t: " . $mounth["Octobre"] . "\n";
    echo "Novem\t: " . $mounth["Novembre"] . "\n";
    echo "Décem\t: " . $mounth["Décembre"] . "\n";

?>

3)
<?php
    #Exercice 3 :

    $tableau = array(
        array("Nom"=>"Denis", "Prénom"=>"Roger", "Mail"=>"Denis.roger@serveur.io", "Téléphone"=>"0102030450"),
        array("Nom"=>"Fred", "Prénom"=>"Pasteur", "Mail"=>"Fred.pasteur@serveur.io", "Téléphone"=>"0102030558"),
        array("Nom"=>"Maris", "Prénom"=>"Stuart", "Mail"=>"Marie.stuart@serveur.io", "Téléphone"=>"0102030608")
    );
    
    echo $tableau[0]["Mail"];
?>