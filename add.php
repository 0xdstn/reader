<?php
    include('inc/core.php');

    $title = 'Add article';

    if($_GET['url']) {
        $url = $_GET['url'];
        $fp = fopen('data.txt', 'a');
        fwrite($fp, "\n" . 'U|' . $url);
        fclose($fp);  
        home();
    }
?>

<?php include('inc/header.php'); ?>
        <h1>Add article</h1>
        <form method="GET">
            <input type="text" name="url" placeholder="URL" /><br>
            <?php echo getKeyInput(); ?>
            <input type="submit" value="Add" />
        </form>
<?php include('inc/footer.php'); ?>

