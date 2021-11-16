<!doctype html>
<html lang="us">
<head>
	<meta charset="utf-8">
	<title>jQuery UI Example Page</title>
	<link href="jquery-ui.css" rel="stylesheet">
	<style>
	body{
		font-family: "Trebuchet MS", sans-serif;
		margin: 50px;
	}
	.demoHeaders {
		margin-top: 2em;
	}
	#dialog-link {
		padding: .4em 1em .4em 20px;
		text-decoration: none;
		position: relative;
	}
	#dialog-link span.ui-icon {
		margin: 0 5px 0 0;
		position: absolute;
		left: .2em;
		top: 50%;
		margin-top: -8px;
	}
	#icons {
		margin: 0;
		padding: 0;
	}
	#icons li {
		margin: 2px;
		position: relative;
		padding: 4px 0;
		cursor: pointer;
		float: left;
		list-style: none;
	}
	#icons span.ui-icon {
		float: left;
		margin: 0 4px;
	}
	.fakewindowcontain .ui-widget-overlay {
		position: absolute;
	}
	select {
		width: 200px;
	}
	</style>
</head>
<body>
<table>
    <thead>
        <tr>
            <th>order</th>
            <th>name</th>
        </tr>
    </thead>
    <tbody class="sortable">
        <?php for($i = 0; $i < 10; $i++): ?>
        <tr>
            <th><?= $i + 1 ?></th>
            <th>item <?= $i + 1 ?></th>
        </tr>
        <?php endfor; ?>
    </tbody>
</table>

<script src="external/jquery/jquery.js"></script>
<script src="jquery-ui.js"></script>
<script>
    $(function(){
        $('.sortable').sortable({
            stop: function( event, ui ) {
                console.log(event);
                console.log(ui);
            }
        });
    });
</script>
</body>
</html>
