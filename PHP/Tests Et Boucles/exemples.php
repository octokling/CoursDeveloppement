<?php
    $a = 1;
    $b = 2;
    if($a > $b){ #Si
        echo "a est plus grand que b";
    }else if ($a < $b){ #Sinon si
        echo "a est plus petit que b";
    }else{ #Sinon
        echo "a est égale à b";
    }
?>

<?php 
    $t = date("H"); #Donne la valeur de l'heure
    if ($t < "18"){
        echo "Passez une bonne journée ;)";
    }
?>

<?php
    $i = 1;
    switch($i){
        case 0: #Si i est égale à 0
            echo "i est égale à 0";
            break; #Fin de la case

        case 1:
            echo "i est égale à 1";
            break; #Fin de la case

        case 2:
            echo "i est égale à 2";
            break; #Fin de la case

        default: #Execution par défaut si aucune des case ne correspondent
            echo "i n'as pas été reconnu";
            break; #Fin de la case
    }
?>

<?php
    $x = 1;
    while($x < 5){ #Tant que $x n'est pas égale à 5 (5 non compris dans la bouble)
        echo "La variable x vaut $x\n";
        $x++;
    }
    #Si la condition de while est à true, alors ça continue de tourner
?>

<?php
    $y = 1;

    do{ #Fait ceci
        echo "$y est inférieur à 5\n";
        $y++;
    }
    while($y <= 5); #Tant que y est inférieur ou égale à 5 
    #Fait d'abords une fois, et si la condition de while est à true, alors refait
?>

<?php
    #for(déclaration d'une variable; comparaison pour la boucle; à faire à chaque fin de boucle)
    for($i = 1; $i <= 10; $i++){
        echo "Itération N°$i\n";
    }
    
?>

<?php
    $couleurs = array("Rouge", "Vert", "Bleu", "Jaune");

    foreach($couleurs as $valeur){
        echo "La valeur est $valeur\n";
    }

    $ages = array("Brice"=>"42", "Jean"=>"57", "Bernard"=>"28");

    foreach($ages as $cle => $valeur){
        echo "$cle à $valeur ans !\n";
    }
?>