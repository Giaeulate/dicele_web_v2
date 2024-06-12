(function($){
    $(document).ready(function(){
        // Encontrar las filas del AcepcionInline
        var $acepcionRows = $('div.inline-group div.inline-related');

        // Iterar sobre cada fila y asignar el índice
        $acepcionRows.each(function(index){
            // Encontrar el campo de índice y actualizar su valor
            var $indexField = $(this).find('input[name$="-get_index"]');
            $indexField.val(index + 1);
        });
    });
})(django.jQuery);
