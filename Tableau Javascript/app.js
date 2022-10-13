console.log("I am here")


const containerDiv = document.getElementById('vizContainer');

const url = 'https://prod-apnortheast-a.online.tableau.com/t/koko/views/chart/1'

const options ={
    hideTabs:true,
    ofFirstInteractive: function(){
        console.log("hey");
    }
};

function initViz(){
    let viz = new tableau.Viz(containerDiv, url, options);
    window.setInterval(() => {
        console.log("Refreshing...");
        viz.refreshDataAsync();
    },10000);
}


initViz();

