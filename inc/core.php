<?php
    $key = trim(file_get_contents('../../key.txt'));
    $incomingKey = trim($_GET['key']);

    if($key !== $incomingKey) {
        die();
    }

    function getKeyInput() {
        global $key;
        return '<input type="hidden" name="key" value="'.$key.'" />' . "\n";
    }

    function home() {
        global $key;
        header('Location: /reader?key=' . $key);
    }

?>
