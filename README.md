# Paolo Tabacaria – loja online
Site estático (GitHub Pages): https://ricksanches5567-art.github.io/paolo-tabacaria/

- Produtos: `data/produtos.json` (gerado por `scripts/process.py` a partir das fotos do catálogo 2026). Códigos = página-posição (ex.: P2-03).
- Preços: enquanto `preco` for `null` a peça mostra "Preço em breve" e não pode ir para a sacola.
- Compra online: `vendasAtivas` em `config.js` (desligada). O servidor de pagamento é um Worker separado e só vende peças com preço > 0.
- Vídeo: `scripts/film.py` gera `video/hero-*.mp4/webm` a partir das fotos.
- Nunca coloque senha, token ou dados de clientes neste repositório (é público).
