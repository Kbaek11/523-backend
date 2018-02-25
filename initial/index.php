<html>
  <head>
    <title>PHP Test</title>
    <script src="hello.js"></script>
  </head>

  <body>
    <?php echo "<p>Hello, World</p>"; ?>
    <form name="myForm" action="/action_page.php"
    onsubmit="return validateForm()" method="post">
    Name: <input type="text" name="fname">
    <input type="submit" value="Submit">
    </form>
  </body>

</html>
