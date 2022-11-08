<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/style/cadastro.css" rel="stylesheet">
    <title>Cadastro</title>
</head>
<body>
<div class="header">
        <h1 class="bl"><a href="/code/index.html">BLACKTIE</a></h1>
    </div>
    <?php include_once("conexao.php"); ?>
   <div class="container">
        <h2>Cadastro</h2>
        <form method="post" action="salvar.php">
            <label>Nome</label><br>
            <input type="text" placeholder="nome" name="nome" required><br>
            <br>
            <label>Email</label><br>
            <input type="text" placeholder="email" name="email" required><br>
            <br>
            <label>Senha</label><br>
            <input type="password" placeholder="senha" name="senha" required><br>
            <br>
            <input type="checkbox" class="checkbox" required><p class="termos">Concordo com os <a href="/code/termos.html">Termos</a></p><br>
            <br>
            <input type="submit" value="salvar">
        </form>
   </div>
</body>
</html>