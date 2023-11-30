<?php
    // Dans ce bonus, nous allons faire un système de gestion d'utilisateurs
    /* La structure du tableau user 
    users:
        (index qui sera son ID)0:
            firstName:
            lastName:
            birthday:
            gender:
            email:
            phone:

    */
    
    $users = array();
    function addRandUser($users){
        $firstNames = array("Astghik", "Enola", "Alexandre", "Lounes", "Loann", "Noa", "Killian", "Logan", "Axel", "Manon", "Gabin", "Matheo", "Alexis", "Clement", "Killian", "Kevin", "Erwan");
        $lastNames = array("Manukyan", "Texier", "Kosiorek", "Souakri", "Barbier", "Mingouolo", "Beaufils", "Gaillard", "Degrauw", "Lefevre", "Ernoult", "Lescouzere", "Lerocheleuil", "Ramos", "Robin", "Roux", "Mornac");
        $mailDomains = array("gmail.com", "outlook.fr", "outlook.com", "free.fr", "sfr.fr", "orange.fr", "ac-poitiers.fr", "lycee-merleauponty.net");

        $firstNameSelected = rand(0, count($firstNames) - 1);
        $lastNameSelected = rand(0, count($lastNames) - 1);
        $mailDomainSelected = rand(0, count($mailDomains) - 1);
        $gender = "";

        switch($firstNames[$firstNameSelected]){
            case "Astghik":
                $gender = "Female";
                break;
            case "Manon":
                $gender = "Female";
                break;
            case "Enola":
                $gender = "Female";
                break;
            default:
                $gender = "Male";
                break;
        }

        /*$birthMin = strtotime("50 years ago");
        $birthMax = strtotime("18 years ago");

        $rand_time = mt_rand($min, $max);

        $birth_date = date('%d/%m/%Y', $rand_time);*/

        $users[count($users)] = array("firstName"=>$firstNames[$firstNameSelected], "lastName"=>$lastNames[$lastNameSelected], "birthday"=>"??/??/????", "gender"=>$gender, "email"=>strtolower($firstNames[$firstNameSelected]) . "_" . strtolower($lastNames[$lastNameSelected]) . "@" . $mailDomains[$mailDomainSelected], "phone"=>"06 XX XX XX XX");

        return $users;
    }   

    function AfficherTableau($users){
        echo "O----------------------------------------------------------------------------------------------------------------------------------O\n";

        foreach($users as $id => $user){
            echo "| ";
            if($id < 10){
                echo "ID: " . $id . "    | ";
            }else if($id < 100){
                echo "ID: " . $id . "   | "; 
            }else if($id < 1000){
                echo "ID: " . $id . "  | "; 
            }else{
                echo "ID: " . $id . " | "; 
            }

            echo "First Name: " . $user["firstName"];
            for($i=1; $i != 15 - strlen($user["firstName"]); $i++){
                echo " ";
            }

            echo "| ";

            echo "Last Name: " . $user["lastName"];
            for($i=1; $i !=20 - strlen($user["lastName"]); $i++){
                echo " ";
            }
            echo "| ";

            echo "E-Mail : " . $user["email"];
            for($i=1; $i !=50 - strlen($user["email"]); $i++){
                echo " ";
            }
            echo "|\n";
        }
        echo "O----------------------------------------------------------------------------------------------------------------------------------O\n";
    }


    for($i=0;$i!=52;$i++){
        $users = addRandUser($users);
    }

    AfficherTableau($users);
?>