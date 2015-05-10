/**
 * Created by marcos on 07/05/15.
 */
console.log('Oi')
$(document).ready(function() {
    var title = $("#titleInput");
    var content = $("#contentInput");
    var author = $("#authorInput");
    var records = $('ol').toggle();
    var salvar = $('#salvar');
    var deletar = $('#deletar');
    var gerenciar = $('#gerenciar');
    var fields = $('#fields input[type=text]');
    var ajaxBtn = $('#ajax-save-gif');
    ajaxBtn.hide();

    function clearAllInputs() {
        fields.val('');
    }

    function getFields() {
        return {
            'title': title.val(),
            'content': content.val(),
            'author' : author.val()
        }
    }

    $(salvar).click(function() {
        $('.has-error').removeClass('has-error');
        $('.help-block').empty();
        salvar.attr('disabled', 'disabled');
        ajaxBtn.show("slow");
        $.post('/articles/rest/salvar',
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

    $(deletar).click(function() {

    });

    gerenciar.click(function() {
        records.slideToggle();
    });
});

