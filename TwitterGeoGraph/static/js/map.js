var map;
var geocoder;
var addresses = [
    '東京都千代田区永田町1丁目7-1',
    '東京都千代田区霞が関2丁目1番1号',
    '東京都千代田区霞が関1-1-1',
    '東京都千代田区霞が関2-1-3'
]
function initMap(){
    geocoder = new google.maps.Geocoder();
    geocoder.geocode({
        'address': addresses[0]
    }, function(results, status) { // 結果
        map = new google.maps.Map(document.getElementById('mainmap'), { // #sampleに地図を埋め込む
            center: results[0].geometry.location, // 地図の中心を指定
            zoom: 15 // 地図のズームを指定
        });
    });
    addresses.map(function(address, i){
    	geocoder.geocode({'address' : address}, function(results, status) {
            // マーカーの表示
            var position = results[0].geometry.location;
            var marker = new google.maps.Marker({
                position: position,
                map: map
            });
    	});
    });
}
