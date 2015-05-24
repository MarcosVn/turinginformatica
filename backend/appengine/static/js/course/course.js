/**
 * Created by marcos on 06/05/15.
 */

$(document).ready(function() {
    var nome = $("#nameInput");
    var dur = $("#durationInput");
    var edu = $("#educationProjectInput");
    var salvar = $("#salvar");
    var records = $('#ol');
    var gerenciar = $("#gerenciar");
    var fields = $('#fields').find('input[type=text]');
    var ajaxBtn = $('#ajax-save-gif');
    var table = $('table');
    records.toggle();
    ajaxBtn.hide();


    function clearAllInputs() {
        fields.val('');
    }

    function getFields() {
        return {
            'name': nome.val(),
            'duration': dur.val(),
            'educationProject': edu.val()
            //'subjects': $('option:selected').val()
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
            getFields()

        ).success(function(courses) {
                 var tr = '<tr value='+courses["id"]+'>';
                tr += '<td>'+courses["name"]+
                '</td> <td>' +courses["duration"]+ '</td><td>'+courses["educationProject"]+'</td>'+
                '</td><td> <a class="btn btn-success" href="{{ s.edit_path }}" style="background: #10698F !important; margin-left: 10px"> <i class="glyphicon glyphicon-pencil"></i></a>'+
                '</td> <td> <button class="btn btn-danger" value="'+courses["id"]+'" style="margin-left: 10px"> <i class="glyphicon glyphicon-trash">' +
                '</i> </button> </td>';
                table.append(tr);
                clearAllInputs();
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