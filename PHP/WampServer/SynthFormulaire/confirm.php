<?php
    $name = $_POST["name"];
    $mail = $_POST["mail"];
    $usrChoice = [];

    $nbOfActivities = 0;
    $tarif = 0;
    $reduc = 0;

    foreach($_POST as $id => $choice){
        if($id != "name" && $id != "mail"){
            $usrChoice[$id] = $choice;
        }
    }

    if(array_key_exists("CIH", $usrChoice)){
        $nbOfActivities++;
        $tarif += 800;
    }
    if(array_key_exists("CC", $usrChoice)){
        $nbOfActivities++;
        $tarif += 450;
    }
    if(array_key_exists("AP", $usrChoice)){
        $nbOfActivities++;
        $tarif += 400;
    }
    if(array_key_exists("AEMC", $usrChoice)){
        $nbOfActivities++;
        $tarif += 350;
    }

    switch($nbOfActivities){
        case 2:
            $reduc = 5;
            break;
        case 3:
            $reduc = 15;
            break;
        case 4:
            $reduc = 25;
            break;
    }

    $tarif = $tarif - ($tarif * $reduc / 100);

    if($usrChoice["age"] == "0"){
        $reduc = 20;
    }else if($usrChoice["age"] == "1"){
        $reduc = 15;
    }

    $tarif = $tarif - ($tarif * $reduc / 100);

?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">    
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Confirmation</title>
    </head>
    <body>
        <style>
            body{
                background-color: #5ABDF1;
                font-size: 25px;
                color: #fff;
            }

            span#user{
                color: #000077;
            }

            span#prix{
                color: #FF0000;
            }

            div#middle{
                text-align: center;
            }
        </style>
        <?php
            echo "<div id='middle'><p>Merci <span id='user'>$name</span> pour votre intérêt, vous avez choisi : </p></div> <ul>";

            if(array_key_exists("CIH", $usrChoice)){
                echo "<li>
                    Les cours individuels :<br>
                    <div id='middle'>
                        Les programmes sportifs sont sur mesure. Les exercices et les conseils dépendent donc directement de vos
                        attentes. L’important est d’utiliser la pratique sportive pour optimiser votre bien-être physique et mental. Lors du
                        premier cours de coaching, vous discutez avec votre coach de votre but, par exemple :
                    </div>
                    <ul>
                        <li>Reprendre une activité sportive en toute sécurité</li>
                        <li>Retrouver une bonne condition physique</li>
                        <li>Débuter un renforcement musculaire global ou ciblé</li>
                        <li>Bénéficier d’une préparation physique</li>
                        <li>Améliorer votre hygiène de vie et votre santé</li>
                        <li>Favoriser une perte de poids</li>
                    </ul>
                </li><br>";
            }

            if(array_key_exists("CC", $usrChoice)){
                echo "<li>
                    Les cours collectifs :<br>
                    <div id='middle'>
                        Les cours collectifs proposent des activités cardio <b>chorégraphiée et dynamique</b> combinant plusieurs exercices
                        et mouvements. Chacun peut y aller à son rythme : les débutants commenceront par des mouvements simples et
                        adaptés à leur niveau ; les confirmés pourront quant à eux donner le meilleur d’eux-mêmes. Tous les muscles
                        sont sollicités. Au-delà de <b>brûler des calories</b> avec ces efforts intenses, vous renforcez votre système cardiovasculaire et cardio-respiratoire. Défoulement garanti !
                    </div>
                    </li><br>";
            }

            if(array_key_exists("AP", $usrChoice)){
                echo "<li>
                    L'accès à la piscine :<br>
                    <div id='middle'>
                        Le premier bassin avec la nage à contre courant pousse à l’effort tandis que le bassin d’eau chaude de 6m sur 6m
                        invite à la détente et au bien-être. Une ambiance qui varie selon les moments de la journée, très dynamique ou
                        relaxante. Smoothies maison et tisanes d etox disponibles.
                    </div>
                </li><br>";
            }

            if(array_key_exists("AEMC", $usrChoice)){
                echo "<li>
                    L'accès aux équipements musculation et cardio :<br>
                    <div id='middle'>
                        Vous profiterez d'équipement de dernières génération sur notre espace dédié à la musculation (machines libres et
                        machines guidées) et sur notre plateau cardio (elliptiques, vélos, tapis de course, etc.).
                    </div>
                        </li><br>";
            }
            echo "</ul>";

            if($usrChoice["age"] == "0"){
                echo "Vous êtes étudiant(e). ";
            }else if($usrChoice["age"] == "1"){
                echo "Vous êtes sénior(e). ";
            }

            echo "Nous vous proposons le tarif suivant : <b><span id='prix'>" . $tarif . "€</span></b><br>
            Nous vous envoyons une proposition écrite avec nos conditions générales de vente par mail à votre adresse <div id='middle'><span id='user'>$mail</span></div>";


        ?>
    </body>
</html>