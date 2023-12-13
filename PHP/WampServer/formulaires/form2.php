<?php

    foreach($_FILES as $file){
        move_uploaded_file($file["tmp_name"], "./datas/" . $file['name']);
        echo $file['name'] . " à été envoyé !<br>";
    }

?>