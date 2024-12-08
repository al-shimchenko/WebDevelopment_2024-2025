<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "orders";

// Создаем соединение
$conn = new mysqli($servername, $username, $password, $dbname);

// Проверяем соединение
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Получаем данные из формы
$last_name = $_POST['last_name'];
$first_name = $_POST['first_name'];
$middle_name = $_POST['middle_name'];
$address = $_POST['address'];
$phone = $_POST['phone'];
$email = $_POST['email'];
$product = $_POST['product'];
$comment = $_POST['comment'];

// SQL-запрос для вставки данных
$sql = "INSERT INTO orders (last_name, first_name, middle_name, address, phone, email, product, comment)
VALUES ('$last_name', '$first_name', '$middle_name', '$address', '$phone', '$email', '$product', '$comment')";

if ($conn->query($sql) === TRUE) {
    echo "Спасибо за заказ!";
} else {
    echo "Ошибка: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>