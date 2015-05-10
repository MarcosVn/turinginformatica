/**
 * Created by marcos on 09/05/15.
 */

$(document).ready(function() {
    var username = $('#usernameInput');
    var password = $('#passwordInput');
    var email = $('#emailInput');
    var name = $('#nameInput');
    var birthday = $('#birthdayInput');
    var records = $('ol');
    var salvar = $('#salvar');
    var deletar = $('#deletar');
    var gerenciar = $('#gerenciar');
    var fields = $('#fields input');
    var ajaxBtn = $('#ajax-save-gif');
    ajaxBtn.hide();
    records.toggle();

    function clearAllFields() {
        fields.val('');
    }

    function getFields() {
        return {
            'username': username.val(),
            'password': password.val(),
            'email' : email.val(),
            'name': name.val(),
            'birthday': birthday.val()
        }
    }

    salvar.click(function() {
        $('.has-error').removeClass('has-error');
        $('.help-block').empty();
        salvar.attr('disabled', 'disabled');
        ajaxBtn.show("slow");

        $.post('/users/rest/salvar',
            getFields(),
            clearAllFields()
        ).success(function(sucesso) {

            })
            .error(function(erro) {
                for (propriedade in erro.responseJSON){
                    $('#'+propriedade+'-div').addClass('has-error');
                    $('#'+propriedade+'-span').text(erro.responseJSON[propriedade]);
                }
            }).always(function(){
                ajaxBtn.hide();
                salvar.removeAttr('disabled');
            });
    });

    deletar.click(function() {}
    );

    gerenciar.click(function() {
       records.slideToggle();
    });
});

