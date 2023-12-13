<table border=1 cellspacing="0">

<?php
    
    foreach($_GET as $cle => $valeur){
        
        echo "
            <tr>
                <td><b>$cle</b></td>
                <td>$valeur</td>
            </tr>";
    }
?>

</table>