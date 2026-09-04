# -*- coding: utf-8 -*-
"""Gerador das paginas de servico e regiao do site Reis Lima Higienizacao.
Rode:  python _build/gerar-paginas.py     (a partir da raiz do projeto)
"""
import os, datetime
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE   = "https://reislimahigienizacao.com.br"
WA     = "5511982445797"
TEL1   = "(11) 98244-5797"
TEL2   = "(11) 98168-6274"
TEL1_R = "+5511982445797"
TEL2_R = "+5511981686274"
EMAIL  = "reislimahigienizacao@gmail.com"
CNPJ   = "43.846.059/0001-08"
NOME   = "Reis Lima Higienização"
GA     = "G-0SX530XN4F"
HOJE   = datetime.date.today().isoformat()

def zap(msg):
    return "https://wa.me/" + WA + "?text=" + quote(msg)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />'
         '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800'
         '&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />')

CSS = """
  * { box-sizing: border-box; }
  body { margin:0; font-family:Manrope,Helvetica,Arial,sans-serif; color:#003366; background:#FFFFFF; -webkit-font-smoothing:antialiased; text-wrap:pretty; }
  a { color:#0072FF; text-decoration:none; }
  a:hover { color:#00C6FF; }
  h1,h2,h3,h4 { font-family:"Plus Jakarta Sans",Helvetica,Arial,sans-serif; margin:0; letter-spacing:-0.02em; }
  p { margin:0; }
  ul { margin:0; padding:0 0 0 20px; }
  li { font-size:15.5px; line-height:1.75; color:#5B6B79; margin-bottom:8px; }
  .wrap { max-width:1120px; margin:0 auto; padding:0 clamp(16px,4vw,28px); }
  .sec { padding:clamp(48px,7vw,84px) 0; }
  .card { background:#FFFFFF; border:1px solid #DFE3E6; border-radius:20px; padding:28px 26px; display:flex; flex-direction:column; gap:10px; transition:transform .22s ease, box-shadow .22s ease; }
  .card:hover { transform:translateY(-5px); box-shadow:0 18px 40px rgba(0,114,255,.12); }
  .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr)); gap:20px; }
  .kicker { font-size:13px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:#00C6FF; }
  .h2 { font-size:clamp(25px,4.4vw,38px); line-height:1.12; font-weight:800; color:#003366; }
  .lead { font-size:clamp(15.5px,1.7vw,17.5px); line-height:1.7; color:#5B6B79; }
  .btn { display:inline-flex; align-items:center; gap:10px; background:#25D366; color:#FFF; padding:15px 26px; border-radius:999px; font-weight:700; font-size:15.5px; box-shadow:0 8px 22px rgba(37,211,102,.28); }
  .btn:hover { filter:brightness(1.06); color:#FFF; }
  .btn-o { display:inline-flex; align-items:center; border:1.5px solid rgba(255,255,255,.45); color:#FFF; padding:15px 26px; border-radius:999px; font-weight:700; font-size:15.5px; }
  .btn-o:hover { background:rgba(255,255,255,.12); color:#FFF; }
  .chip { display:inline-block; font-size:14px; font-weight:600; color:#003366; background:#F1F5F9; border:1px solid #E2E8F0; border-radius:999px; padding:8px 15px; margin:0 8px 8px 0; }
  .fab { position:fixed; bottom:18px; right:18px; z-index:80; display:flex; align-items:center; gap:10px; background:#25D366; color:#FFF; padding:15px 22px; border-radius:999px; font-weight:700; font-size:15px; box-shadow:0 14px 34px rgba(0,0,0,.28); animation:rl-float 3.2s ease-in-out infinite; }
  @keyframes rl-float { 0%,100% { transform:translateY(0);} 50% { transform:translateY(-6px);} }
  @media (max-width:600px){ .fab{ padding:13px 18px; font-size:14px; } }
"""

def head(titulo, descricao, url, imagem, jsonld):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{titulo}</title>
<meta name="description" content="{descricao}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="{NOME}" />
<meta name="geo.region" content="BR-SP" />
<meta name="geo.placename" content="São Paulo" />
<link rel="canonical" href="{url}" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="pt_BR" />
<meta property="og:site_name" content="{NOME}" />
<meta property="og:title" content="{titulo}" />
<meta property="og:description" content="{descricao}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{SITE}/assets/{imagem}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{titulo}" />
<meta name="twitter:description" content="{descricao}" />
<meta name="twitter:image" content="{SITE}/assets/{imagem}" />
<link rel="icon" type="image/x-icon" href="/assets/favicon.png" />
<link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon.png" />
{FONTS}
<style>{CSS}</style>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA}');
</script>
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
"""

def header():
    return f"""<header style="position:sticky; top:0; z-index:50; background:rgba(255,255,255,.94); backdrop-filter:blur(12px); border-bottom:1px solid #E4E7E9">
  <div class="wrap" style="padding-top:10px; padding-bottom:10px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px 20px">
    <a href="/" style="display:flex; align-items:center; flex:0 0 auto">
      <img src="/assets/logo-reis-lima-hi.png" alt="{NOME} — higienização de estofados e vidros em São Paulo" width="200" height="64" style="height:clamp(56px,8vw,68px); width:auto; display:block" />
    </a>
    <nav style="display:flex; align-items:center; gap:18px; font-size:14.5px; font-weight:600; color:#4A5A66; flex:1 1 auto; min-width:0; overflow-x:auto; scrollbar-width:none; padding:4px 0">
      <a href="/" style="color:#4A5A66; white-space:nowrap">Início</a>
      <a href="/#servicos" style="color:#4A5A66; white-space:nowrap">Serviços</a>
      <a href="/#galeria" style="color:#4A5A66; white-space:nowrap">Galeria</a>
      <a href="/#depoimentos" style="color:#4A5A66; white-space:nowrap">Depoimentos</a>
      <a href="/#faq" style="color:#4A5A66; white-space:nowrap">FAQ</a>
      <a href="/#contato" style="color:#4A5A66; white-space:nowrap">Contato</a>
    </nav>
    <a href="{zap('Olá! Gostaria de um orçamento.')}" rel="noopener" target="_blank" class="btn" style="padding:11px 20px; font-size:14.5px; white-space:nowrap; flex:0 0 auto">
      <span style="width:8px; height:8px; border-radius:50%; background:#FFF; display:block"></span>Orçamento no WhatsApp</a>
  </div>
</header>
"""

def breadcrumb(nome):
    return f"""<div style="background:#F5F5F5; border-bottom:1px solid #E4E7E9">
  <div class="wrap" style="padding-top:12px; padding-bottom:12px; font-size:13.5px; color:#5B6B79">
    <a href="/" style="color:#0072FF; font-weight:600">Início</a>
    <span style="padding:0 8px">›</span><span>{nome}</span>
  </div>
</div>
"""

def footer():
    ls = "".join(f'<a href="/{s["slug"]}/" style="font-size:14.5px; color:#9FD3EA; line-height:1.9">{s["menu"]}</a>' for s in SERVICOS)
    lr = "".join(f'<a href="/{r["slug"]}/" style="font-size:14.5px; color:#9FD3EA; line-height:1.9">{r["menu"]}</a>' for r in REGIOES)
    return f"""<footer style="background:#003366; color:#9FD3EA">
  <div class="wrap" style="padding-top:clamp(40px,6vw,58px); padding-bottom:26px; display:grid; grid-template-columns:repeat(auto-fit,minmax(min(230px,100%),1fr)); gap:clamp(28px,4vw,44px)">
    <div style="display:flex; flex-direction:column; gap:14px; align-items:flex-start">
      <img src="/assets/logo-reis-lima-hi.png" alt="{NOME}" width="200" height="64" loading="lazy" style="height:64px; width:auto; display:block; background:#FFF; border-radius:14px; padding:10px 16px" />
      <p style="font-size:14.5px; line-height:1.7; max-width:34ch">Higienização de estofados, colchões, cadeiras e tapetes, limpeza e cristalização de vidros e fachadas em São Paulo e região.</p>
      <p style="font-size:13px; line-height:1.7">CNPJ {CNPJ}</p>
    </div>
    <div style="display:flex; flex-direction:column">
      <span style="font-family:'Plus Jakarta Sans'; font-size:15px; font-weight:700; color:#FFF; margin-bottom:10px">Serviços</span>{ls}
    </div>
    <div style="display:flex; flex-direction:column">
      <span style="font-family:'Plus Jakarta Sans'; font-size:15px; font-weight:700; color:#FFF; margin-bottom:10px">Regiões atendidas</span>{lr}
    </div>
    <div style="display:flex; flex-direction:column; gap:8px">
      <span style="font-family:'Plus Jakarta Sans'; font-size:15px; font-weight:700; color:#FFF; margin-bottom:2px">Contato</span>
      <a href="{zap('Olá! Gostaria de um orçamento.')}" rel="noopener" target="_blank" style="font-size:14.5px; color:#9FD3EA">WhatsApp {TEL1}</a>
      <a href="tel:{TEL2_R}" style="font-size:14.5px; color:#9FD3EA">Telefone {TEL2}</a>
      <a href="mailto:{EMAIL}" style="font-size:14.5px; color:#9FD3EA">{EMAIL}</a>
      <span style="font-size:14.5px; line-height:1.6">São Paulo — SP<br />Atendemos a capital, Grande SP e ABC</span>
      <span style="font-size:14.5px">Segunda a sábado, das 8h às 19h</span>
    </div>
  </div>
  <div class="wrap" style="padding-top:18px; padding-bottom:36px; border-top:1px solid rgba(255,255,255,.12); display:flex; justify-content:space-between; gap:18px; flex-wrap:wrap; font-size:13px">
    <span>© 2026 {NOME} — CNPJ {CNPJ}</span>
    <span>Desenvolvido por: <a href="https://dnosistemas.com.br" target="_blank" rel="noopener" style="color:#7FE2FF; font-weight:700">dnosistemas.com.br</a></span>
  </div>
</footer>
<a href="{zap('Olá! Gostaria de um orçamento.')}" rel="noopener" target="_blank" class="fab">
  <span style="width:9px; height:9px; border-radius:50%; background:#FFF; display:block"></span>WhatsApp</a>
</body>
</html>
"""

def cta(titulo, msg):
    return f"""<section style="background:linear-gradient(120deg,#0072FF,#00C6FF)">
  <div class="wrap" style="padding-top:clamp(38px,6vw,58px); padding-bottom:clamp(38px,6vw,58px); display:flex; align-items:center; justify-content:space-between; gap:30px; flex-wrap:wrap">
    <h2 style="font-size:clamp(22px,3.4vw,30px); line-height:1.25; font-weight:800; color:#FFF; max-width:26ch">{titulo}</h2>
    <a href="{zap(msg)}" rel="noopener" target="_blank" style="display:inline-flex; align-items:center; background:#FFF; color:#003366; padding:16px 30px; border-radius:999px; font-weight:800; font-size:16px">Pedir orçamento no WhatsApp</a>
  </div>
</section>
"""

def bloco_faq(faq):
    itens = "".join(f"""<div style="background:#FFF; border:1px solid #E2E8F0; border-radius:16px; padding:22px 24px; display:flex; flex-direction:column; gap:8px">
      <h3 style="font-size:17.5px; font-weight:700; color:#003366">{p}</h3>
      <p style="font-size:15px; line-height:1.7; color:#5B6B79">{r}</p></div>""" for p, r in faq)
    return f"""<section class="sec" style="background:#F5F5F5; border-top:1px solid #E4E7E9">
  <div class="wrap">
    <span class="kicker">Perguntas frequentes</span>
    <h2 class="h2" style="margin:12px 0 28px">Dúvidas antes de contratar</h2>
    <div style="display:flex; flex-direction:column; gap:12px">{itens}</div>
  </div>
</section>
"""

def outros_servicos(slug_atual):
    cards = "".join(f"""<a href="/{s['slug']}/" class="card" style="color:inherit">
      <span style="width:36px; height:4px; border-radius:99px; background:linear-gradient(90deg,#00C6FF,#0072FF)"></span>
      <h3 style="font-size:18px; font-weight:700; color:#003366; padding-top:6px">{s['menu']}</h3>
      <p style="font-size:14.5px; line-height:1.6; color:#5B6B79">{s['resumo']}</p></a>"""
      for s in SERVICOS if s['slug'] != slug_atual)
    return f"""<section class="sec" style="background:#FFF">
  <div class="wrap">
    <span class="kicker">Outros serviços</span>
    <h2 class="h2" style="margin:12px 0 28px">Também cuidamos disso para você</h2>
    <div class="grid">{cards}</div>
  </div>
</section>
"""

def bloco_regioes(texto):
    links = "".join(f'<a href="/{r["slug"]}/" class="chip">{r["menu"]}</a>' for r in REGIOES)
    return f"""<section class="sec" style="background:#FFF; border-top:1px solid #E4E7E9">
  <div class="wrap">
    <span class="kicker">Onde atendemos</span>
    <h2 class="h2" style="margin:12px 0 14px">Atendimento em toda a São Paulo</h2>
    <p class="lead" style="max-width:70ch; margin-bottom:22px">{texto}</p>
    <div>{links}</div>
  </div>
</section>
"""

SERVICOS = [
{
 "slug":"higienizacao-de-estofados",
 "menu":"Higienização de estofados e sofás",
 "resumo":"Lavagem de sofá com extração, removendo manchas, ácaros e odores.",
 "title":"Higienização de Estofados em São Paulo | Reis Lima",
 "desc":"Empresa de lavagem de sofá em São Paulo. Higienização de estofados com extração, remoção de manchas, ácaros e odores. Orçamento grátis pelo WhatsApp.",
 "h1":"Higienização de estofados e lavagem de sofá em São Paulo",
 "imagem":"g-sofa-antes-depois.jpeg",
 "alt":"Sofá de suede antes e depois da higienização em São Paulo",
 "intro":["Se você procura uma <strong>empresa de lavagem de sofá em São Paulo</strong>, a Reis Lima faz a higienização do seu estofado no local, com equipamento de extração profissional e produtos regularizados junto à Anvisa.",
          "Removemos poeira impregnada, ácaros, manchas do dia a dia e odores de tecido — sem encharcar o estofado e sem agredir o revestimento. Atendemos residências, escritórios, clínicas e condomínios na capital, na Grande São Paulo e no ABC."],
 "inclui":["Sofás retráteis, reclináveis, de canto e chaise","Poltronas, puffs, namoradeiras e recamiers","Estofados de suede, chenille, veludo, linho e couro sintético","Cabeceiras de cama estofadas","Remoção de manchas de café, gordura, tinta e xixi de pet","Neutralização de odores e tratamento antiácaro"],
 "difs":[("Extração profissional","O equipamento injeta a solução e aspira a sujeira dissolvida no mesmo movimento, reduzindo bastante a umidade final."),
         ("Produtos seguros","Usamos produtos regularizados junto à Anvisa, seguros para crianças, idosos e animais de estimação."),
         ("Serviço no local","Não levamos o seu sofá embora. Todo o processo é feito na sua casa ou empresa, com proteção do piso e do ambiente."),
         ("Orçamento sem compromisso","Você manda fotos pelo WhatsApp, recebe o valor fechado e decide sem pressão.")],
 "faq":[("Quanto custa a higienização de um sofá em São Paulo?","O valor depende do número de lugares, do tipo de tecido e do estado do estofado. Mande uma foto pelo WhatsApp e enviamos o preço fechado, sem compromisso."),
        ("Quanto tempo o sofá leva para secar?","Varia com o tecido, a ventilação e o clima do dia. Como usamos extração, boa parte da umidade sai no próprio processo e orientamos você sobre os cuidados até a secagem completa."),
        ("A higienização remove manchas antigas?","Na maioria dos casos há melhora significativa. Manchas muito antigas ou que já desbotaram a fibra podem clarear sem sair por completo — avaliamos e falamos com honestidade antes de começar."),
        ("Vocês atendem escritórios e condomínios?","Sim. Fazemos higienização de estofados para empresas, escritórios e condomínios, inclusive em contratos de manutenção periódica.")],
 "cta":"Pronto para deixar seu sofá com cara de novo?",
 "wa":"Olá! Gostaria de um orçamento de higienização de estofados.",
 "reg":"Fazemos lavagem de sofá e higienização de estofados na Zona Sul, Zona Oeste, Zona Norte, Centro de São Paulo e em todo o ABC Paulista."
},
{
 "slug":"higienizacao-de-colchoes",
 "menu":"Higienização de colchões",
 "resumo":"Limpeza antiácaro e antifungos para um sono mais saudável.",
 "title":"Higienização de Colchões em São Paulo | Limpeza Antiácaro",
 "desc":"Higienização de colchões em São Paulo com tratamento antiácaro e antifungos. Indicado para alergia e rinite. Serviço no local, orçamento grátis no WhatsApp.",
 "h1":"Higienização de colchões em São Paulo",
 "imagem":"g-colchao.jpeg",
 "alt":"Colchão de casal antes e depois da higienização antiácaro",
 "intro":["Um terço da sua vida acontece em cima do colchão — e é ali que se acumulam ácaros, células de pele, suor e fungos. A <strong>limpeza de colchão em São Paulo</strong> da Reis Lima faz a higienização profunda com aspiração, extração e tratamento antiácaro.",
          "É o serviço mais procurado por quem tem <strong>rinite, asma ou alergia respiratória</strong>, por famílias com bebês e por quem quer preservar a vida útil do colchão."],
 "inclui":["Colchões de solteiro, casal, queen e king","Colchões de molas, espuma e viscoelástico","Camas box e box conjugado","Berços e colchões infantis","Remoção de manchas de suor, urina e leite","Tratamento antiácaro e antifungos nas duas faces"],
 "difs":[("Tratamento antiácaro","Aplicação específica contra ácaros e fungos, o principal gatilho de crises alérgicas dentro de casa."),
         ("Nas duas faces","Higienizamos as duas faces e as laterais do colchão, além da base box quando houver."),
         ("Sem encharcar","O processo de extração controla a umidade para que o colchão volte a ser usado no mesmo dia, conforme orientação."),
         ("Produtos seguros","Regularizados junto à Anvisa, indicados para quartos de crianças e pessoas alérgicas.")],
 "faq":[("Com que frequência devo higienizar o colchão?","Recomenda-se a cada 6 meses. Para alérgicos, pessoas com rinite ou lares com pets, o intervalo de 3 a 4 meses costuma dar mais resultado."),
        ("Posso dormir no colchão no mesmo dia?","Na maioria dos casos sim. Orientamos o tempo de ventilação necessário conforme o tipo de colchão e o clima do dia."),
        ("A higienização tira manchas de xixi?","Trabalhamos a mancha e o odor com produtos específicos. O resultado depende de quanto tempo a mancha ficou impregnada, mas a melhora costuma ser bem visível."),
        ("Quanto custa a higienização de um colchão?","Depende do tamanho e do estado. Envie o tipo de colchão pelo WhatsApp e passamos o valor na hora, sem compromisso.")],
 "cta":"Durma melhor em um colchão realmente limpo.",
 "wa":"Olá! Gostaria de um orçamento de higienização de colchão.",
 "reg":"Atendemos higienização de colchões na Zona Sul, Zona Oeste, Zona Norte, Centro de São Paulo e no ABC Paulista."
},
{
 "slug":"higienizacao-de-cadeiras",
 "menu":"Higienização de cadeiras e poltronas",
 "resumo":"Cadeiras de jantar, poltronas e cadeiras de escritório.",
 "title":"Higienização de Cadeiras e Poltronas em São Paulo | Reis Lima",
 "desc":"Higienização de cadeiras de jantar, poltronas e cadeiras de escritório em São Paulo. Atendimento a empresas e condomínios. Orçamento grátis no WhatsApp.",
 "h1":"Higienização de cadeiras e poltronas em São Paulo",
 "imagem":"g-sofa-equipe.jpeg",
 "alt":"Equipe da Reis Lima higienizando estofado em São Paulo",
 "intro":["Cadeiras de jantar e cadeiras de escritório recebem uso diário e acumulam suor, gordura e poeira no tecido. A Reis Lima faz a <strong>higienização de cadeiras em São Paulo</strong> peça por peça, com extração e secagem controlada.",
          "É o serviço ideal para <strong>escritórios, coworkings, restaurantes, clínicas e salas de reunião</strong>, além de residências com mesa de jantar estofada."],
 "inclui":["Cadeiras de jantar estofadas","Cadeiras de escritório e presidente","Poltronas de leitura, amamentação e decorativas","Banquetas, puffs e cadeiras de recepção","Higienização em lote para empresas","Contratos de manutenção periódica"],
 "difs":[("Preço por peça","Orçamento por unidade, com desconto progressivo para lotes de cadeiras de escritório."),
         ("Fora do horário comercial","Para empresas, agendamos em horários que não interrompem a operação."),
         ("Secagem rápida","Peças menores secam mais rápido, o que permite devolver o ambiente ao uso no mesmo dia."),
         ("Nota fiscal para empresas","Emitimos nota fiscal — CNPJ " + CNPJ + ".")],
 "faq":[("Vocês fazem higienização de cadeiras de escritório em lote?","Sim. Atendemos escritórios e coworkings com dezenas de cadeiras, com preço por peça e agendamento fora do horário de pico."),
        ("O serviço é feito no local?","Sim, higienizamos as cadeiras no seu escritório ou residência, com proteção do piso e organização do ambiente."),
        ("Quanto tempo demora?","Depende da quantidade. Uma cadeira leva poucos minutos; um lote de escritório é planejado no orçamento com prazo definido."),
        ("Atendem condomínios e áreas comuns?","Sim, incluindo salões de festa, salas de reunião e áreas de convivência.")],
 "cta":"Cadeiras limpas, ambiente com outra cara.",
 "wa":"Olá! Gostaria de um orçamento de higienização de cadeiras.",
 "reg":"Higienizamos cadeiras e poltronas na Zona Sul, Zona Oeste, Zona Norte, Centro de São Paulo e no ABC Paulista."
},
{
 "slug":"limpeza-de-tapetes",
 "menu":"Limpeza de tapetes",
 "resumo":"Lavagem por tipo de fibra, com secagem controlada.",
 "title":"Limpeza de Tapetes em São Paulo | Preço e Orçamento Grátis",
 "desc":"Limpeza de tapetes em São Paulo com lavagem adequada a cada fibra e secagem controlada. Peça o preço da higienização do seu tapete pelo WhatsApp.",
 "h1":"Limpeza e higienização de tapetes em São Paulo",
 "imagem":"g-sofa-depois.jpeg",
 "alt":"Tapete higienizado pela Reis Lima em São Paulo",
 "intro":["Quem pesquisa <strong>limpeza de tapetes preço</strong> quer saber duas coisas: quanto custa e se o tapete volta bonito. A Reis Lima orça por metro quadrado e escolhe o processo conforme a fibra, para preservar cor, textura e trama.",
          "Fazemos a higienização de tapetes em São Paulo com aspiração profunda, tratamento de manchas, lavagem e secagem controlada."],
 "inclui":["Tapetes de sala, quarto e hall","Fibras sintéticas, lã, sisal e algodão","Tapetes felpudos, shaggy e de pelo alto","Passadeiras e capachos internos","Remoção de manchas e neutralização de odores","Tratamento antiácaro para alérgicos"],
 "difs":[("Processo por fibra","Cada material pede um método. Identificamos a fibra antes de começar para não desbotar nem encolher a peça."),
         ("Orçamento por metro quadrado","Preço transparente: você informa as medidas e recebe o valor fechado."),
         ("Secagem controlada","Controlamos a umidade para evitar cheiro de mofo e deformação da trama."),
         ("Antiácaro opcional","Tapete é o maior acumulador de ácaros da casa. O tratamento pode ser incluído no serviço.")],
 "faq":[("Qual o preço da limpeza de tapete?","O cálculo é por metro quadrado e varia conforme a fibra e o estado do tapete. Informe as medidas pelo WhatsApp e enviamos o valor na hora."),
        ("O tapete é lavado na minha casa?","Sim, na maioria dos casos fazemos a higienização no local. Peças que exigem imersão são avaliadas caso a caso no orçamento."),
        ("Tapete de lã pode ser lavado?","Pode, com produto e umidade adequados à fibra. É justamente por isso que identificamos o material antes de iniciar."),
        ("Quanto tempo leva para secar?","Depende da espessura do pelo e da ventilação do ambiente. Orientamos os cuidados até a secagem completa.")],
 "cta":"Seu tapete de volta à cor original.",
 "wa":"Olá! Gostaria de um orçamento de limpeza de tapete.",
 "reg":"Fazemos limpeza de tapetes na Zona Sul, Zona Oeste, Zona Norte, Centro de São Paulo e no ABC Paulista."
},
{
 "slug":"impermeabilizacao-de-estofados",
 "menu":"Impermeabilização de estofados",
 "resumo":"Proteção que repele líquidos e facilita a limpeza do dia a dia.",
 "title":"Impermeabilização de Sofás e Estofados em São Paulo | Reis Lima",
 "desc":"Impermeabilização de sofás e estofados em São Paulo. Proteção que repele líquidos, evita manchas e facilita a limpeza. Orçamento grátis pelo WhatsApp.",
 "h1":"Impermeabilização de sofás e estofados em São Paulo",
 "imagem":"g-teste-agua.jpeg",
 "alt":"Teste da água em estofado impermeabilizado pela Reis Lima",
 "intro":["A impermeabilização cria uma barreira invisível no tecido: o líquido derramado forma gotas na superfície em vez de penetrar na fibra, e você limpa com um pano antes que vire mancha.",
          "É a escolha de quem tem <strong>crianças pequenas, animais de estimação ou estofado de tecido claro</strong> — e de quem acabou de comprar um sofá novo e quer conservá-lo."],
 "inclui":["Sofás, poltronas e cadeiras estofadas","Cabeceiras de cama e recamiers","Tapetes e passadeiras","Estofados novos, recém-comprados","Aplicação após a higienização, para melhor fixação","Teste da água demonstrado no fim do serviço"],
 "difs":[("Barreira contra líquidos","Café, refrigerante, suco e xixi de pet ficam na superfície e saem com um pano seco."),
         ("Não altera o toque","O produto não deixa o tecido plastificado nem muda a cor do revestimento."),
         ("Melhor após higienizar","Aplicamos sobre o tecido limpo, o que garante fixação uniforme e mais durabilidade."),
         ("Prolonga a vida do estofado","Menos limpezas agressivas ao longo do tempo significam mais anos de tecido bonito.")],
 "faq":[("Quanto tempo dura a impermeabilização?","A durabilidade depende do uso, da frequência de limpeza e do tipo de tecido. Orientamos no orçamento o intervalo indicado para o seu caso."),
        ("Pode ser aplicada em sofá usado?","Pode. O ideal é higienizar antes, para que a proteção não sele a sujeira dentro da fibra."),
        ("O produto é seguro para crianças e pets?","Usamos produtos regularizados junto à Anvisa. Respeitado o tempo de secagem, o estofado volta ao uso normal."),
        ("Quanto tempo até poder usar o sofá?","Informamos o tempo de secagem no dia do serviço, conforme o produto aplicado e a ventilação do ambiente.")],
 "cta":"Proteja seu estofado antes da próxima mancha.",
 "wa":"Olá! Gostaria de um orçamento de impermeabilização de estofados.",
 "reg":"Impermeabilizamos estofados na Zona Sul, Zona Oeste, Zona Norte, Centro de São Paulo e no ABC Paulista."
},
{
 "slug":"cristalizacao-de-vidros",
 "menu":"Cristalização e limpeza de vidros",
 "resumo":"Remoção de manchas e proteção que devolve o brilho ao vidro.",
 "title":"Cristalização de Vidros em São Paulo | Limpeza de Vidros SP",
 "desc":"Cristalização e limpeza de vidros em São Paulo: sacadas, box, janelas e guarda-corpos. Remove manchas, protege e devolve o brilho. Orçamento no WhatsApp.",
 "h1":"Cristalização e limpeza de vidros em São Paulo",
 "imagem":"g-vidros.jpeg",
 "alt":"Vidros de sacada antes e depois da cristalização em São Paulo",
 "intro":["Vidro manchado de chuva ácida, resíduo de obra ou marca de água dura não sai com limpeza comum. A <strong>cristalização de vidros</strong> remove essas incrustações e aplica uma proteção que repele água e sujeira, deixando a superfície lisa e brilhante.",
          "Atendemos <strong>sacadas envidraçadas, box de banheiro, janelas, portas, espelhos e guarda-corpos</strong> em residências, comércios e condomínios de São Paulo."],
 "inclui":["Sacadas e varandas envidraçadas","Box de banheiro com mancha de água dura","Janelas, portas e vitrines","Guarda-corpos e divisórias de vidro","Espelhos e tampos","Remoção de respingo de tinta, cimento e rejunte pós-obra"],
 "difs":[("Remove o que a limpeza comum não tira","Incrustações minerais e manchas de chuva exigem cristalização, não apenas detergente."),
         ("Proteção duradoura","A camada aplicada repele água e sujeira, o que espaça a necessidade de limpezas pesadas."),
         ("Pós-obra","Removemos respingos de tinta, cimento e rejunte sem riscar o vidro."),
         ("Comércios e condomínios","Atendemos vitrines, lojas e áreas comuns com agendamento fora do horário de pico.")],
 "faq":[("Qual a diferença entre limpar e cristalizar o vidro?","A limpeza remove a sujeira da superfície. A cristalização remove incrustações que já penetraram no vidro e aplica uma proteção que evita que voltem tão rápido."),
        ("Cristalização resolve mancha de box de banheiro?","Sim, é um dos casos mais comuns. A mancha esbranquiçada do box é depósito mineral da água, exatamente o que a cristalização trata."),
        ("Quanto custa a cristalização de vidros?","O orçamento é por metragem. Informe as medidas ou envie fotos pelo WhatsApp e passamos o valor."),
        ("Atendem condomínios?","Sim, inclusive em contratos de manutenção periódica de vidros e áreas comuns.")],
 "cta":"Vidros sem mancha, com brilho de novo.",
 "wa":"Olá! Gostaria de um orçamento de cristalização de vidros.",
 "reg":"Fazemos cristalização e limpeza de vidros na Zona Sul, Zona Oeste, Zona Norte, Centro de São Paulo e no ABC Paulista."
},
{
 "slug":"limpeza-de-fachadas",
 "menu":"Limpeza de fachadas de vidro",
 "resumo":"Fachadas envidraçadas de prédios, lojas e condomínios.",
 "title":"Limpeza de Fachadas de Vidro em SP | Fachada Envidraçada",
 "desc":"Limpeza de fachadas de vidro em São Paulo para prédios, lojas e condomínios. Cristalização de fachada envidraçada com equipe própria. Orçamento no WhatsApp.",
 "h1":"Limpeza de fachadas de vidro em São Paulo",
 "imagem":"g-fachada.jpeg",
 "alt":"Limpeza de fachada envidraçada em altura em São Paulo",
 "intro":["A fachada é o cartão de visita do prédio ou da loja. Poluição, chuva e resíduo de obra deixam o vidro opaco e manchado em poucos meses. A Reis Lima faz a <strong>limpeza de fachada de vidro em SP</strong> com equipe própria e cristalização opcional.",
          "Atendemos <strong>condomínios residenciais e comerciais, lojas, escritórios e galerias</strong>, com agendamento planejado para não atrapalhar moradores e clientes."],
 "inclui":["Fachadas envidraçadas de prédios","Vitrines e fachadas de lojas","Pele de vidro e esquadrias","Cristalização de fachada de vidro","Limpeza pós-obra e pós-reforma","Contratos de manutenção periódica"],
 "difs":[("Equipe própria","O serviço é executado pela nossa equipe, com contato direto com você em todas as etapas."),
         ("Cristalização opcional","Além da limpeza, aplicamos a proteção que retarda o retorno das manchas de chuva e poluição."),
         ("Agenda planejada","Definimos data e horário junto com o síndico ou o gestor para reduzir o impacto na rotina."),
         ("Nota fiscal e CNPJ","Empresa formalizada — CNPJ " + CNPJ + " — com documentação para administradoras e condomínios.")],
 "faq":[("Vocês atendem condomínios e administradoras?","Sim. Atendemos condomínios residenciais e comerciais, inclusive em contratos periódicos, com toda a documentação para a administradora."),
        ("Como é feito o orçamento da fachada?","Avaliamos a metragem, a altura e as condições de acesso. Envie fotos e o endereço pelo WhatsApp para uma primeira estimativa."),
        ("Fazem limpeza pós-obra?","Sim, incluindo remoção de respingos de tinta, cimento e rejunte dos vidros e esquadrias."),
        ("Com que frequência a fachada deve ser limpa?","Depende da exposição à poluição e à chuva. Em São Paulo, muitos condomínios adotam manutenção semestral.")],
 "cta":"Fachada limpa valoriza todo o prédio.",
 "wa":"Olá! Gostaria de um orçamento de limpeza de fachada de vidro.",
 "reg":"Atendemos limpeza de fachadas na Zona Sul, Zona Oeste, Zona Norte, Centro de São Paulo e no ABC Paulista."
},
]

REGIOES = [
{
 "slug":"higienizacao-de-estofados-zona-sul",
 "menu":"Zona Sul de SP",
 "nome":"Zona Sul de São Paulo",
 "title":"Higienização de Estofados na Zona Sul de SP | Reis Lima",
 "desc":"Empresa de lavagem de sofá na Zona Sul de SP: higienização de estofados, colchões, tapetes e cristalização de vidros em Moema, Vila Mariana, Brooklin e região.",
 "h1":"Atendemos higienização de estofados na Zona Sul de SP",
 "imagem":"g-sofa-antes-depois.jpeg",
 "intro":["Procurando uma <strong>empresa de lavagem de sofá na Zona Sul</strong>? A Reis Lima atende toda a região com higienização de estofados, colchões, cadeiras e tapetes, além de limpeza e cristalização de vidros e fachadas.",
          "O serviço é feito na sua casa, no escritório ou no condomínio, com equipe própria e agendamento de segunda a sábado, das 8h às 19h."],
 "bairros":["Moema","Vila Mariana","Itaim Bibi","Vila Olímpia","Brooklin","Campo Belo","Santo Amaro","Morumbi","Chácara Santo Antônio","Saúde","Jabaquara","Ipiranga","Vila Clementino","Cidade Monções","Granja Julieta","Interlagos"],
 "wa":"Olá! Sou da Zona Sul de SP e gostaria de um orçamento."
},
{
 "slug":"higienizacao-de-estofados-zona-oeste",
 "menu":"Zona Oeste e Alphaville",
 "nome":"Zona Oeste de São Paulo e Alphaville",
 "title":"Higienização de Estofados na Zona Oeste de SP e Alphaville",
 "desc":"Lavagem de sofá e higienização de estofados na Zona Oeste de SP e em Alphaville: Pinheiros, Vila Madalena, Perdizes, Butantã, Barueri e Osasco.",
 "h1":"Higienização de estofados na Zona Oeste de SP e Alphaville",
 "imagem":"g-sofa-extracao.jpeg",
 "intro":["A Reis Lima atende a <strong>Zona Oeste de São Paulo e a região de Alphaville</strong> com higienização de estofados, colchões, cadeiras e tapetes, impermeabilização e cristalização de vidros e fachadas.",
          "Atendemos apartamentos, casas, escritórios e condomínios, com orçamento gratuito pelo WhatsApp e agenda de segunda a sábado."],
 "bairros":["Pinheiros","Vila Madalena","Alto de Pinheiros","Perdizes","Pompeia","Lapa","Vila Leopoldina","Butantã","Sumaré","Barra Funda","Água Branca","Rio Pequeno","Alphaville","Barueri","Osasco","Tamboré"],
 "wa":"Olá! Sou da Zona Oeste/Alphaville e gostaria de um orçamento."
},
{
 "slug":"higienizacao-de-estofados-zona-norte-centro",
 "menu":"Zona Norte e Centro",
 "nome":"Zona Norte e Centro de São Paulo",
 "title":"Higienização de Estofados na Zona Norte e Centro de SP",
 "desc":"Higienização de estofados, colchões e tapetes na Zona Norte e no Centro de São Paulo: Santana, Tucuruvi, Higienópolis, Bela Vista e Santa Cecília.",
 "h1":"Higienização de estofados na Zona Norte e Centro de SP",
 "imagem":"g-sofa-equipe.jpeg",
 "intro":["Atendemos a <strong>Zona Norte e o Centro de São Paulo</strong> com higienização de estofados, colchões, cadeiras e tapetes, além de limpeza e cristalização de vidros, box e fachadas.",
          "Trabalhamos com residências, escritórios, lojas e condomínios, com serviço feito no local e orçamento sem compromisso."],
 "bairros":["Santana","Tucuruvi","Casa Verde","Mandaqui","Horto Florestal","Vila Guilherme","Freguesia do Ó","Jaçanã","Higienópolis","Santa Cecília","Bela Vista","Consolação","República","Liberdade","Bom Retiro","Vila Buarque"],
 "wa":"Olá! Sou da Zona Norte/Centro de SP e gostaria de um orçamento."
},
{
 "slug":"higienizacao-de-estofados-abc-paulista",
 "menu":"ABC Paulista",
 "nome":"ABC Paulista",
 "title":"Higienização de Estofados no ABC Paulista | Reis Lima",
 "desc":"Lavagem de sofá e higienização de estofados no ABC Paulista: Santo André, São Bernardo, São Caetano, Diadema e Mauá. Orçamento grátis pelo WhatsApp.",
 "h1":"Higienização de estofados no ABC Paulista",
 "imagem":"g-colchao.jpeg",
 "intro":["A Reis Lima atende o <strong>ABC Paulista</strong> com higienização de estofados, colchões, cadeiras e tapetes, impermeabilização e limpeza e cristalização de vidros e fachadas.",
          "Atendimento residencial e empresarial, com equipe própria, produtos regularizados junto à Anvisa e agenda de segunda a sábado."],
 "bairros":["Santo André","São Bernardo do Campo","São Caetano do Sul","Diadema","Mauá","Ribeirão Pires","Rudge Ramos","Jardim do Mar","Vila Assunção","Bairro Jardim","Centro de Santo André","Paulicéia"],
 "wa":"Olá! Sou do ABC Paulista e gostaria de um orçamento."
},
]

BAIRROS_JSON = ",".join(f'{{"@type":"City","name":"{b}"}}' for r in REGIOES for b in r["bairros"])

def ld_negocio(url):
    return ('{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness",'
      f'"@id":"{SITE}/#negocio","name":"{NOME}","alternateName":"Reis Lima",'
      f'"url":"{SITE}/","image":"{SITE}/assets/hero-sofa-vista.jpeg","logo":"{SITE}/assets/logo-reis-lima-hi.png",'
      '"description":"Higienização de estofados, colchões, cadeiras e tapetes, impermeabilização e limpeza e cristalização de vidros e fachadas em São Paulo e região.",'
      f'"telephone":"{TEL1_R}","email":"{EMAIL}","taxID":"{CNPJ}","priceRange":"$$",'
      '"address":{"@type":"PostalAddress","addressLocality":"São Paulo","addressRegion":"SP","addressCountry":"BR"},'
      '"geo":{"@type":"GeoCoordinates","latitude":-23.5505,"longitude":-46.6333},'
      '"areaServed":[{"@type":"City","name":"São Paulo"},{"@type":"AdministrativeArea","name":"Grande São Paulo"},{"@type":"AdministrativeArea","name":"ABC Paulista"}],'
      '"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"19:00"}],'
      '"foundingDate":"2021",'
      f'"sameAs":["https://wa.me/{WA}"]}}')

def ld_faq(faq):
    itens = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (p, r) for p, r in faq)
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % itens

def ld_breadcrumb(nome, url):
    return ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      f'{{"@type":"ListItem","position":1,"name":"Início","item":"{SITE}/"}},'
      f'{{"@type":"ListItem","position":2,"name":"{nome}","item":"{url}"}}]}}')

def ld_service(s, url):
    return ('{"@context":"https://schema.org","@type":"Service",'
      f'"name":"{s["menu"]} em São Paulo","serviceType":"{s["menu"]}",'
      f'"description":"{s["desc"]}","url":"{url}",'
      f'"provider":{{"@type":"HomeAndConstructionBusiness","name":"{NOME}","telephone":"{TEL1_R}","url":"{SITE}/"}},'
      f'"areaServed":[{{"@type":"City","name":"São Paulo"}},{{"@type":"AdministrativeArea","name":"ABC Paulista"}}],'
      '"availableChannel":{"@type":"ServiceChannel","serviceUrl":"%s"}}' % zap(s["wa"]))

def pagina_servico(s):
    url = f"{SITE}/{s['slug']}/"
    ld = '[' + ld_negocio(url) + ',' + ld_service(s, url) + ',' + ld_faq(s["faq"]) + ',' + ld_breadcrumb(s["menu"], url) + ']'
    intro = "".join(f'<p class="lead" style="max-width:64ch">{p}</p>' for p in s["intro"])
    inclui = "".join(f"<li>{i}</li>" for i in s["inclui"])
    difs = "".join(f"""<div class="card">
      <span style="width:36px; height:4px; border-radius:99px; background:linear-gradient(90deg,#00C6FF,#0072FF)"></span>
      <h3 style="font-size:18.5px; font-weight:700; color:#003366; padding-top:6px">{t}</h3>
      <p style="font-size:15px; line-height:1.65; color:#5B6B79">{d}</p></div>""" for t, d in s["difs"])
    return (head(s["title"], s["desc"], url, s["imagem"], ld) + header() + breadcrumb(s["menu"]) + f"""
<section style="background:linear-gradient(160deg,#003366 0%,#0072FF 58%,#00C6FF 100%); color:#FFF; overflow:hidden">
  <div class="wrap" style="padding-top:clamp(40px,6vw,72px); padding-bottom:clamp(44px,6vw,78px); display:grid; grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr)); gap:clamp(28px,5vw,52px); align-items:center">
    <div style="display:flex; flex-direction:column; align-items:flex-start; gap:22px">
      <span style="font-size:12.5px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.22); padding:7px 13px; border-radius:999px">São Paulo, Grande SP e ABC</span>
      <h1 style="font-size:clamp(28px,5.4vw,46px); line-height:1.08; font-weight:800; max-width:18ch">{s['h1']}</h1>
      <p style="font-size:clamp(15.5px,1.8vw,18px); line-height:1.65; color:#C9E9F7; max-width:48ch">{s['resumo']} Orçamento gratuito e sem compromisso pelo WhatsApp.</p>
      <div style="display:flex; gap:12px; flex-wrap:wrap">
        <a href="{zap(s['wa'])}" rel="noopener" target="_blank" class="btn">Pedir orçamento grátis</a>
        <a href="tel:{TEL2_R}" class="btn-o">Ligar {TEL2}</a>
      </div>
    </div>
    <div style="position:relative; height:clamp(230px,38vw,380px); border-radius:24px; overflow:hidden; box-shadow:0 26px 60px rgba(0,0,0,.35)">
      <img src="/assets/{s['imagem']}" alt="{s['alt']}" width="1200" height="800" style="width:100%; height:100%; object-fit:cover; display:block" />
    </div>
  </div>
</section>

<section class="sec" style="background:#FFF">
  <div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr)); gap:clamp(28px,5vw,52px)">
    <div style="display:flex; flex-direction:column; gap:16px">
      <span class="kicker">O serviço</span>
      <h2 class="h2">{s['menu']} feita com processo próprio</h2>
      {intro}
    </div>
    <div style="background:#F5F5F5; border-radius:20px; padding:30px 28px">
      <h3 style="font-size:19px; font-weight:700; color:#003366; margin-bottom:14px">O que atendemos</h3>
      <ul>{inclui}</ul>
    </div>
  </div>
</section>

<section class="sec" style="background:#F5F5F5; border-top:1px solid #E4E7E9">
  <div class="wrap">
    <span class="kicker">Por que a Reis Lima</span>
    <h2 class="h2" style="margin:12px 0 28px">Atuamos desde 2021 em São Paulo</h2>
    <div class="grid">{difs}</div>
  </div>
</section>

<section class="sec" style="background:#FFF">
  <div class="wrap">
    <span class="kicker">Como funciona</span>
    <h2 class="h2" style="margin:12px 0 28px">Três passos até o resultado</h2>
    <div class="grid">
      <div style="background:#F5F5F5; border-radius:20px; padding:30px 28px; display:flex; flex-direction:column; gap:10px">
        <span style="font-family:'Plus Jakarta Sans'; font-size:15px; font-weight:800; color:#00C6FF; letter-spacing:.1em">01</span>
        <h3 style="font-size:19px; font-weight:700; color:#003366">Você fala com a gente</h3>
        <p style="font-size:15px; line-height:1.65; color:#5B6B79">Mande uma mensagem no WhatsApp contando o que precisa e, se possível, envie fotos das peças ou do ambiente.</p></div>
      <div style="background:#F5F5F5; border-radius:20px; padding:30px 28px; display:flex; flex-direction:column; gap:10px">
        <span style="font-family:'Plus Jakarta Sans'; font-size:15px; font-weight:800; color:#00C6FF; letter-spacing:.1em">02</span>
        <h3 style="font-size:19px; font-weight:700; color:#003366">Orçamento e agendamento</h3>
        <p style="font-size:15px; line-height:1.65; color:#5B6B79">Avaliamos o serviço, passamos o valor sem compromisso e agendamos no melhor horário para você.</p></div>
      <div style="background:#F5F5F5; border-radius:20px; padding:30px 28px; display:flex; flex-direction:column; gap:10px">
        <span style="font-family:'Plus Jakarta Sans'; font-size:15px; font-weight:800; color:#00C6FF; letter-spacing:.1em">03</span>
        <h3 style="font-size:19px; font-weight:700; color:#003366">Serviço realizado</h3>
        <p style="font-size:15px; line-height:1.65; color:#5B6B79">Nossa equipe executa o serviço no local, com cuidado no manuseio e organização do ambiente.</p></div>
    </div>
  </div>
</section>
""" + bloco_regioes(s["reg"]) + bloco_faq(s["faq"]) + outros_servicos(s["slug"]) + cta(s["cta"], s["wa"]) + footer())


def pagina_regiao(r):
    url = f"{SITE}/{r['slug']}/"
    faq = [("Vocês atendem toda a %s?" % r["nome"], "Sim. Atendemos os principais bairros da região. Envie o seu endereço pelo WhatsApp e confirmamos a disponibilidade na hora."),
           ("O serviço é feito na minha casa?", "Sim. Higienizamos estofados, colchões, cadeiras e tapetes no local, com proteção do piso e organização do ambiente."),
           ("Qual o horário de atendimento?", "De segunda a sábado, das 8h às 19h. O agendamento é feito no horário mais conveniente para você dentro desse período."),
           ("Como peço um orçamento?", "Pelo WhatsApp %s. Informe o serviço, a quantidade de peças ou a metragem e, se possível, envie fotos. O orçamento é gratuito." % TEL1)]
    ld = ('[' + ld_negocio(url) + ',' + ld_faq(faq) + ',' + ld_breadcrumb(r["menu"], url) + ']')
    intro = "".join(f'<p class="lead" style="max-width:64ch">{p}</p>' for p in r["intro"])
    chips = "".join(f'<span class="chip">{b}</span>' for b in r["bairros"])
    servs = "".join(f"""<a href="/{s['slug']}/" class="card" style="color:inherit">
      <span style="width:36px; height:4px; border-radius:99px; background:linear-gradient(90deg,#00C6FF,#0072FF)"></span>
      <h3 style="font-size:18px; font-weight:700; color:#003366; padding-top:6px">{s['menu']} na {r['menu']}</h3>
      <p style="font-size:14.5px; line-height:1.6; color:#5B6B79">{s['resumo']}</p></a>""" for s in SERVICOS)
    outras = "".join(f'<a href="/{o["slug"]}/" class="chip">{o["menu"]}</a>' for o in REGIOES if o["slug"] != r["slug"])
    return (head(r["title"], r["desc"], url, r["imagem"], ld) + header() + breadcrumb(r["menu"]) + f"""
<section style="background:linear-gradient(160deg,#003366 0%,#0072FF 58%,#00C6FF 100%); color:#FFF">
  <div class="wrap" style="padding-top:clamp(40px,6vw,70px); padding-bottom:clamp(44px,6vw,74px); display:grid; grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr)); gap:clamp(28px,5vw,52px); align-items:center">
    <div style="display:flex; flex-direction:column; align-items:flex-start; gap:22px">
      <span style="font-size:12.5px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; background:rgba(212,175,55,.18); border:1px solid rgba(212,175,55,.45); color:#E8D9A8; padding:7px 13px; border-radius:999px">{r['nome']}</span>
      <h1 style="font-size:clamp(27px,5.2vw,44px); line-height:1.08; font-weight:800; max-width:19ch">{r['h1']}</h1>
      <p style="font-size:clamp(15.5px,1.8vw,18px); line-height:1.65; color:#C9E9F7; max-width:48ch">Estofados, colchões, cadeiras, tapetes, vidros e fachadas. Serviço no local, de segunda a sábado, das 8h às 19h.</p>
      <div style="display:flex; gap:12px; flex-wrap:wrap">
        <a href="{zap(r['wa'])}" rel="noopener" target="_blank" class="btn">Pedir orçamento grátis</a>
        <a href="tel:{TEL2_R}" class="btn-o">Ligar {TEL2}</a>
      </div>
    </div>
    <div style="position:relative; height:clamp(220px,36vw,360px); border-radius:24px; overflow:hidden; box-shadow:0 26px 60px rgba(0,0,0,.35)">
      <img src="/assets/{r['imagem']}" alt="Higienização de estofados na {r['nome']}" width="1200" height="800" style="width:100%; height:100%; object-fit:cover; display:block" />
    </div>
  </div>
</section>

<section class="sec" style="background:#FFF">
  <div class="wrap" style="display:flex; flex-direction:column; gap:16px">
    <span class="kicker">Atendimento local</span>
    <h2 class="h2">Higienização com equipe própria na {r['menu']}</h2>
    {intro}
  </div>
</section>

<section class="sec" style="background:#F5F5F5; border-top:1px solid #E4E7E9">
  <div class="wrap">
    <span class="kicker">Bairros e cidades</span>
    <h2 class="h2" style="margin:12px 0 14px">Onde atendemos na {r['menu']}</h2>
    <p class="lead" style="max-width:66ch; margin-bottom:22px">Estes são os pontos que mais atendemos na região. Se o seu bairro não estiver na lista, mande o endereço pelo WhatsApp — provavelmente atendemos também.</p>
    <div>{chips}</div>
  </div>
</section>

<section class="sec" style="background:#FFF">
  <div class="wrap">
    <span class="kicker">Serviços na região</span>
    <h2 class="h2" style="margin:12px 0 28px">O que fazemos na {r['menu']}</h2>
    <div class="grid">{servs}</div>
  </div>
</section>

<section class="sec" style="background:#F5F5F5; border-top:1px solid #E4E7E9">
  <div class="wrap">
    <span class="kicker">Outras regiões</span>
    <h2 class="h2" style="margin:12px 0 18px">Também atendemos</h2>
    <div>{outras}</div>
  </div>
</section>
""" + bloco_faq(faq) + cta("Precisa de higienização na %s?" % r["menu"], r["wa"]) + footer())


def main():
    urls = [(SITE + "/", "1.0", "weekly")]
    for s in SERVICOS:
        d = os.path.join(RAIZ, s["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(pagina_servico(s))
        urls.append((f"{SITE}/{s['slug']}/", "0.9", "monthly"))
    for r in REGIOES:
        d = os.path.join(RAIZ, r["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(pagina_regiao(r))
        urls.append((f"{SITE}/{r['slug']}/", "0.8", "monthly"))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, p, f in urls:
        sm.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{HOJE}</lastmod>\n    <changefreq>{f}</changefreq>\n    <priority>{p}</priority>\n  </url>")
    sm.append("</urlset>\n")
    open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm))
    open(os.path.join(RAIZ, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: %s/sitemap.xml\n" % SITE)
    print("Paginas geradas:", len(urls) - 1)

if __name__ == "__main__":
    main()
