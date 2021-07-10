<!-- App.svelte -->
<script>
	import { Router, Link, Route } from "svelte-routing";
	import Home from "./routes/Home.svelte";
	import About from "./routes/About.svelte";

	window.BASE_URL = process.env.API_URL;
	console.log(window.BASE_URL);
	if (
		window.location.hostname == "localhost" ||
		window.location.hostname == "127.0.0.1"
	) {
		console.log("In development mode");
		window.BASE_URL = "http://127.0.0.1:4040";
	}

	export let url = "";
</script>

<Router {url}>
	<nav id="navbar">
		<Link to="/">Home</Link> |
		<Link to="about">About</Link>
	</nav>
	<div>
		<Route path="about" component={About} />
		<Route path="/"><Home /></Route>
	</div>
</Router>

<style>
	* {
		box-sizing: border-box;
	}
	#navbar {
		text-align: center;
	}
</style>
