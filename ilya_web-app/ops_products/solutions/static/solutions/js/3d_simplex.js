 var data = [
            {
                type: 'surface',
                x: {{ X.tolist()|safe }},
                y: {{ Y.tolist()|safe }},
                z: {{ Z1.tolist()|safe }},
                colorscale: 'Viridis'
            },
            {
                type: 'surface',
                x: {{ X.tolist()|safe }},
                y: {{ Y.tolist()|safe }},
                z: {{ Z2.tolist()|safe }},
                colorscale: 'Hot'
            }
        ];

        var layout = {
            title: 'Production Distribution',
            scene: {
                xaxis: {title: 'P1'},
                yaxis: {title: 'P2'},
                zaxis: {title: 'Z'}
            }
        };

        Plotly.newPlot('plot', data, layout);