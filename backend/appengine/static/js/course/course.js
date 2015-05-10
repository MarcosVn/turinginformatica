/**
 * Created by marcos on 06/05/15.
 */

$(document).ready(function() {
    var nome = $("#nameInput");
    var dur = $("#durationInput");
    var salvar = $("#salvar");
    var records = $('#ol').toggle();
    var gerenciar = $("#gerenciar");
    var fields = $('#fields').find('input[type=text]');
    var ajaxBtn = $('#ajax-save-gif').hide();
    var table = $('table');

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

    function getId(ctx) {
        return {
            'id': ctx.val()
        }
    }

    $(document).on('click', 'td button', function() {
        var r = confirm("Deseja realmente remover este registro?");

        if (r) {
            $.post('/acourses/rest/deletar',
                getId($(this))
            ).success(function(dic) {
                    $('tr[value='+dic["id"]+']').remove();
                });
        }
    });

    salvar.click(function(){
        $('.has-error').removeClass('has-error');
        $('.help-block').empty();
        salvar.attr('disabled', 'disabled');
        ajaxBtn.show("slow");
        $.post('/acourses/rest/salvar',
            getFields(),
            clearAllInputs()
        ).success(function(dct) {
                var hj = new Date();
                table.append('<tr value="'+dct["id"]+'"> <td>'+dct["name"]+
                '</td> <td>' +dct["duration"]+ '</td>'+
                '<td>' +(hj.toLocaleDateString() +'&nbsp;&nbsp;'+ hj.toLocaleTimeString())+ '</td>'+
                '<td> <a class="btn btn-success" href="{{ s.edit_path }}" style="background: #10698F !important; margin-left: 10px"> <i class="glyphicon glyphicon-pencil"></i></a>'+
                '</td> <td> <button class="btn btn-danger" value="'+dct["id"]+'" style="margin-left: 10px"> <i class="glyphicon glyphicon-trash"></i> </button> </td>');
            }).error(function(erro) {
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