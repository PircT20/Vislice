% import model

<!DOCTYPLE html>
<html>
<head>
<meta charset="UTF-8"
</head>
<body>

    <h1><Vislice></h1>

    <h2>{{igra.pravilni_del_gesla()}}</h2>

    <p>Nepravilni ugibi: <b>{{igra.nepravilni_ugibi()}}</b></p>

    <img src="/img/{{igra.stevilo.napak()}}.jpg" alt="obesanje">
% if stanje == model.ZMAGA:

    <h1>ZMAGA</h1>
    <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

% elif stanje == model.PORAZ:

    <h1>PORAZ</h1>
    <pravilno geslo: <b>{{igra.geslo}}</b></p>
    <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

% else:

    <form action ="/igra/{{id_igre}}/" method="" >
    Črka: <input type="text" name="crka" />
    <button type="submit">Ugibaj</button>
    </form>

% end

</body>

</html>
