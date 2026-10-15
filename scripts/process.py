import glob,os,json,csv
from PIL import Image
S='/workspace/paolo-cat/crops'
prods=[]
for f in sorted(glob.glob(S+'/prod-*.jpg')):
  pid=os.path.basename(f)[5:-4]  # P2-01
  im=Image.open(f).convert('RGB')
  for d,w in (('p',900),('t',480)):
    x=im.copy(); x.thumbnail((w,w*2)); x.save(f'img/{d}/{pid}.webp',quality=84 if d=='p' else 80)
  pg,pos=pid[1:].split('-')
  prods.append({'id':pid,'pagina':int(pg),'posicao':int(pos),'nome':f'Peça de vidro {pid}','preco':None,'img':pid,'w':im.width,'h':im.height})
json.dump(prods,open('data/produtos.json','w'),ensure_ascii=False,indent=1)
with open('/workspace/paolo-cat/precos-template.csv','w',newline='') as fh:
  w=csv.writer(fh,delimiter=';'); w.writerow(['id','pagina','posicao','imagem','nome','preco','peso_kg','comprimento_cm','largura_cm','altura_cm','observacao'])
  for p in prods: w.writerow([p['id'],p['pagina'],p['posicao'],f"crops/prod-{p['id']}.jpg",'','','','','','',''])
print(len(prods))
