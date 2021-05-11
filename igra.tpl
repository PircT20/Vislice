% import model

<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <h2>{{igra.pravilni_del_gesla()}}</h2>

  <p>Nepravilni ugibi: <b>{{igra.nepravilni_ugibi()}}</b></p>

  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  <form action="/igra/{{id_igre}}/"method="post">
   Črka: <input type= "text" name="crka" />
   <button type="submit">Ugibaj</button>
  </form>
</body>

</html>


