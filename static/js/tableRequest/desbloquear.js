function desbloquear(url, name, bloqueo, table='#data-table') {
    Swal.fire({
        title: `¿Desea desbloquer al usuario ${name}?`,
        text: `¡Este usuario fue bloqueado por tener ${bloqueo} intentos fallidos al iniciar sesión!`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Si, Desbloquear',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#338AFF',
        cancelButtonColor: '#CAC7C7'
    }).then((respuesta) => {
        if(respuesta.value) {
          $.ajax({
            url: url,
            method: 'POST',
            headers: { 'X-CSRFToken': getCookie('csrftoken')},
            success: (data) => {
                if(data.result === 'OK') {
                    Swal.fire('Exito', 'Se ha desbloqueado el usuario', 'warning');
                    $(table).DataTable().ajax.reload(null, false);
                } else {
                    Swal.fire('Error', 'Ha ocurrido un error al desbloquear el usuario', 'error');
                }
            },
            error: (error) => {
                const mensaje = error.responseJSON ? error.responseJSON.result : 'No se puede desbloquear el usuario';
                Swal.fire('Error', mensaje, 'error');
            }
          });
        }
    });
}