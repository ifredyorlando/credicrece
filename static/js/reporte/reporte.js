// Message
const first_message = `Al contratar los servicios de ISSE, usted, en calidad de "Remitente", acuerda, en su nombre y en nombre del destinatario del Envío ("Destinatario") y de cualquier persona interesada en el Envío, que se aplicarán estos Términos y Condiciones. "Envío" significa todos los documentos o paquetes que viajan amparados por una guía aérea de transporte y que pueden ser transportados por el medio de transporte que ISSE considere idóneo, incluido el transporte aéreo, por carretera o a través de cualquier otro transportista.Se entenderá como guía aérea cualquier identificador del Envío o documento producido por los sistemas automatizados de ISSE o del Remitente como: etiqueta,código de barras,conocimiento de embarque aéreo o carta de porte, así como cualquier versión electrónica de los mismos. Cada Envío se transporta de conformidad con una responsabilidad limitada de acuerdo con lo establecido en el presente documento. Si el Remitente requiere una protección mayor, podrá concertar una protección que cubra el valor del envío, pagando un precio adicional (Véase más abajo para mayor información).La expresión "ISSE" incluye cualquier miembro de la red ISSE Express.`;
const message_left = `1. Despacho de aduanas\nISSE podrá llevar a cabo cualquiera de las siguientes actividades en nombre del Remitente o del Destinatario con el objeto de prestar sus servicios: (1) completar cualquier documento, modificar códigos de producto o servicio y pagar cualquier arancel, impuesto o sanción exigidos por la legislación y normativa aplicables ("Aranceles aduaneros"); (2) actuar como el agente de carga del Remitente a efectos de aduanas y controles de exportación y como Destinatario exclusivamente a efectos de designar a un agente de aduanas para tramitar el despacho de aduanas y la entrada; y (3) reconducir el Envío al agente de aduanas del Destinatario o a otra dirección a petición de cualquier persona que ISSE, a su razonable juicio, crea autorizada para ello.\n\n` +
    `2. Envíos inaceptables\nUn Envío es considerado inaceptable si: \n * No se realiza la declaración de aduanas cuando así lo exige la normativa aduanera aplicable. \n * Contiene artículos falsos, animales, lingotes de oro o plata, dinero, piedras preciosas, armas, explosivos y munición; restos humanos; artículos ilegales tales como marfil y narcóticos. \n * Está clasificado como sustancia tóxica, mercancía peligrosa, artículo prohibido o restringido por la IATA (International Air Transport Association), la ICAO (International Civil Aviation Organization), ADR (European Road Transport Regulation on dangerous goods), u otra organización pertinente ("Mercancía peligrosa"); \n * Su dirección es incorrecta, no está adecuadamente indicada \n * Su embalaje es defectuoso o inadecuado para su transporte seguro mediante un manejo y cuidado habitual. Contiene cualquier otro artículo que ISSE decida que no puede ser transportado de forma segura o legal. \n\n ` +
    `3. Entregas e imposibilidades de entrega Los Envíos no pueden ser enviados a apartados de correos o códigos postales. Los Envíos son entregados en la dirección del Destinatario facilitada por el Remitente pero no necesariamente a la persona indicada como Destinatario. Los envíos a direcciones que dispongan de un área central de recepción serán entregados en dicha área.\n ISSE podrá notificar al Destinatario una entrega a realizar o una entrega fallida. Se le podrán ofrecer al Destinatario opciones de entrega alternativas, tales como entrega otro día, entrega sin necesidad de firma, redirección del envío o recogida en un Punto de Venta de ISSE. El Remitente podrá descartar ciertas opciones de entrega bajo petición. Si el Envío es considerado inaceptable de acuerdo a la Sección 2, se ha infravalorado a efectos de aduanas, si el Destinatario no puede ser razonablemente identificado o localizado, o el Destinatario rechaza pagar los aranceles aduaneros y/u otros cargos del Envío, ISSE hará cuanto razonablemente esté a su alcance para devolver el Envío al Remitente por cuenta de éste y, de no ser posible, el Envío podrá ser abandonado, destruido, enajenado o vendido sin incurrir en ningún tipo de responsabilidad hacia el Remitente ni ninguna otra persona, aplicándose las ganancias contra los aranceles aduaneros, los cargos del Envío y costes administrativos relacionados, procediéndose a la devolución del resto de las ganancias generadas en la venta al Remitente. ISSE tendrá derecho a destruir cualquier Envío que la legislación aplicable impida devolver al Remitente, así como cualquier Envío de Mercancía peligrosa.\n\n` +
    `4. Inspección\nISSE se reserva el derecho de abrir e inspeccionar un Envío sin notificación previa, por motivos de seguridad, de aduanas o por otros motivos de regulación\n\n` +
    `5. Precio del Envío y tasas\nEl precio del Envío de ISSE se calcula en función del peso real o volumétrico por bulto, aplicándose el mayor, y cualquier bulto podrá ser pesado y medido de nuevo por ISSE para confirmar este cálculo. El Remitente o el Destinatario, cuando ISSE actúe en nombre del Destinatario, pagará o reembolsará a ISSE todos los cargos del Envío u otros cargos vencidos o derechos aduaneros debidos por los servicios prestados por ISSE o incurridos por ISSE en nombre del Remitente o del Destinatario. El pago de los derechos aduaneros podrá solicitarse antes de realizar la entrega. any Customs Duties on behalf of a Receiver who does not have an account Si ISSE utiliza su crédito con las autoridades aduaneras, anticipa cualquier importe en concepto de derechos aduaneros en nombre de un Destinatario que no tiene una cuenta con ISSE, ISSE estará autorizada a establecer un cargo.\n\n` +
    `6. Responsabilidad de ISSE\n6.1 La responsabilidad de ISSE en relación a cualquier Envío transportado por aire (incluyendo el transporte auxiliar por carretera o paradas en ruta) está limitada por el Convenio de Montreal o el Convenio de Varsovia, según aplique o, en ausencia de dicho Convenio, al menor de los siguientes importes (i) el valor de mercado o el valor declarado o (ii) 19 Derechos Especiales de Giro por kilogramo (aproximadamente USD 26.00 por kilogramo). Dichos límites también serán de aplicación para todo el resto de formas de transporte, excepto cuando los Envíos se hayan transportado únicamente por carretera, en cuyo caso aplicarán los límites establecidos a continuación.`;
const message_right = `Para envíos internacionales transportados por carretera, la responsabilidad de ISSE está o se considera limitada por el Convenio para el Transporte Internacional de Mercancías por Carretera (CMR) al menor de los siguientes importes (i) valor actual de mercado o el valor declarado o (ii) 8,33 Derechos Especiales de Giro por kilogramo (aproximadamente USD 14.00 por kilogramo). Dichos límites también serán de aplicación para el transporte nacional de mercancías por carretera, en ausencia de legislación imperativa o de límites de responsabilidad inferiores establecidos en la legislación de transporte nacional aplicable Si el Remitente requiere extender el límite de responsabilidad, podrá adquirir el producto de Protección de Valor del Envío pagando un precio adicional, tal y como se indica en la Sección 8, o bien concertar su propio seguro. La responsabilidad de ISSE queda limitada estrictamente a la pérdida y daño directo al Envío y a los límites por kilogramo especificados en la presente Sección 6. Quedan excluidos todos los demás tipos de pérdida o daño (tales como, a título meramente enunciativo, el lucro cesante, la pérdida de intereses y de futuros negocios), con independencia de que dicha pérdida o daño sea indirecto o de especial consideración, e incluso si se hubiera avisado a ISSE sobre el riesgo de dicha pérdida o daño.\n\n`+
    `6.2 ISSE hará cuanto razonablemente esté a su alcance para entregar el Envío de acuerdo a los tiempos de tránsito habituales de ISSE, pero estos tiempos de tránsito no son vinculantes y no forman parte del contrato. ISSE no se hace responsable de pérdidas o daños ocasionados por demoras, pero para ciertos envíos, el Remitente podrá solicitar una compensación limitada por retraso de acuerdo a los términos y condiciones de Garantía de Devolución, que están disponibles en el sitio web de ISSE o en el Departamento de Atención al Cliente de ISSE.\n\n` +
    `7. Reclamaciones\nTodas las reclamaciones deben ser enviadas por escrito a ISSE en un plazo de treinta (30) días a partir de la fecha en que ISSE aceptó el Envío, a falta de lo cual ISSE quedará eximida de toda responsabilidad. Las reclamaciones están limitadas a una por Envío y su finiquito será completo y final para toda pérdida y daño en relación a dicho Envío. \n\n` +
    `8. Protección del Valor del Envío\n ISSE podrá concertar una protección que cubra el valor en caso de pérdida o daño del Envío, siempre y cuando el Remitente así se lo indique a ISSE por escrito, rellenando la casilla designada al efecto en el anverso de la Guía Aérea, o a través de los sistemas automatizados de ISSE, y pague el precio aplicable. La Protección del Valor del Envío no cubre daños o pérdidas indirectas, ni las pérdidas o daños ocasionados por demoras.\n\n` +
    `9. Circunstancias ajenas al control de ISSE\n ISSE no es responsable de las pérdidas o daños derivados de circunstancias ajenas a su control. Estas circunstancias incluyen pero no se limitan a las siguientes: daño eléctrico o magnético a imágenes electrónicas o fotográficas, datos o grabaciones o borrado de los elementos mencionados anteriormente; cualquier defecto o característica relacionada con la naturaleza del Envío, incluso, si estos son conocidos por ISSE; cualquier acción u omisión por parte de personas no empleadas o contratadas por ISSE - ej. Remitente, Destinatario, terceros, aduanas u otros representantes gubernamentales; "Fuerza Mayor" - ej. terremotos, huracanes, tormentas, inundaciones, niebla, guerras, accidentes aéreos, disturbios, embargos, conmoción civil o acciones sindicales.\n\n` +
    `10. Garantías e indemnización del Remitente\nEl Remitente indemnizará y mantendrá indemne a ISSE por cualquier daño o pérdida que se derive del incumplimiento por parte del Remitente, de cualquier legislación o normativa aplicable, y del incumplimiento por parte del Remitente de cualquiera de las siguientes declaraciones y garantías: \n* Toda la información facilitada por el Remitente o sus representantes es completa y exacta; \n* El envío es aceptable para su transporte de acuerdo a la Sección 2; \n* El Envío fue preparado en instalaciones seguras por personal fiable y se protegió de interferencias no autorizadas durante su preparación, almacenamiento y traslado del mismo a ISSE; \n* El Remitente ha cumplido con la legislación aplicable en materia de aduanas, importación, exportación, protección de datos, sanciones, embargos y otras leyes y normativas; y \n* El Remitente ha obtenido todos los consentimientos necesarios en relación con los datos personales facilitados a ISSE, incluyendo información del Destinatario que podrá ser solicitada para el transporte, despacho de aduanas y la entrega, como la dirección de correo electrónico y número de teléfono móvil.\n\n`+
    `11. Ruta \nEl Remitente acepta que el Envío pueda transportarse por cualquier ruta y pueda ser desviado, incluida la posibilidad de parar en lugares de escala intermedios.\n\n`+
    `12. Legislación aplicable\n Cualquier controversia que se derive o esté relacionada con estos Términos y Condiciones estará sujeta a la jurisdicción de los Tribunales del país de origen del Envío y se regirá igualmente por la legislación de dicho país. El remitente se somete irrevocablemente a dicha jurisdicción, a menos que la ley aplicable indique lo contrario. No obstante, si la legislación aplicable permitiera la elección de fuero o de jurisdicción, ésta será la determinada por ISSE.\n\n`+
    `13. Nulidad e ineficacia\nSi alguna de las cláusulas o parte de las mismas fueran nulas o ineficaces, permanecerán subsistentes el resto de los Términos y Condiciones no afectados por la nulidad o ineficacia.`;
// cookie
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

// event
$('#reporte').on('click', () => {
    $.ajax({
        type: 'get',
        url: url_guia.replace('0', guia_id),
        headers: { 'X-CSRFToken': getCookie('csrftoken')},
        success: (data) => {
            if(data.hasOwnProperty('result') && data.result.length >= 0) {
                GenerateReports(data.result);
            } else {
                toastr.error('Error al obtener la informacion', 'Error');
            }
        },
        error: (error) => {
            const mensaje = error.responseJSON ? error.responseJSON.result : 'Ocurrio un error al contactar con el servidor';
            toastr.error(mensaje, 'Error');
        }
    });
});

function GenerateReports(list) {
    const { jsPDF } = window.jspdf;
    let doc = new jsPDF();
    let height = 15;
    GenerateTableTerminosCondiciones(doc, height);
    doc.addPage();
    GenerateTableReciboEnvio(doc, height, list);
    doc.setFontSize(11);
    doc.text('2020 © ISSE EXPRESS', 15, 280);
    doc.setProperties({title: 'ReciboEnvio'});
    window.open(doc.output('bloburl', '_blank'));
}

    // create of the table
    function GenerateTableTerminosCondiciones(doc, height) {
        doc.autoTable({
            startY: height,
            showHead: 'firstPage',
            margin: { top: 15},
            theme: 'plain',
            head: [
                [{content: 'TÉRMINOS Y CONDICIONES DE TRANSPORTE DE ISSE EXPRESS',  colSpan: 2, styles: {fontSize: 10}}],
                [{content: '("Términos y Condiciones")',  colSpan: 2}],
                [{content: 'AVISO IMPORTANTE:',  colSpan: 2}]
            ],
            headStyles: {fontStyle: 'bold', fillColor: [255, 255, 255], textColor: Color = 0, fontSize: 7, halign: 'center'},
            styles: {halign: 'left', fontSize: 6.6, textColor: Color = 0, lineWidth: 0},
            columnStyles: {0: {cellWidth: 84}},
            body: [
                [{content: first_message, colSpan: 2}],
                [message_left, message_right],
            ]
        });
    }
    function GenerateTableReciboEnvio(doc, height, body) {
        doc.autoTable({
            startY: 5,
            showHead: 'firstPage',
            margin: { top: 15},
            theme: 'plain',
            head: [
                ['', '', '',  ''],
                [{content: 'Recibo del envío',  colSpan: 4}]
            ],
            headStyles: {fontStyle: 'bold', fillColor: [255, 255, 255], textColor: Color = 0, fontSize: 20, halign: 'center'},
            styles: {halign: 'left', fontSize: 10, textColor: Color = 0, lineWidth: 0},
            columnStyles: {0: {cellWidth: 47}, 1: {cellWidth: 47}, 2: {cellWidth: 47}},
            body: body,
            didDrawCell: (data) => {
                if (data.section === 'body' && (data.row.index === 0 || data.row.index === 10)) {
                    doc.setDrawColor(0, 0, 0);
                    doc.line(data.cell.x, data.cell.y, data.cell.x + data.cell.width, data.cell.y);
                }
            }
        });
    }