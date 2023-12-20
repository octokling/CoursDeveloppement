<?php
    function resultDices(){
        static $ancien = null;
        static $lances = 0;

        $nouveau = rand(1,6);
        $lances++;

        if($ancien != null){
            if($lances <= 6){
                echo "Ancien: $ancien Nouveau: $nouveau -> ";
                if($ancien < $nouveau){
                    echo "Gagné !\n";
                    $ancien = null;
                }else if($ancien == $nouveau){
                    echo "Égalité.\n";
                    $ancien = null;
                }else if($ancien > $nouveau){
                    echo "Perdu...\n";
                    $ancien = null;
                }
            }
        }else{
            $ancien = $nouveau;
        }
    }
    
    for($i=0;$i <= 10; $i++){
        resultDices();
    }
?>