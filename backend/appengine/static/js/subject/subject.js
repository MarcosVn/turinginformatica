/**
 * Created by marcos on 07/05/15.
 */

$(document).ready(function() {
    var name = $('#nameInput');
    var activities = $('#activitiesInput');
    var records = $('ol');
    var salvar = $('#salvar');
    var deletar = $('#deletar');
    var gerenciar = $('#gerenciar');
    var fields = $('#fields').find('input[type=text]');
    var ajaxBtn = $('#ajax-save-gif');
    records.toggle();
    ajaxBtn.hide();

    function clearAllFields() {
        fields.val('');
    }

    function getFields() {
        return {
            'name': name.val(),
            'activities': activities.val()
        }
    }

    salvar.click(function() {
        $('.has-error').removeClass('has-error');
        $('.help-block').empty();
        salvar.attr('disabled', 'disabled');
        ajaxBtn.show("slow");
        $.post('/subjects/rest/salvar',
            getFields(),
            clearAllFields()
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

    deletar.click(function() {

    });

    gerenciar.click(function(){
        records.slideToggle();
    });
});
