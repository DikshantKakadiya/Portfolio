<!-- process_request.php -->
<?php
// Establish database connection
$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "PSIRT";

$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// Retrieve form data
$petName = $_POST['pet_name'];
$requestDate = $_POST['request_date'];

// Prepare and bind the statement
$stmt = mysqli_prepare($conn, "INSERT INTO Orders (type, state) VALUES (?, ?)");
mysqli_stmt_bind_param($stmt, "ss", $petName, $requestDate);

// Execute the statement
if (mysqli_stmt_execute($stmt)) {
  echo "Request submitted successfully.";
} else {
  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

// Close the statement and connection
mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
