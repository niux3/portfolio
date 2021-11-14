<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<div id="target_a"></div>
<div id="target_b"></div>
<!-- <script id="item_tmpl" type="text/template">
    <div id="<%=id%>" class="<%=(i % 2 == 1 ? " even" : "")%>">
        <div class="grid_1 alpha right">
          <img class="righted" src="<%=profile_image_url%>"/>
        </div>
        <div class="grid_6 omega contents">
          <p><b><a href="/<%=from_user%>"><%= from_user %></a>:</b> <%=text%></p>
        </div>
      </div>

</script> -->

<script id="usageList" type="text/template">
    <table cellspacing='0' cellpadding='0' border='1'>
        <thead>
            <tr>
                <th>Id</th>
                <th>Name</th>
            </tr>
        </thead>
        <tbody>
            <%
            // repeat items
            for (var i = 0; i < users.length; i++) {
                var item = users[i],
                    key = i;
            %>
            <tr>
                <!-- use variables -->
                <td><%= key %></td>
                <td class="">
                    <!-- use %- to inject un-sanitized user input (see 'Demo of XSS hack') -->
                    <h3><%= item.name %></h3>
                    <p><%= item.interests %></p>
                </td>
            </tr>
            <% } %>
        </tbody>
    </table>
</script>
    <script src="app.js?v=<?= time() ?>"></script>
</body>
</html>
