<!-- client_dashboard.php -->
<?php
// Retrieve the user ID from the session or authentication data
$userId = $_SESSION['user_id'];

// Query the database to retrieve client requests
$sql = "SELECT * FROM Orders WHERE client_id = $userId";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
  // Display the client requests
  while ($row = mysqli_fetch_assoc($result)) {
    $orderNumber = $row['order_number'];
    $type = $row['type'];
    $state = $row['state'];
    
    // Display the order details
    echo "Order Number: $orderNumber<br>";
    echo "Type: $type<br>";
    echo "State: $state<br><br>";
  }
} else {
  echo "No requests found.";
}
?>
