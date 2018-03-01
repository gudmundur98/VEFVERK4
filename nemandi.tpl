<!DOCTYPE html>
<html>
<head>
    <title>Kennitala</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/css.css">
</head>
<body>
    <%
    nafn = "Ekki til"
    braut = "Ekki til"
    for nemandi in bekkur["nemendur"]:
        if nemandi["kt"] == kt:
            nafn = nemandi["nafn"]
            braut = nemandi["braut"]
        end
    end %>
    <h1>Kennitala : {{kt}}</h1>
    <h1>Nafn : {{nafn}}</h1>
    <h1>Braut : {{braut}}</h1>


</body>
</html>