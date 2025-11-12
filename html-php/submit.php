<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="utf-8">
    <title>Dati inviati</title>
</head>
<body>
    <h1>Dati inviati</h1>
    <ul>
        <li>Nome: <?php echo $_POST['nome']; ?></li>
        <li>Cognome: <?php echo $_POST['cognome']; ?></li>
        <li>Data di nascita: <?php echo $_POST['data_nascita']; ?></li>
        <li>Email: <?php echo $_POST['email']; ?></li>
        <li>Telefono: <?php echo $_POST['telefono']; ?></li>
        <li>Note: <?php echo $_POST['note']; ?></li>
    </ul>
    <p><a href="form.html" target="_blank">Torna al form</a></p>
</body>
</html>