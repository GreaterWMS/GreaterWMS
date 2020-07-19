
function initMap() {
    var html = `
        <div class="goolge-map-content">
                <div class="thumb">
                    <img src="assets/img/news/01.jpg" alt="google hover images">
                    <span class="tag">travel</span>
                    <div class="hover">
                        <span class="rating">3.5</span>
                        <div class="content-inner">
                            <div class="icon">
                                <a href="#"><i class="far fa-heart"></i></a>
                            </div>
                            <div class="content">
                               <a href="#"><h4>Turanto Boat Ride</h4></a>
                                <span class="location">20/b, Parker island, united kingdom</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    `;
    var locations = [
        [html, 23.9748222, 89.2077907, 3, 'assets/img/marker/01.png'],
        [html, 23.8048222, 89.6077907, 2, 'assets/img/marker/02.png'],
        [html, 23.9000222, 90.0577907, 1, 'assets/img/marker/03.png'],
        [html, 23.7648222, 90.727707, 4, 'assets/img/marker/04.png'],
        [html, 23.8248222, 90.9579007, 5, 'assets/img/marker/05.png'],
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: new google.maps.LatLng(23.8066719, 90.3237784),
        styles: [
            {
                elementType: 'labels',
                stylers: [{
                    visibility: 'on'
                }]
            },
            {
                elementType: 'geometry',
                stylers: [{
                    color: '#EDEDED'
                }]
            },
            {
                featureType: 'administrative.locality',
                elementType: 'labels.text.fill',
                stylers: [{
                    color: '#b1b1b1'
                }]
            },
            {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{
                    color: '#F7F7F7'
                }]
            },
            {
                featureType: 'road',
                elementType: 'geometry',
                stylers: [{
                    color: '#F7F7F7'
                }]
            },
            {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{
                    color: '#F7F7F7'
                }]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{
                    color: '#F7F7F7'
                }]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry.stroke',
                stylers: [{
                    color: '#F7F7F7'
                }]
            },
            {
                featureType: 'water',
                elementType: 'geometry',
                stylers: [{
                    color: '#F7F7F7'
                }]
            },
            {
                featureType: 'water',
                elementType: 'labels.text.fill',
                stylers: [{
                    color: '#b1b1b1'
                }]
            },
            {
                "featureType": "road",
                "elementType": "labels",
                "stylers": [
                    { "visibility": "off" }
                ]
            }
        ]
        //mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map,
            icon: locations[i][4],
            animation: google.maps.Animation.DROP,
        });
        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }




}
