'use strict';

$(document).ready(function() {

	// Area chart
	
	if ($('#apexcharts-area').length > 0) {
	var options = {
		chart: {
			height: 350,
			type: "area",
			toolbar: {
				show: false
			},
		},
		dataLabels: {
			enabled: false
		},
		stroke: {
			curve: "smooth"
		},
		series: [{
			name: "Teachers",
			data: [45, 60, 75, 51, 42, 42, 30]
		}, {
			name: "Students",
			color: '#FFBC53',
			data: [24, 48, 56, 32, 34, 52, 25]
		}],
		xaxis: {
			categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
		}
	}
	var chart = new ApexCharts(
		document.querySelector("#apexcharts-area"),
		options
	);
	chart.render();
	}

	// Bar chart
	
	if ($('#bar').length > 0) {
	// var optionsBar = {
	// 	chart: {
	// 		type: 'bar',
	// 		height: 350,
	// 		width: '100%',
	// 		stacked: true,
	// 		toolbar: {
	// 			show: false
	// 		},
	// 	},
	// 	dataLabels: {
	// 		enabled: false
	// 	},
	// 	plotOptions: {
	// 		bar: {
	// 			columnWidth: '45%',
	// 		}
	// 	},
	// 	series: [{
	// 		name: "Boys",
	// 		color: '#fdbb38',
	// 		data: [420, 532, 516, 575, 519, 517, 454, 392, 262, 383, 446, 551, 563, 421, 563, 254, 452],
	// 	}, {
	// 		name: "Girls",
	// 		color: '#19affb',
	// 		data: [336, 612, 344, 647, 345, 563, 256, 344, 323, 300, 455, 456, 526, 652, 325, 425, 436],
	// 	}],
	// 	labels: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
	// 	xaxis: {
	// 		labels: {
	// 			show: false
	// 		},
	// 		axisBorder: {
	// 			show: false
	// 		},
	// 		axisTicks: {
	// 			show: false
	// 		},
	// 	},
	// 	yaxis: {
	// 		axisBorder: {
	// 			show: false
	// 		},
	// 		axisTicks: {
	// 			show: false
	// 		},
	// 		labels: {
	// 			style: {
	// 				colors: '#777'
	// 			}
	// 		}
	// 	},
	// 	title: {
	// 		text: '',
	// 		align: 'left',
	// 		style: {
	// 			fontSize: '18px'
	// 		}
	// 	}

	// }
    $(document).ready(function() {
		// Fonction pour récupérer les données des élèves par niveau et par sexe via AJAX
		function fetchElevesParNiveauEtSexe() {
			$.ajax({
				url: '/get_eleves_par_niveau_et_sexe/',  // URL de la vue Django
				method: 'GET',
				dataType: 'json',
				success: function(data) {
					// Données récupérées
					var labels = data.labels;  // Noms des niveaux
					var garcons = data.garcons;  // Nombre de garçons par niveau
					var filles = data.filles;  // Nombre de filles par niveau
	
					// Configurer le graphique avec les données récupérées
					var optionsBar = {
						chart: {
							type: 'bar',
							height: 350,
							width: '100%',
							stacked: true,  // Activer le mode empilé
							toolbar: {
								show: false
							},
						},
						dataLabels: {
							enabled: false
						},
						plotOptions: {
							bar: {
								horizontal: false,  // Barres verticales
								columnWidth: '45%',
								endingShape: 'rounded'
							},
						},
						series: [{
							name: "Garçons",
							data: garcons,  // Données dynamiques
							color: '#19affb',  // Couleur bleue pour les garçons
						}, {
							name: "Filles",
							data: filles,  // Données dynamiques
							color: '#FFA500',  // Couleur orange pour les filles
						}],
						xaxis: {
							categories: labels,  // Noms des niveaux
						},
						yaxis: {
							title: {
								text: 'Nombre d\'élèves'
							}
						},
						title: {
							text: 'Nombre d\'élèves par niveau et par genre',
							align: 'left',
							style: {
								fontSize: '18px'
							}
						},
						legend: {
							show: true,  // Afficher la légende
							position: 'top',  // Position de la légende
						},
						fill: {
							opacity: 1,  // Opacité des barres
						},
					}
	
					// Rendu du graphique
					var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
					chartBar.render();
				},
				error: function(error) {
					console.error('Erreur lors de la récupération des données :', error);
				}
			});
		}
	
		// Appeler la fonction pour récupérer les données et générer le graphique
		fetchElevesParNiveauEtSexe();
	});

	var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
	chartBar.render();
	}
  
});