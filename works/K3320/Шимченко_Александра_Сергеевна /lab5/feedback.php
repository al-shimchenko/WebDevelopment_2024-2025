<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $firstname = htmlspecialchars($_POST['firstname']);
    $lastname = htmlspecialchars($_POST['lastname']);
    $email = htmlspecialchars($_POST['email']);
    $feedback = htmlspecialchars($_POST['feedback']);
    $variant = isset($_POST['variant']) ? htmlspecialchars($_POST['variant']) : 'Не указано';
    $topics = isset($_POST['topics']) ? $_POST['topics'] : [];

    echo "<h1>Обратная связь получена, спасибо!</h1>";
    echo "<p><strong>Имя:</strong> $firstname</p>";
    echo "<p><strong>Фамилия:</strong> $lastname</p>";
    echo "<p><strong>Email:</strong> $email</p>";
    echo "<p><strong>Вариант:</strong> $variant</p>";
    echo "<p><strong>Выбранные темы:</strong> " . implode(', ', $topics) . "</p>";
    echo "<p><strong>Обратная связь:</strong> $feedback</p>";

} elseif ($_SERVER["REQUEST_METHOD"] === "GET") {
    $firstname = isset($_GET['firstname']) ? htmlspecialchars($_GET['firstname']) : '';
    $lastname = isset($_GET['lastname']) ? htmlspecialchars($_GET['lastname']) : '';
    $email = isset($_GET['email']) ? htmlspecialchars($_GET['email']) : '';
    $feedback = isset($_GET['feedback']) ? htmlspecialchars($_GET['feedback']) : '';
    $variant = isset($_GET['variant']) ? htmlspecialchars($_GET['variant']) : 'Не указано';
    $topics = isset($_GET['topics']) ? $_GET['topics'] : [];

    echo "<h1>Обратная связь получена, спасибо!</h1>";
    echo "<p><strong>Имя:</strong> $firstname</p>";
    echo "<p><strong>Фамилия:</strong> $lastname</p>";
    echo "<p><strong>Email:</strong> $email</p>";
    echo "<p><strong>Вариант:</strong> $variant</p>";
    echo "<p><strong>Выбранные темы:</strong> " . implode(', ', $topics) . "</p>";
    echo "<p><strong>Обратная связь:</strong> $feedback</p>";
} else {
    echo "Неверный метод запроса.";
}
?>