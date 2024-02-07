<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulaire</title>
    </head>
    <body>
        <div class="Formulaire">
            <form action="#" method="post">
                <label for="marque">Choisissez une marque de voiture</label>
                <select name="editeur" required>
                    <option value="Renault">Renault</option>
                    <option value="Peugeot">Peugeot</option>
                    <option value="Toyota">Toyota</option>
                    <option value="Volkswagen">Volkswagen</option>
                </select>
                <input type="submit">
            </form>
        </div>
        
        <div class="Resultats">
            <?php
                if($_POST){
                    echo "oui";
                }else{
                    echo "false";
                }
            ?>
        </div>
    </body>
</html>