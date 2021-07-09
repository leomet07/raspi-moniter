<!-- App.svelte -->
<script>
	import { Router, Link, Route } from "svelte-routing";
	import Home from "./routes/Home.svelte";
	import About from "./routes/About.svelte";

	export let url = "";
</script>

<Router {url}>
	<nav id="navbar">
		<Link to="/">Home</Link>
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
