<script>
	import Chart from "chart.js/auto";

	import { onMount } from "svelte";
	onMount(async () => {
		console.log("Hello Home!");

		var xyValues = [
			{ x: 50, y: 7 },
			{ x: 60, y: 8 },
			{ x: 70, y: 8 },
			{ x: 80, y: 9 },
			{ x: 90, y: 9 },
			{ x: 100, y: 9 },
			{ x: 110, y: 10 },
			{ x: 120, y: 11 },
			{ x: 130, y: 14 },
			{ x: 140, y: 14 },
			{ x: 150, y: 15 },
		];

		var mychart = new Chart("chart", {
			type: "scatter",
			data: {
				datasets: [
					{
						pointRadius: 4,
						pointBackgroundColor: "rgb(0,0,255)",
						data: xyValues,
					},
				],
			},
			options: {
				legend: { display: false },
				scales: {
					xAxes: [{ ticks: { min: 40, max: 160 } }],
					yAxes: [{ ticks: { min: 6, max: 16 } }],
				},
			},
		});

		let response = await fetch("http://127.0.0.1:4040/get_data", {
			method: "GET",
			headers: {},
		});

		let data = await response.json();

		console.log(data);
	});
</script>

<h1>Home</h1>
<div>
	<canvas id="chart" width="400" height="400" />
</div>
