<?php
    $fruits = array("Pomme", "Cerise", "Banane");
    var_dump($fruits);
?>

<?php
    $age = array("Victor"=>"35", "Dorian"=>"37", "Hugo"=>"24", "Logan"=>"18", "Kevin"=>"19");
    var_dump($age);
?>

<?php
    $age2["Denis"] = "41";
    $age2["Axel"] = "47";
    $age2["Killian"] = "25";
    var_dump($age2);
?>

<?php
    $age3 = array("Loann"=>"41", "Noa"=>"62", "Alexandre"=>"95", "Alexis"=>"15", "Clément"=>"66");
    echo "Alexis a " . $age3["Alexis"] . " ans.";
?>

<?php
    $tableau["Manon"] = 525;
    $tableau["Gabin"] = NULL;
    $tableau["Lounes"] = "Chaussure";
    $tableau["Enola"] = FALSE;

    var_dump($tableau);
?>

<?php
    $tableau2["Matheo"] = 852.52586;
    $tableau2["Matheo"] = TRUE;

    var_dump($tableau2)
?>

<?php
    $tableau3[7] = "Saint agnant";
    $tableau3[7.62] = 49.224;
    $tableau3[1] = 12.241;
    $tableau3[true] = "Salut mon sac walmart";

    var_dump($tableau3);
?>

<?php
    $tab1["Astghik"] = 25;
    $tab1["Erwan"] = 25;
    $tab1["Corentin"] = 25;

    $tab2["Oasis"] = 1;
    $tab2["Tropico"] = 2;
    $tab2["Tessaire"] = 3;

    $tab3 = $tab1 + $tab2;
    var_dump($tab3);

?>