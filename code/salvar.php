<?php
include_once("conexao.php");
$nome = $_POST['nome'];
$email = $_POST['email'];
$senha = $_POST['senha']

$query = "INSERT INTO Clientes (nome, email, senha)
          VALUES ('$nome', '$email', '$senha')";
$resultado = mysqli_query($conn, $query);

if(mysqli_affected_rows($conn) > 0)
{
    echo "Cliente salvo com sucesso";
} else{
    echo "Cliente não foi salvo com sucesso";
}