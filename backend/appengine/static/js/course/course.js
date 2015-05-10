/**
 * Created by marcos on 06/05/15.
 */

$(document).ready(function() {
    var nome = $("#nameInput");
    var dur = $("#durationInput");
    var salvar = $("#salvar");
    var deletar = $("#excluir");
    var records = $('ol');
    var gerenciar = $("#gerenciar");
    var fields = $("#fields input[type=text]");
    var ajaxBtn = $('#ajax-save-gif');
    records.toggle();
    ajaxBtn.hide();

    function clearAllInputs() {
        fields.val('');
    }

    function getFields() {
        return {
            'name': nome.val(),
            'duration': dur.val(),
            'subjects': $('option:selected').val()
        }
    }

    $(salvar).click(function(){
        $('.has-error').removeClass('has-error');
        $('.help-block').empty();
        salvar.attr('disabled', 'disabled');
        ajaxBtn.show("slow");
        $.post('/acourses/rest/salvar',
            getFields(),
            clearAllInputs()
        ).error(function(erro) {
                for (propriedade in erro.responseJSON){
                    $('#'+propriedade+'-div').addClass('has-error');
                    $('#'+propriedade+'-span').text(erro.responseJSON[propriedade]);
                }
            }).always(function(){
                ajaxBtn.hide();
                salvar.removeAttr('disabled');
            });
    });

    $(deletar).click(function () {

    });

    gerenciar.click(function() {
        records.slideToggle();
    });
});