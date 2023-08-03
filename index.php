<?php
     include('inc/core.php');   
    $title = 'Home';
?>

<?php include('inc/header.php'); ?>
<h1>Reader</h1>
<p>
    [<a href="add.php?key=<?php echo $key; ?>">Add article</a>]
</p>
<ol start='0'>
    <?php
        $fp = fopen('data.txt', 'r');
        $lines = array();
        while (($ln = fgets($fp)) !== false) {
            $ex = explode('|',trim($ln));
            if($ex[0] == 'U') {
                echo '<li><a href="articles/' . md5($ex[1]) . '.html">'.($ex[2] ? $ex[2] : $ex[1]).'</a></li>';
            }
        }
        fclose($fp);  
    ?>
</ol>
<?php include('inc/footer.php'); ?>
