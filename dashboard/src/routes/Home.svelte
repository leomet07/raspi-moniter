<script>
	import Chart from "chart.js/auto";
	import "chartjs-adapter-moment";
	import moment from "moment";

	import { onMount } from "svelte";
	onMount(async () => {
		console.log("Hello Home!");

		let response = await fetch("http://127.0.0.1:4040/get_data", {
			method: "GET",
			headers: {},
		});

		let data = await response.json();

		console.log(data);

		let speeds = {
			datasets: [
				{
					label: "Upload",
					data: {},
					fill: false,
					borderColor: "green",
				},
				{
					label: "Download",
					data: {},
					fill: false,
					borderColor: "blue",
				},
			],
		};
		let losses = {
			datasets: [
				{
					label: "Loss",
					data: {},
					fill: false,
					borderColor: "red",
				},
			],
		};
		for (let i = 1; i < data.length; i++) {
			// Start at 1 to skip first row

			let row = data[i];

			if (row.includes(null)) {
				continue; // if error value, skip it
			}

			console.log(i, row);

			let timestamp = row[row.length - 1];
			console.log(timestamp);

			let upload = row[0];
			let download = row[1];
			let loss = row[2];

			// Add upload

			speeds.datasets[0].data[timestamp] = upload;

			speeds.datasets[1].data[timestamp] = download;

			losses.datasets[0].data[timestamp] = loss;
		}

		genChart(speeds, "Internet speeds", "speeds");
		genChart(losses, "Packet Loss", "losses", 80);
	});

	function genChart(data, title, chartid, max) {
		console.log(data);
		let config = {
			type: "line",
			data: data,
			options: {
				maintainAspectRatio: false,
				responsive: true,
				plugins: {
					title: {
						display: true,
						text: title,
					},
				},
				scales: {
					x: {
						type: "time",
						time: {
							unit: "minute",
							format: "h:mm:ss.SSS a",
						},
					},
					y: {
						max: max || null,
						min: 0,
					},
				},
			},
		};

		const chart = new Chart(chartid, config);
	}
</script>

<main id="home">
	<h1>Home</h1>
	<div class="canvas_container">
		<canvas class="chartjschart" id="speeds" />
	</div>
	<div class="canvas_container">
		<canvas class="chartjschart" id="losses" />
	</div>
</main>

<style>
	.chartjschart {
		width: 100%;
		height: 100%;
	}
	.canvas_container {
		height: 600px;
		margin-bottom: 100px;
	}
	#home {
		text-align: center;
	}
</style>
