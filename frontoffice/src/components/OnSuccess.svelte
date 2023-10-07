<script>
    export let dataForm

    $: appointment = dataForm['appointment'] !== undefined ? dataForm['appointment'] : false
    $: date = dataForm['date_appointment'] !== undefined ? new Date(dataForm['date_appointment']) : new Date()
    $: hour = dataForm['hour_appointment'] !== undefined ? dataForm['hour_appointment'].replace(':', ' h ') : ''
    $: phone = dataForm['phone'] !== undefined ? dataForm['phone'] : ''
    $: dateDayWeek = date.getDay()
    $: dateNumber = date.getDate()
    $: dateMonth = date.getMonth()
    $: dateYear = date.getFullYear()

    let months = [
            'janvier',
            'février',
            'mars',
            'avril',
            'mai',
            'juin',
            'juillet',
            'août',
            'septembre',
            'octobre',
            'novembre',
            'décembre',
        ],
        days = [
            'dimanche',
            'lundi',
            'mardi',
            'mercredi',
            'jeudi',
            'vendredi',
            'samedi'
        ]
    

</script>
<p>{JSON.stringify(dataForm)}</p>
<p>{typeof dataForm['appointment']}</p>

<div class="on-success">
    <h1>Merci !</h1>
    <p>Bonjour {dataForm['civility']} {dataForm['lastname']}, <br><br>Le mail que vous m'avez transmis m'a bien été remis. Je vous transmettrai dans les meilleurs délais une réponse.</p>
    
    {#if appointment }
        
    <p>Je prends note du rendez vous que vous m'avez soumis</p>
        <dl>
            <dt>Date</dt>
            <dd>{days[dateDayWeek]} {dateNumber} {months[dateMonth]} {dateYear}</dd>
            <dt>Heure</dt>
            <dd>{hour}</dd>
            <dt>Téléphone</dt>
            <dd>{phone}</dd>
        </dl>
    {/if}
    <p>Si vous avez des questions annexes, n'hésitez pas à me contacter. Je me ferai un plaisir de vous répondre au mieux que je pourrai.<br> En ayant le plaisir de converser ou de discuter avec vous, <br>bien à vous et à bientôt</p>
</div>