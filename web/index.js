function generateKML() {
  cords = document.getElementById("cords").value;
  console.log(eel.generate(cords));
}
const form = document.getElementById("form");
const erro = document.getElementById("erro-text");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  generateKML();
});

// erro.innerHTML = "|--| Arquivo gerado com sucesso |--|";
// erro.classList.remove("erro");
// erro.classList.remove("fail");
// erro.classList.add("sucess");

// if () {
//     erro.innerHTML = "|--| Erro ao gerar o arquivo KML |--|";
//     erro.classList.remove("erro");
//     erro.classList.remove("sucess");
//     erro.classList.add("fail");
