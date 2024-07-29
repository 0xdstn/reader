<?php
    include('inc/core.php');

    if($_GET['id'] != null) {
        $id = $_GET['id'];
        $fp = fopen('data.txt', 'r');
        $lines = array();
        $i = 0;
        if($id != null) {
            while (($ln = fgets($fp)) !== false) {
                if($i == $id) {
                    $ln[0] = 'R';
                }
                $lines[] = trim($ln);
                $i++;
            }
            fclose($fp);  
            file_put_contents('data.txt',implode("\n",$lines));
        }
    }
    home();
?>
