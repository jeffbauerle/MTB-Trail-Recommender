// $(function() {
//     var dropdown = {
//         region: $('#select_region'),
//         trail: $('#select_trail')
//     };

   



//     // function to call XHR and update goodsrec dropdown
//     function updateTrail() {
//         var region = dropdown.region.val();
//         dropdown.trail.attr('disabled', 'disabled');
//         console.log(region);

//         if (region.length) {
//             dropdown.trail.empty();
//             var trailsUrl = $("#trailsUrl").val();
//             $.getJSON(trailsUrl, {region: region}, function(data) {
//                 console.log(data);
//                 data.forEach(function(item) {
//                     dropdown.trail.append(
//                         $('<option>', {
//                             // style: df['colors'].iloc[item.id]
//                             class: item.color,
//                             value: item.id,
//                             text: item.name
//                         })
//                     );
//                 });
//                 dropdown.trail.removeAttr('disabled');
//             });
//         }
//     }

//     // event listener to customer dropdown change
//     dropdown.region.on('change', function() {
//         updateTrail();
//     });


// });

