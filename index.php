<?php

    function generate($type = 'password', $length = 14)
    {
        $time = time();

        $characters = '';

        if ($type == 'password')
            $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),./<>?;:{}|[]\-=_+~';
        else
            $characters = '0123456789abcdefghijklmnopqrstuvwxyz';

        $charactersLength = strlen($characters);
        $randomString = '';

        for ($i = 0; $i < $length; $i++)
        {
            $randomString .= $characters[rand(0, $charactersLength - 1)];
        }

        $randomString = $time . $randomString;

        return $randomString;
    }

    $emailAddress = generate('sensative', '20')."@cwfrazier.com";
    $password = generate('password', 20);
?>

<html>
    <head>
        <title>New Password</title>

    </head>
    <body>
    <form method="POST" action="index.php">
<?php
    echo "
        <table>
            <tr><td>$emailAddress</td></tr>
            <tr><td>$password</td></tr>
        </table>
";

?>

    </form>
    </body>
</html>
