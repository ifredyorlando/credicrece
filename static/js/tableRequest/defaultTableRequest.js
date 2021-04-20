// Function request ajax table
// function custom for request table
/**
 *
 * @param url
 * @param language_url
 * @param columns
 * @param data
 * @returns {{serverSide: boolean, columns: *, searching: boolean, responsive: boolean, processing: boolean, destroy: boolean, language: {url: *}, sDom: string, lengthMenu: number[][], ajax: {headers: {"X-CSRFToken": *}, data: *, type: string, url: *}}}
 */
let time;

function postDefaultTableRequest(url, language_url, columns, data){
    return  {
        ajax: {
            url: url,
            type: 'post',
            data: data,
            headers: { 'X-CSRFToken': getCookie('csrftoken')},
        },
        language: {
            url: language_url
        },
        lengthMenu: [[10, 25, 50], [10, 25, 50]],
        searching: true,
        sDom: "<tr><'row'<'col-md-12 col-lg-4'l><'col-md-12 col-lg-8 text-right'i><'col-md-12'p>>",
        processing: true,
        serverSide: true,
        responsive: true,
        destroy: true,
        columns: columns
    };
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function eliminarData(url, table='#data-table') {
    Swal.fire({
        title: '¿Desea eliminar el registro?',
        text: 'Esto no se podra revertir',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Si, Eliminar',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#D1504A',
        cancelButtonColor: '#CAC7C7'
    }).then((respuesta) => {
        if(respuesta.value) {
          $.ajax({
            url: url,
            method: 'POST',
            headers: { 'X-CSRFToken': getCookie('csrftoken')},
            success: (data) => {
                if(data.result === 'OK') {
                    Swal.fire('Exito', 'Se ha eliminado el registro', 'success');
                    $(table).DataTable().ajax.reload(null, false);
                } else {
                    Swal.fire('Error', 'Ha ocurrido un error al eliminar', 'error');
                }
            },
            error: (error) => {
                const mensaje = error.responseJSON ? error.responseJSON.result : 'No se puede eliminar el registro';
                Swal.fire('Error', mensaje, 'error');
            }
          });
        }
    });
}

function activarData(url, table='#data-table') {
    Swal.fire({
        title: '¿Desea activar el registro?',
        text: 'Este registro aparecera en el listado principal',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Si, Activar',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#52adc8',
        cancelButtonColor: '#CAC7C7'
    }).then((respuesta) => {
        if(respuesta.value) {
          $.ajax({
            url: url,
            method: 'POST',
            headers: { 'X-CSRFToken': getCookie('csrftoken')},
            success: (data) => {
                if(data.result === 'OK') {
                    Swal.fire('Exito', 'Se ha activado el registro', 'success');
                    $(table).DataTable().ajax.reload(null, false);
                } else {
                    Swal.fire('Error', 'Ha ocurrido un error al eliminar', 'error');
                }
            },
            error: (error) => {
                const mensaje = error.responseJSON ? error.responseJSON.result : 'No se puede eliminar el registro';
                Swal.fire('Error', mensaje, 'error');
            }
          });
        }
    });
}

function FormSubmit(content, modal, table, editar = true) {
    const form = content + ' form';
    $(form).submit((e) => {
        e.preventDefault();
        $.ajax({
            type: $(form).attr('method'),
            url: $(form).attr('action'),
            data: $(form).serialize(),
            headers: { 'X-CSRFToken': getCookie('csrftoken')},
            success: (xhr, ajaxOptions, throwError) => {
                if ($(xhr).find('.is-invalid').length > 0) {
                    $(modal).find(content).html(xhr);
                    FormSubmit(content, modal, table, editar);
                } else {
                    $(table).DataTable().ajax.reload(null, false);
                    if (editar) {
                        $(modal).find(content).html('');
                        $(modal).modal('hide');
                        toastr.warning('Se ha actualizado el registro exitosamente', 'Actualizado');
                    } else {
                        $(modal).find(content).html(xhr);
                        FormSubmit(content, modal, table, editar);
                        toastr.success('Se agrego el registro exitosamente', 'Completado');
                    }
                }
            },
            error: (xhr, ajaxOptions, throwError) => {
                const mensaje = error.responseJSON ? error.responseJSON.result : 'Ocurrio un error al contactar con el servidor';
                Swal.fire('Error', mensaje, 'error');
            }
        })
    });
}


function dataFormModal(url, editar = true , content='#modal-content', modal='#modal-base', table='#data-table') {
    $(content).load(url, () => {
        $(modal).modal('show');
        FormSubmit(content, modal, table, editar);
    });
}

$('#buscador').on('keyup search input past cut', () => {
    clearTimeout(time);
    time = setTimeout(() => {
        $('#data-table').DataTable().search($('#buscador').val()).draw()
    }, 600);
});
$('#buscador-responsivo').on('keyup search input past cut', () => {
    clearTimeout(time);
    time = setTimeout(() => {
        $('#data-table').DataTable().search($('#buscador-responsivo').val()).draw()
    }, 600);
});