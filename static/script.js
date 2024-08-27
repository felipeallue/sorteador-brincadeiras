let anguloAtual = 0;

document.getElementById('girar-btn').addEventListener('click', () => {
    const roleta = document.getElementById('roleta');
    
    const anguloGirar = Math.floor(Math.random() * 360) + 1080; 
    
    anguloAtual += anguloGirar;
    
    roleta.style.transform = `rotate(${anguloAtual}deg)`;
    
    setTimeout(() => {
        const brincadeiras = [
            {
                nome: "Pega-pega",
                descricao: "Uma criança corre atrás das outras para tentar pegá-las. Quem for pego se torna o pegador.",
                imagem: "https://via.placeholder.com/200?text=Pega-pega"
            },
            {
                nome: "Esconde-esconde",
                descricao: "Uma criança conta até um número específico enquanto as outras se escondem. O objetivo é encontrar todas as outras crianças.",
                imagem: "https://via.placeholder.com/200?text=Esconde-esconde"
            },
            {
                nome: "Queimada",
                descricao: "Dois times tentam acertar os jogadores adversários com uma bola. Quem for acertado sai do jogo.",
                imagem: "https://via.placeholder.com/200?text=Queimada"
            },
            {
                nome: "Cabo de guerra",
                descricao: "Dois times puxam uma corda em direções opostas, e o time que conseguir puxar o outro para o seu lado vence.",
                imagem: "https://via.placeholder.com/200?text=Cabo+de+guerra"
            },
            {
                nome: "Dança das cadeiras",
                descricao: "Crianças dançam ao redor de cadeiras, e quando a música para, devem se sentar. Quem ficar sem cadeira sai do jogo.",
                imagem: "https://via.placeholder.com/200?text=Dança+das+cadeiras"
            },
            {
                nome: "Amarelinha",
                descricao: "Desenhe um diagrama no chão e pule com um pé ou dois seguindo a sequência numérica.",
                imagem: "https://via.placeholder.com/200?text=Amarelinha"
            },
            {
                nome: "Batata-quente",
                descricao: "As crianças passam um objeto de mão em mão ao som de uma música. Quando a música parar, quem estiver segurando o objeto sai.",
                imagem: "https://via.placeholder.com/200?text=Batata-quente"
            },
            {
                nome: "Corrida do saco",
                descricao: "Crianças entram em sacos e pulam até a linha de chegada. Quem chegar primeiro vence.",
                imagem: "https://via.placeholder.com/200?text=Corrida+do+saco"
            },
            {
                nome: "Telefone sem fio",
                descricao: "Uma criança sussurra uma frase no ouvido de outra, e a mensagem vai passando até o último jogador. A frase final é comparada à original para ver se mudou.",
                imagem: "https://via.placeholder.com/200?text=Telefone+sem+fio"
            },
            {
                nome: "Elefante colorido",
                descricao: "Um jogador diz uma cor e as outras crianças precisam tocar em algo com essa cor o mais rápido possível.",
                imagem: "https://via.placeholder.com/200?text=Elefante+colorido"
            }
        ];

        const segmentoSelecionado = Math.floor(((anguloAtual % 360) / 360) * brincadeiras.length);
        const brincadeira = brincadeiras[segmentoSelecionado];
        
       
        document.getElementById('resultado').textContent = `Brincadeira sorteada: ${brincadeira.nome}`;
        document.getElementById('descricao').textContent = `Descrição: ${brincadeira.descricao}`;
        document.getElementById('brincadeira-imagem').src = brincadeira.imagem;
    }, 4000); 
});
