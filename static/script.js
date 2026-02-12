let anguloAtual = 0;

document.getElementById('girar-btn').addEventListener('click', () => {
    const roleta = document.getElementById('roleta');
    
    const anguloGirar = Math.floor(Math.random() * 360) + 1080; 
    
    anguloAtual += anguloGirar;
    
    roleta.style.transform = `rotate(${anguloAtual}deg)`;
    
    setTimeout(() => {
        // Buscar brincadeira do servidor
        fetch('/sortear')
            .then(response => response.json())
            .then(brincadeira => {
                document.getElementById('resultado').textContent = `Brincadeira sorteada: ${brincadeira.nome}`;
                document.getElementById('descricao').textContent = `Descrição: ${brincadeira.descricao}`;
            })
            .catch(error => {
                console.error('Erro ao sortear brincadeira:', error);
                document.getElementById('resultado').textContent = 'Erro ao sortear brincadeira';
            });
    }, 4000); 
});
