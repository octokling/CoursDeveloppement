<?php
    $titre = $_POST["Titre"];
    $editeur = $_POST["Editeur"];
    $date = $_POST["Date_de_publication"];
    $isbn = $_POST["ISBN-10"];

    echo "
    <b>Titre</b> : $titre<br>
    <b>Éditeur</b> : $editeur<br>
    <b>Date de publication</b> : $date<br>
    <b>ISBN-10</b> : $isbn";
?>