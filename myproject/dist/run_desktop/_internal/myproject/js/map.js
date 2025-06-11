document.addEventListener("DOMContentLoaded", function () {
    const mapElement = document.getElementById("map");
    const idToken = mapElement.getAttribute("data-id-token");

    if (!idToken) {
        alert("No Earth Engine token provided.");
        return;
    }

    ee.data.authenticateViaOauth(idToken, () => {
        ee.initialize(null, null, () => {
            console.log("Earth Engine initialized");

            // Set up Leaflet map
            const map = L.map("map").setView([24.9, 91.8], 9);
            L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
                attribution: '&copy; OpenStreetMap contributors',
            }).addTo(map);

            // Add EE flood image
            const floodImage = ee.Image('MODIS/MCD43A4_006_NDVI/2017_05_01').visualize({
                min: 0.0,
                max: 9000,
                palette: ['000000', '00FF00']
            });

            const mapId = floodImage.getMap({ format: 'png' }, (mapId) => {
                const eeTileUrl = `https://earthengine.googleapis.com/map/${mapId.mapid}/{z}/{x}/{y}?token=${mapId.token}`;
                L.tileLayer(eeTileUrl, { attribution: "Google Earth Engine" }).addTo(map);
            });

        }, (err) => {
            console.error("EE init error", err);
        });
    }, (err) => {
        console.error("Auth error", err);
    });
});
