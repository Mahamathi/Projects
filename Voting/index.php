<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>PHP Voting System</title>

	<!--css bootstrap link-->
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">

</head>
<body class="bg-dark">
	<h1 class="text-info text-center p-3">Voting System</h1>
	<div class="bg-info py-4">
		<h2 class="text-center">Login</h2>
		<div class="container text-center">
			<form action="actions/login.php" method="POST">
				<div class="mb-3">
					<input type="text" class="form-control w-50 m-auto" name="username" placeholder="Enter your username" required="required">
				</div>

				<div class="mb-3">
					<input type="text" class="form-control w-50 m-auto" name="mobile" placeholder="Enter your mobile number" required="required" maxlength="10" minlength="10">
				</div>

				<div class="mb-3">
					<input type="password" class="form-control w-50 m-auto" name="password" placeholder="Enter your password" required="required">
				</div>

				<div class="mb-3">
					<select name="std" class="form-select w-50 m-auto">
						<option value="group">Group</option>
						<option value="voter">Voter</option>
					</select>
				</div>
				<button type="submit" class="btn btn-dark my-4">Login</button>
				<p>Don't have an account?
				<a href="partials/registrationvoting.php" class="text-white">Register here</a>
			</form>
			
		</div>
	</div>

</body>
</html>