/**
 * Created by marcos on 09/05/15.
 */

$(document).ready(function() {
    var username = $('#usernameInput');
    var password = $('#passwordInput');
    var email = $('#emailInput');
    var name = $('#nameInput');
    var birthday = $('#birthdayInput');
    var records = $('#ol').toggle();
    var salvar = $('#salvar');
    var deletar = $('#deletar');
    var gerenciar = $('#gerenciar');
    var fields = $('#fields').find('input');
    var ajaxBtn = $('#ajax-save-gif').hide();

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

    function getId(ctx) {
        return {
            'id': ctx.val()
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
        ).success(function(dct) {
                table.append('<tr value="'+dct["id"]+'"> <td>'+dct["username"]+
                '</td> <td>' +dct["email"]+ '</td>'+
                '<td>' +dct["name"]+ '</td> <td>'+ dct["birthday"]+
                '<td> <a class="btn btn-success" href="{{ s.edit_path }}" style="background: #10698F !important; margin-left: 10px"> <i class="glyphicon glyphicon-pencil"></i></a>'+
                '</td> <td> <button class="btn btn-danger" value="'+dct["id"]+'" style="margin-left: 10px"> <i class="glyphicon glyphicon-trash"></i> </button> </td>');
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


    gerenciar.click(function() {
       records.slideToggle();
       $(this).css({"color":"white"});
    });
});

