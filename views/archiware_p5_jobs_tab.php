<div id="archiware_p5_jobs-tab"></div>
<h2 data-i18n="archiware_p5_jobs.title"></h2>

<table id="archiware_p5_jobs-tab-table"></table>

<script>
$(document).on('appReady', function(){
    $.getJSON(appUrl + '/module/archiware_p5_jobs/get_data/' + serialNumber, function(data){
        var table = $('#archiware_p5_jobs-tab-table');
        $.each(data, function(key,val){
            var th = $('<th>').text(i18n.t('archiware_p5_jobs.column.' + key));
            var td = $('<td>').text(val);
            table.append($('<tr>').append(th, td));
        });
    });
});
</script>



