    function loadFile(filePath)
    {
        var result = null;
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", filePath, false);
        xmlhttp.send();
        if (xmlhttp.status==200)
        {
            result = xmlhttp.responseText;
        }
        return result;
    }

    let arquivo = "data.json";
    let texto = loadFile(arquivo);
    let json = JSON.parse(texto);   //Parser do arquivo texto
    let Wsyn = json.pesos           //Wsyn é a mesma matrix Wsyn do arquivo Python

    // create an array with nodes  
    var nodes_array = [];
    let _NEURON = "Neuron ";
    for(var i = 0; i< Wsyn[0].length;i++)     //Cria um array com todos os nós do sistema
    {
        nodes_array.push({id: i, label: _NEURON.concat(String(i+1))});
    }
 
    var nodes = new vis.DataSet(nodes_array);      //Cria o objeto nodes

    // create an array with edges
    // É necessario varrer cada elemento da matrix para checar as coneccoes
    var edges_array = [];
    for(var i = 0; i< Wsyn[0].length;i++)
    {
        for(var j = 0; j< Wsyn[0].length;j++)
        {
            if (Wsyn[i][j] != 0)
                edges_array.push(
                    {from: i, 
                    to: j, 
                    arrows:'to',
                    dashes:true,
                    label:String(Wsyn[i][j]),
                    value:Wsyn[i][j],
                    smooth: {type: 'cubicBezier'}}
                );
        }
    }

  var edges = new vis.DataSet(edges_array);

  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };

  var options =
    {
        edges: {
            selectionWidth: function (width) {return width*2;},
            scaling: {
                min: 1,
                max: 5,
                label: {
                    enabled: true,
                    min: 10,
                    max: 20,
                    maxVisible: 60,
                    drawThreshold: 15
                }
            },
        },
        layout: {
            improvedLayout: true,
        },
        physics: 
        {
            barnesHut: {
                gravitationalConstant: -800,
                centralGravity: 0.1,
                springConstant: 0,
                avoidOverlap: 0
            }
        }
    };





  var network = new vis.Network(container, data, options);

    network.on("selectNode", function (params) {
        let filePath = "images/n";
        filePath+=String(params.nodes[0]+1)
        filePath+=".png";
        document.getElementById('templateImage').src=filePath;
        document.getElementById('templateImage').style.display='block';

        var nodeID = params.nodes[0];
        if (nodeID)
        {
            var clickedNode = nodes.get(nodeID);
            clickedNode.color = 
            {
                highlight: 
                {
                    border: '#790812',
                    background: '#FFFFFF'
                }
            }
        nodes.update(clickedNode);
        }
    });