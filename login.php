<!-- login.php -->
<?php
// Include the FancySSO library
require_once 'fancy_sso_library.php';

// Initialize the FancySSO client
$fancySSO = new FancySSOClient('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET');

// Redirect the user to the SSO provider for authentication
$fancySSO->redirectToProvider();

// After successful authentication, the SSO provider will redirect the user back to this page

// Retrieve the authentication response from the SSO provider
$authResponse = $fancySSO->getAuthResponse();

// Verify the authentication response
if ($fancySSO->verifyAuthResponse($authResponse)) {
  // Authentication successful
  $userId = $authResponse['user_id'];
  $username = $authResponse['username'];
  
  // Store the user information securely (e.g., in a session)
  $_SESSION['user_id'] = $userId;
  $_SESSION['username'] = $username;
  
  // Redirect the user to the desired page
  header('Location: dashboard.php');
  exit;
} else {
  // Authentication failed
  echo "Authentication failed.";
}
?>
