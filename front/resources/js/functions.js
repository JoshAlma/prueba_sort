
async function submitForm(){
  let txt_practicante = document.getElementById('txt_practicante')
  let txt_array = document.getElementById('txt_array')
  let data = {
      nombre : txt_practicante.value,
      array : txt_array.value
  }
  try {
      const response = await fetch("http://127.0.0.1:8000/acomodar_numeros", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
  
      console.log("Success:", response);

      const result = await response.json();
      console.log("Success:", result);

      if (response.status == 200){
        let div_table = document.getElementById('resultado')
        let div_msg = document.getElementById('msg')
        let div_formulario = document.getElementById('formulario')

        div_table.innerHTML = ""
        div_msg.innerHTML =""

        let table = ''
        let indice = 1
        table += '<table style="width:100%" >'
        table += '<tr> <th style="width:50%">#</th> <th style="width:50%">Dato</th> </tr>'
        result.sorted_array.forEach((num) => {
          table += '<tr> <td style="width:50%" class = "negrita">'+ indice +'</td> <td style="width:50%">'+ num +'</td> </tr>'
          indice += 1
        })
        table += '</table><br>'

        table += '<p class = "max"> Max: '+ result.max +'</p>'
        table += '<p class = "min"> Min: '+ result.min +'</p><br>'

        div_table.innerHTML = table

        div_table.style.display = 'block'
        div_formulario.style.height = "100%"

      }
      else if(response.status == 401){
        let div_table = document.getElementById('resultado')
        let div_msg = document.getElementById('msg')
        let div_formulario = document.getElementById('formulario')

        div_table.innerHTML = ""
        div_msg.innerHTML =""

        div_msg.innerHTML = '<p>'+ result.message + '</p>'
        div_msg.style.display = 'block'
        div_formulario.style.height = "50%"
      }



  } catch (error) {
      console.error(error);
  }
}

