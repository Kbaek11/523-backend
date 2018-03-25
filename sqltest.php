//save this as a .php page (e.g., sqltest.php)
<?php
$dbhost = getenv("MYSQL_SERVICE_HOST");  //IMPORTANT: the env MYSQL_SERVICE_HOST/PORT assumes your database service name is "MYSQL"
$dbport = getenv("MYSQL_SERVICE_PORT");  //If your database service name is "FOO", then this would be "FOO_SERVICE_HOST" and "FOO_SERVICE_PORT"
$dbuser = getenv("POSTGRESQL_USER");
$dbpwd = getenv("POSTGRESQL_PASSWORD");
$dbname = getenv("POSTGRESQL_DATABASE");
$connection = new mysqli($dbhost, $dbuser, $dbpwd, $dbname);
if ($connection->connect_errno) {
printf("Connect failed: %s\n", $mysqli->connect_error);
exit();
} else {
printf("Connected to the database");
}
$connection->close();
?>